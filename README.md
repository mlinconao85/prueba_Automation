Se utilizo Python con WebDriver.
1- Instalar las dependencias:
install -r requirements.txt
2- Ejecutar un script determinado con Allure
Por ejemplo:
behave -f allure_behave.formatter:AllureFormatter -o allure-results -t @loginNP2

3- Para generar el documento de reporte:
allure generate allure-results -o allure-report --clean

