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

class TestBonificaciones:

    def test_monto_1000_no_tiene_bonificacion(self):
        resultado = calcular_recarga(monto=1000)
        assert resultado["bonificacion_porcentaje"] == 0

    def test_monto_5000_no_tiene_bonificacion(self):
        resultado = calcular_recarga(monto=5000)
        assert resultado["bonificacion_porcentaje"] == 0

    def test_monto_9999_no_tiene_bonificacion(self):
        resultado = calcular_recarga(monto=9999)
        assert resultado["bonificacion_porcentaje"] == 0

    def test_monto_10000_recibe_bono_10_porciento(self):
        resultado = calcular_recarga(monto=10000)
        assert resultado["bonificacion_porcentaje"] == 10

    def test_monto_20000_recibe_bono_10_porciento(self):
        resultado = calcular_recarga(monto=20000)
        assert resultado["bonificacion_porcentaje"] == 10

    def test_monto_29999_recibe_bono_10_porciento(self):
        resultado = calcular_recarga(monto=29999)
        assert resultado["bonificacion_porcentaje"] == 10

    def test_monto_30000_recibe_bono_25_porciento(self):
        resultado = calcular_recarga(monto=30000)
        assert resultado["bonificacion_porcentaje"] == 25

    def test_monto_40000_recibe_bono_25_porciento(self):
        resultado = calcular_recarga(monto=40000)
        assert resultado["bonificacion_porcentaje"] == 25

    def test_monto_50000_recibe_bono_25_porciento(self):
        resultado = calcular_recarga(monto=50000)
        assert resultado["bonificacion_porcentaje"] == 25            