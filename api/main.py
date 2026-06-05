from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from recargaya.calculadora import calcular_recarga

app = FastAPI(
    title="RecargaYa API",
    description="API REST para calcular el valor final de recargas de celular",
    version="1.0.0",
)


class RecargaRequest(BaseModel):
    monto: float
    premium: bool = False

    @field_validator("monto")
    @classmethod
    def monto_debe_ser_positivo(cls, v):
        if v <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        return v


class RecargaResponse(BaseModel):
    monto: float
    bonificacion_porcentaje: int
    datos_bonificados: float
    premium: bool


@app.get("/")
def raiz():
    return {"servicio": "RecargaYa API", "version": "1.0.0", "estado": "activo"}


@app.get("/health")
def health():
    return {"estado": "ok"}


@app.post("/recargas/calcular", response_model=RecargaResponse)
def calcular(request: RecargaRequest):
    try:
        resultado = calcular_recarga(
            monto=request.monto,
            premium=request.premium,
        )
        return RecargaResponse(**resultado)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))