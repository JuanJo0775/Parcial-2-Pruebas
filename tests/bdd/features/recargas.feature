Feature: Calculo de recargas de celular
  Como operador de RecargaYa S.A.S.
  Quiero calcular el valor final de una recarga
  Para aplicar bonificaciones correctamente segun el monto y el plan del usuario

  Scenario: Monto por debajo del minimo es rechazado
    Given que el usuario intenta recargar 500 pesos
    When se procesa la recarga
    Then el sistema rechaza la operacion con error "Monto fuera del rango permitido"

  Scenario: Monto por encima del maximo es rechazado
    Given que el usuario intenta recargar 60000 pesos
    When se procesa la recarga
    Then el sistema rechaza la operacion con error "Monto fuera del rango permitido"

  Scenario: Recarga estandar sin bonificacion
    Given que el usuario intenta recargar 5000 pesos
    And el usuario no tiene plan premium
    When se procesa la recarga
    Then la bonificacion aplicada es 0 porciento

  Scenario: Recarga con bono del 25 por ciento para usuario premium
    Given que el usuario intenta recargar 30000 pesos
    And el usuario tiene plan premium
    When se procesa la recarga
    Then la bonificacion aplicada es 30 porciento

  Scenario Outline: Bonificaciones segun umbral de monto
    Given que el usuario intenta recargar <monto> pesos
    And el usuario no tiene plan premium
    When se procesa la recarga
    Then la bonificacion aplicada es <bonificacion> porciento

    Examples:
      | monto | bonificacion |
      | 1000  | 0            |
      | 9999  | 0            |
      | 10000 | 10           |
      | 29999 | 10           |
      | 30000 | 25           |
      | 50000 | 25           |