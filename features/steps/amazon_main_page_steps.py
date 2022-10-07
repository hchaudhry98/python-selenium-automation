from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {product}')
def search_product(context, product):
    element = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    element.clear()
    element.send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Search results for {product_result} are shown')
def verify_search_results(context, product_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert product_result == actual_result, f'Error! Expected {product_result}, but got {actual_result}'
