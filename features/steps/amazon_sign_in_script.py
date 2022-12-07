from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Returns & Orders page')
def click_orders(context):
    element = context.driver.find_element(By.ID, 'nav-orders')
    element.click()


