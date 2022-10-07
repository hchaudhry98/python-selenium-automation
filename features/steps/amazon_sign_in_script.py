from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Returns & Orders page')
def click_orders(context):
    element = context.driver.find_element(By.ID, 'nav-orders')
    element.click()


@then('Verify Sign In page opened')
def verify_sign_in_page(context):
    expected_result1 = 'Sign in'
    actual_result1 = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result1 == actual_result1, f'Error: Expected {expected_result1}, but got {actual_result1}'
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Error: Expected to see email input box'

