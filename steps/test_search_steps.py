from pytest_bdd import given, scenario, then, when
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.result_page import ResultPage
from utils.webdriver import driver_setup

# CONSTANTES
URL = "https://blogdoagi.com.br"

# DRIVER
def driver():
    driver = driver_setup()
    yield driver
    driver.quit()

# CENÁRIOS
@scenario('test_search.feature', 'Pesquisa de sentenca correta')
def test_pesquisa_de_sentenca_correta():
    """Pesquisa de sentenca correta."""

@scenario('test_search.feature', 'Pesquisa de sentenca incorreta')
def test_pesquisa_de_sentenca_incorreta():
    """Pesquisa de sentenca incorreta."""
###
    
@given('que acesso o blog')
def access_blog(driver):
    """que acesso o blog."""
    main_page = MainPage(driver)
    main_page.open_page(URL)
    return main_page

@when('clica no botão de pesquisa')
def click_search_button(driver):
    """clica no botão de pesquisa."""
    search_page = SearchPage(driver)
    search_page.search_button_click()

@when('preenchido o input com a sentença correta')
def fill_search_input_correct(driver):
    """preenchido o input com a sentença correta."""
    search_page = SearchPage(driver)
    termo_pesquisado = search_page.search_titulo()
    search_page.search_input_sentence(termo_pesquisado)

@when('pressionado a tecla ENTER')
def press_enter_key(driver):
    """pressionado a tecla ENTER."""
    search_page = SearchPage(driver)
    search_page.search_input_sentence_enter()

@then('devo visualizar os resultados pesquisa correta')
def verify_search_results_corret(driver):
    """devo visualizar os resultados pesquisa correta."""
    result_page = ResultPage(driver)
    texto_esperado = "Resultados encontrados para:"
    texto_encontrado = result_page.search_result_title()
    assert texto_esperado in texto_encontrado, f"O termo esperado é {texto_esperado} porém foi encontrado {texto_encontrado}"
    print(result_page.search_result_title())

@when('preenchido o input com a sentença incorreta')
def fill_search_input_incorrect(driver):
    """preenchido o input com a sentença incorreta."""
    search_page = SearchPage(driver)
    termo_pesquisado = "termo que não tem nada haver"
    search_page.search_input_sentence(termo_pesquisado)

@then('devo visualizar os resultados pesquisa incorreta')
def verify_search_results_incorret(driver):
    """devo visualizar os resultados pesquisa incorreta."""
    result_page = ResultPage(driver)
    texto_esperado = "Lamentamos, mas nada foi encontrado para sua pesquisa"
    if result_page.search_label_not_fount() is not False:
        texto_encontrado = result_page.search_label_not_fount()
    else:
        texto_encontrado = result_page.search_result_title()
     
    assert texto_esperado in texto_encontrado, f"O termo esperado é: \" {texto_esperado} \" porém foi encontrado: \" {texto_encontrado} \""
    print(result_page.search_result_title())

