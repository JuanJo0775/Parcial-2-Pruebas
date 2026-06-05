# Tabla de Casos de Prueba — Partición de Equivalencia y Valores Límite

## Campo analizado: monto de recarga

### Clases de equivalencia

- **Clase inválida inferior:** monto < 1.000
- **Clase válida estándar:** 1.000 ≤ monto < 10.000 (sin bonificación)
- **Clase válida con bono 10%:** 10.000 ≤ monto < 30.000
- **Clase válida con bono 25%:** 30.000 ≤ monto ≤ 50.000
- **Clase inválida superior:** monto > 50.000

### Casos de prueba

| ID | Monto | Plan Premium | Clase | Técnica | Resultado esperado |
|----|-------|-------------|-------|---------|-------------------|
| CP-01 | 0 | No | Inválida inferior | Valor límite | Rechazado |
| CP-02 | 999 | No | Inválida inferior | Valor límite | Rechazado |
| CP-03 | 1.000 | No | Válida estándar | Valor límite inferior | Bono 0% |
| CP-04 | 5.000 | No | Válida estándar | Partición equivalencia | Bono 0% |
| CP-05 | 9.999 | No | Válida estándar | Valor límite | Bono 0% |
| CP-06 | 10.000 | No | Válida bono 10% | Valor límite | Bono 10% |
| CP-07 | 20.000 | No | Válida bono 10% | Partición equivalencia | Bono 10% |
| CP-08 | 29.999 | No | Válida bono 10% | Valor límite | Bono 10% |
| CP-09 | 30.000 | No | Válida bono 25% | Valor límite | Bono 25% |
| CP-10 | 40.000 | No | Válida bono 25% | Partición equivalencia | Bono 25% |
| CP-11 | 50.000 | No | Válida bono 25% | Valor límite superior | Bono 25% |
| CP-12 | 50.001 | No | Inválida superior | Valor límite | Rechazado |
| CP-13 | 100.000 | No | Inválida superior | Partición equivalencia | Rechazado |
| CP-14 | 10.000 | Sí | Válida bono 10% | Premium | Bono 15% (10+5) |
| CP-15 | 30.000 | Sí | Válida bono 25% | Premium | Bono 30% (25+5) |
| CP-16 | 5.000 | Sí | Válida estándar | Premium sin bono base | Bono 0% (premium no suma si no hay bono) |