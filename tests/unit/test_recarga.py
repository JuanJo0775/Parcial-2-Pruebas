import pytest
from recargaya.calculadora import calcular_recarga


class TestValidacionMonto:

    def test_monto_cero_es_rechazado(self):
        with pytest.raises(ValueError, match="Monto fuera del rango permitido"):
            calcular_recarga(monto=0)

    def test_monto_999_es_rechazado(self):
        with pytest.raises(ValueError, match="Monto fuera del rango permitido"):
            calcular_recarga(monto=999)

    def test_monto_50001_es_rechazado(self):
        with pytest.raises(ValueError, match="Monto fuera del rango permitido"):
            calcular_recarga(monto=50001)

    def test_monto_100000_es_rechazado(self):
        with pytest.raises(ValueError, match="Monto fuera del rango permitido"):
            calcular_recarga(monto=100000)