
import time
import sys
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging
from locustfile import RecargaYaUser, verificar_p95, UMBRAL_P95_MS

"""
Script que levanta Locust en modo headless, corre 60 segundos
con 30 usuarios y verifica que el P95 sea menor a 300ms.
"""

setup_logging("INFO")

USUARIOS = 30
SPAWN_RATE = 5
DURACION_SEGUNDOS = 60


def main():
    env = Environment(user_classes=[RecargaYaUser], events=None)
    env.create_local_runner()

    env.runner.start(USUARIOS, spawn_rate=SPAWN_RATE)
    print(f"Corriendo {USUARIOS} usuarios durante {DURACION_SEGUNDOS}s...")
    time.sleep(DURACION_SEGUNDOS)
    env.runner.stop()

    paso = verificar_p95(env)
    sys.exit(0 if paso else 1)


if __name__ == "__main__":
    main()