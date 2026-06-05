def calcular_recarga(monto: float, premium: bool = False) -> dict:
    if monto < 1000 or monto > 50000:
        raise ValueError("Monto fuera del rango permitido")
    return {}