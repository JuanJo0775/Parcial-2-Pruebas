import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers
from recargaya.calculadora import calcular_recarga

FEATURES_DIR = Path(__file__).parent / "features"
scenarios(str(FEATURES_DIR / "recargas.feature"))


# ── Contexto compartido ──────────────────────────────────────────────────────

@pytest.fixture
def contexto():
    return {}


# ── Givens ───────────────────────────────────────────────────────────────────

@given(parsers.parse("que el usuario intenta recargar {monto:d} pesos"), target_fixture="contexto")
def dado_monto(monto):
    return {"monto": monto, "premium": False}


@given(parsers.parse("el usuario tiene plan premium"))
def dado_premium(contexto):
    contexto["premium"] = True


@given(parsers.parse("el usuario no tiene plan premium"))
def dado_no_premium(contexto):
    contexto["premium"] = False


# ── When ─────────────────────────────────────────────────────────────────────

@when("se procesa la recarga")
def cuando_procesa(contexto):
    try:
        resultado = calcular_recarga(
            monto=contexto["monto"],
            premium=contexto.get("premium", False),
        )
        contexto["resultado"] = resultado
        contexto["error"] = None
    except ValueError as e:
        contexto["resultado"] = None
        contexto["error"] = str(e)


# ── Thens ────────────────────────────────────────────────────────────────────

@then(parsers.parse('el sistema rechaza la operacion con error "{mensaje}"'))
def entonces_error(contexto, mensaje):
    assert contexto["error"] == mensaje


@then(parsers.parse("la bonificacion aplicada es {bonificacion:d} porciento"))
def entonces_bonificacion(contexto, bonificacion):
    assert contexto["error"] is None
    assert contexto["resultado"]["bonificacion_porcentaje"] == bonificacion