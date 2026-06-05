import json
from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer, stats_history
import locust.stats


UMBRAL_P95_MS = 300


class RecargaYaUser(HttpUser):
    wait_time = between(0.5, 1.5)
    host = "http://localhost:8000"

    @task(3)
    def calcular_recarga_estandar(self):
        self.client.post(
            "/recargas/calcular",
            json={"monto": 10000, "premium": False},
            name="POST /recargas/calcular - estandar",
        )

    @task(2)
    def calcular_recarga_premium(self):
        self.client.post(
            "/recargas/calcular",
            json={"monto": 30000, "premium": True},
            name="POST /recargas/calcular - premium",
        )

    @task(1)
    def calcular_recarga_minima(self):
        self.client.post(
            "/recargas/calcular",
            json={"monto": 1000, "premium": False},
            name="POST /recargas/calcular - minima",
        )

    @task(1)
    def health_check(self):
        self.client.get(
            "/health",
            name="GET /health",
        )


def verificar_p95(environment: Environment) -> bool:
    stats = environment.runner.stats.total
    p95_ms = stats.get_response_time_percentile(0.95)
    print(f"\nP95 obtenido: {p95_ms:.2f}ms — Umbral: {UMBRAL_P95_MS}ms")
    if p95_ms < UMBRAL_P95_MS:
        print(f"PASS — P95 {p95_ms:.2f}ms < {UMBRAL_P95_MS}ms")
        return True
    else:
        print(f"FAIL — P95 {p95_ms:.2f}ms >= {UMBRAL_P95_MS}ms")
        return False