MONTO_MINIMO = 1_000
MONTO_MAXIMO = 50_000


def calcular_recarga(monto: float, premium: bool = False) -> dict:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise ValueError("Monto fuera del rango permitido")
    return {}