# RecargaYa — Módulo de Cálculo de Recargas

**Autor:** Juan Jose Naranjo  
**Empresa:** RecargaYa S.A.S.  
**Lenguaje:** Python 3.12  

Módulo para calcular el valor final de recargas de celular, desarrollado con TDD, BDD, API REST y pruebas de rendimiento.

## Reglas de negocio

- El monto de recarga debe estar entre $1.000 y $50.000
- Recargas de $10.000 o más reciben un 10% de datos de bonificación
- Recargas de $30.000 o más reciben un 25% de datos de bonificación
- Usuarios con plan premium obtienen un 5% adicional sobre cualquier bonificación

## Requisitos

- Python 3.12
- pip

## Instalación

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Ejecutar pruebas unitarias (TDD)

```bash
pytest tests/unit/ -v
```

## Ejecutar pruebas BDD

```bash
pytest tests/bdd/ -v
```

## Ejecutar la API

```bash
uvicorn api.main:app --reload
```

## Ejecutar pruebas de rendimiento (Locust)

```bash
locust -f tests/performance/locustfile.py --headless -u 30 -r 5 --run-time 60s --host http://localhost:8000
```
```bash
locust -f tests/performance/locustfile.py --host http://localhost:8000
```

## Pipeline CI

El pipeline corre automáticamente en cada push a cualquier rama. Ver `.github/workflows/ci.yml`.


