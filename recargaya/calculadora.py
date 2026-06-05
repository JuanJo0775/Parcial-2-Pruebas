MONTO_MINIMO = 1_000
MONTO_MAXIMO = 50_000
UMBRAL_BONO_ALTO = 30_000
UMBRAL_BONO_BAJO = 10_000
BONO_ALTO = 25
BONO_BAJO = 10
BONO_PREMIUM = 5


def _calcular_bonificacion_base(monto: float) -> int:
    if monto >= UMBRAL_BONO_ALTO:
        return BONO_ALTO
    if monto >= UMBRAL_BONO_BAJO:
        return BONO_BAJO
    return 0


def _calcular_datos_bonificados(monto: float, bonificacion: int) -> float:
    return round(monto * bonificacion / 100, 2)


def calcular_recarga(monto: float, premium: bool = False) -> dict:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise ValueError("Monto fuera del rango permitido")

    bonificacion = _calcular_bonificacion_base(monto)

    if premium and bonificacion > 0:
        bonificacion += BONO_PREMIUM

    datos_bonificados = _calcular_datos_bonificados(monto, bonificacion)

    return {
        "monto": monto,
        "bonificacion_porcentaje": bonificacion,
        "datos_bonificados": datos_bonificados,
        "premium": premium,
    }