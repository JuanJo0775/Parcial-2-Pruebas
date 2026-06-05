MONTO_MINIMO = 1_000
MONTO_MAXIMO = 50_000
UMBRAL_BONO_ALTO = 30_000
UMBRAL_BONO_BAJO = 10_000
BONO_ALTO = 25
BONO_BAJO = 10


def _calcular_bonificacion_base(monto: float) -> int:
    if monto >= UMBRAL_BONO_ALTO:
        return BONO_ALTO
    if monto >= UMBRAL_BONO_BAJO:
        return BONO_BAJO
    return 0


def calcular_recarga(monto: float, premium: bool = False) -> dict:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise ValueError("Monto fuera del rango permitido")

    bonificacion = _calcular_bonificacion_base(monto)

    return {
        "monto": monto,
        "bonificacion_porcentaje": bonificacion,
    }