import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


class TestApiHealth:

    def test_raiz_retorna_200(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_health_retorna_ok(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["estado"] == "ok"


class TestApiCalcular:

    def test_recarga_valida_sin_premium(self):
        response = client.post(
            "/recargas/calcular",
            json={"monto": 10000, "premium": False},
        )
        assert response.status_code == 200
        assert response.json()["bonificacion_porcentaje"] == 10

    def test_recarga_valida_con_premium(self):
        response = client.post(
            "/recargas/calcular",
            json={"monto": 30000, "premium": True},
        )
        assert response.status_code == 200
        assert response.json()["bonificacion_porcentaje"] == 30

    def test_recarga_monto_invalido_retorna_422(self):
        response = client.post(
            "/recargas/calcular",
            json={"monto": 500, "premium": False},
        )
        assert response.status_code == 422

    def test_recarga_monto_excede_maximo_retorna_422(self):
        response = client.post(
            "/recargas/calcular",
            json={"monto": 60000, "premium": False},
        )
        assert response.status_code == 422

    def test_respuesta_incluye_todos_los_campos(self):
        response = client.post(
            "/recargas/calcular",
            json={"monto": 10000, "premium": False},
        )
        data = response.json()
        assert "monto" in data
        assert "bonificacion_porcentaje" in data
        assert "datos_bonificados" in data
        assert "premium" in data