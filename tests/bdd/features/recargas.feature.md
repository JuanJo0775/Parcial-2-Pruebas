
Característica: Cálculo de recargas de celular
  Como operador de RecargaYa S.A.S.
  Quiero calcular el valor final de una recarga
  Para aplicar bonificaciones correctamente según el monto y el plan del usuario

  Escenario: Monto por debajo del mínimo es rechazado
    Dado que el usuario intenta recargar 500 pesos
    Cuando se procesa la recarga
    Entonces el sistema rechaza la operación con error "Monto fuera del rango permitido"

  Escenario: Monto por encima del máximo es rechazado
    Dado que el usuario intenta recargar 60000 pesos
    Cuando se procesa la recarga
    Entonces el sistema rechaza la operación con error "Monto fuera del rango permitido"

  Escenario: Recarga estándar sin bonificación
    Dado que el usuario intenta recargar 5000 pesos
    Y el usuario no tiene plan premium
    Cuando se procesa la recarga
    Entonces la bonificación aplicada es 0 porciento

  Escenario: Recarga con bono del 25% para usuario premium
    Dado que el usuario intenta recargar 30000 pesos
    Y el usuario tiene plan premium
    Cuando se procesa la recarga
    Entonces la bonificación aplicada es 30 porciento

  Esquema del escenario: Bonificaciones según umbral de monto
    Dado que el usuario intenta recargar <monto> pesos
    Y el usuario no tiene plan premium
    Cuando se procesa la recarga
    Entonces la bonificación aplicada es <bonificacion> porciento

    Ejemplos:
      | monto | bonificacion |
      | 1000  | 0            |
      | 9999  | 0            |
      | 10000 | 10           |
      | 29999 | 10           |
      | 30000 | 25           |
      | 50000 | 25           |