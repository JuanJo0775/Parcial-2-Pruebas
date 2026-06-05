# RecargaYa — Módulo de Cálculo de Recargas

**Autor:** Juan Jose Naranjo  
**Empresa:** RecargaYa S.A.S.  
**Lenguaje:** Python 3.12

Módulo para calcular el valor final de recargas de celular, desarrollado con TDD, BDD, API REST y pruebas de rendimiento con pipeline CI en GitHub Actions.

## Reglas de negocio

- El monto de recarga debe estar entre $1.000 y $50.000, de lo contrario se rechaza
- Recargas de $10.000 o más reciben un 10% de datos de bonificación
- Recargas de $30.000 o más reciben un 25% de datos de bonificación
- Usuarios con plan premium obtienen un 5% adicional sobre cualquier bonificación base
- El 5% premium solo aplica si existe una bonificación base mayor a cero

## Requisitos

- Python 3.12
- pip

## Instalación

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Ejecutar pruebas unitarias TDD

```bash
pytest tests/unit/ -v
```

## Ejecutar pruebas BDD

```bash
pytest tests/bdd/ -v
```

## Ejecutar todos los tests

```bash
pytest -v
```

## Levantar la API

```bash
uvicorn api.main:app --reload
```

La documentación interactiva queda disponible en `http://localhost:8000/docs`

## Ejecutar pruebas de rendimiento con Locust

Primero levanta la API en una terminal:

```bash
uvicorn api.main:app --reload
```

Luego en otra terminal, modo headless:

```bash
locust -f tests/performance/locustfile.py --headless -u 30 -r 5 --run-time 60s --host http://localhost:8000 --only-summary
```

O con interfaz web para ver métricas en tiempo real:

```bash
locust -f tests/performance/locustfile.py --host http://localhost:8000
```

Con la interfaz web abre `http://localhost:8089`, configura 30 usuarios y spawn rate 5.

## Estructura del proyecto

- `recargaya/` — módulo de lógica de negocio
- `api/` — API REST con FastAPI
- `tests/unit/` — tests unitarios TDD
- `tests/bdd/` — tests BDD con pytest-bdd y Gherkin
- `tests/performance/` — scripts de rendimiento con Locust
- `.github/workflows/` — pipeline CI con GitHub Actions

## Pipeline CI

El pipeline corre automáticamente en cada push a cualquier rama y en pull requests a main. Ejecuta en orden:

- Tests unitarios TDD
- Tests BDD con Gherkin
- Prueba de rendimiento Locust con verificación de P95 < 300ms

Ver `.github/workflows/ci.yml`