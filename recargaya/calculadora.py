MONTO_MINIMO = 1_000
MONTO_MAXIMO = 50_000
UMBRAL_BONO_ALTO = 30_000
UMBRAL_BONO_BAJO = 10_000
BONO_ALTO = 25
BONO_BAJO = 10


def calcular_recarga(monto: float, premium: bool = False) -> dict:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise ValueError("Monto fuera del rango permitido")

    if monto >= UMBRAL_BONO_ALTO:
        bonificacion = BONO_ALTO
    elif monto >= UMBRAL_BONO_BAJO:
        bonificacion = BONO_BAJO
    else:
        bonificacion = 0

    return {
        "monto": monto,
        "bonificacion_porcentaje": bonificacion,
    }