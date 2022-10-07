from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Cart icon')
def open_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify that the Cart is empty')
def verify_cart_empty(context):
    expected_result = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Cart is empty')]").text
    actual_result = 'Your Amazon Cart is empty'
    assert expected_result==actual_result, f'Error: Expected {expected_result}, but got {actual_result}'