Feature: Login


  @loginHP1 @uat
  Scenario Outline: Ingreso exitoso al sistema
    Given Me encuentro el ambiente de "pruebas"
    When Ingreso al Login de usuario
    And Ingreso el email de "<username>"
    And Ingreso la "<password>"
    And Selecciono Login
    Then Debo Visualizar el Dashboard para el usuario "<user_name>"

    Examples:
      | username                 | password |user_name|
      | moi.linconao@gmail.com   | secret   |moises|


      @loginNP1 @uat
  Scenario Outline: Probamos los casos donde usuario y pass sean incorrectos
    Given Me encuentro el ambiente de "pruebas"
    When Ingreso al Login de usuario
    And Ingreso el email de "<username>"
    And Ingreso la "PasswordErronea"
    And Selecciono Login
    Then Debo Visualizar el "<mensaje_Error>"

    Examples:
      | username                  |mensaje_Error                       |
      | mmm@gmail.com             |Your email or password is incorrect!|
      | moi.linconao@gmail.com    |Your email or password is incorrect!|

  @loginNP2 @uat
    Scenario: Validamos que no permita ingresar con los campos vacios
    Given Me encuentro el ambiente de "pruebas"
    When Ingreso al Login de usuario
    And Ingreso el email de " "
    And Ingreso la " "
    And Selecciono Login
    Then Debo mantenerme en el dashboard



