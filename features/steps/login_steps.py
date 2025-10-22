from behave import given, when, then
import json
from features.pages.login_page import LoginPage

@given('Me encuentro el ambiente de "{ambiente}"')
def step_impl(context, ambiente):
    with open('utils/urls.json') as f:
        urls = json.load(f)
    url = urls.get(ambiente)
    if not url:
        raise ValueError("Ambiente '{ambiente}' no definido en urls.json")
    context.driver.get(url)
    context.login_page = LoginPage(context.driver)

@when('Ingreso al Login de usuario')
def step_impl(context):
        context.login_page.ingresar_al_login()

#esto sirve para que permita el ingreso de valores vacios
@when('Ingreso el email de "{username}"')
@when('Ingreso el email de ""')
def step_impl(context, username):
    context.login_page.ingresar_email(username)

#para ingresar solo la password correcta
#se guarda en una variable de entorno la cual se inyecta al contexto
#permite el ingreso de clave vacias
@when('Ingreso la "{secret}"')
@when('Ingreso la ""')
def step_impl(context, secret):
    context.login_page.ingresar_password(context.password)

@when('Selecciono Login')
def step_impl(context):
    context.login_page.click_login()

@then('Debo Visualizar el Dashboard para el usuario "{user_name}"')
def step_impl(context,user_name):
    assert context.login_page.dashboard_visible(user_name), "El dashboard no es visible"

@then('Debo Visualizar el "{mensaje_Error}"')
def step_impl(context,mensaje_Error):
    assert context.login_page.validar_error(mensaje_Error), "No se visualiza el mensaje de error"

@then('Debo mantenerme en el dashboard')
def step_impl(context):
    assert context.login_page.validar_si_estamos_en_login(), "OK"
