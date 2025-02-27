from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


CART = (By.ID, "nav-cart-count")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")
LINKS = (By.CSS_SELECTOR, "div[class*='nav-tab-all_style'] a")
HAM_MENU = (By.ID, "nav-hamburger-menu")
FOOTER_LINKS = (By.CSS_SELECTOR, ".navFooterDescItem a")
SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {product}')
def search_product(context, product):
    element = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    element.clear()
    element.send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click on button from SignIn popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')
    e.click()


@when('Wait for {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In disappears')
def verify_sign_in_btn_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN), message='Sign in is still visible')


@then('Search results for {product_result} are shown')
def verify_search_results(context, product_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert product_result == actual_result, f'Error! Expected {product_result}, but got {actual_result}'


@when('Click on first product')
def click_first_product(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_PRICE), message='Product not clickable')
    e.click()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART).text
    assert expected_count == actual_count, f'Expected {expected_count}, but instead got {actual_count}'


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    menu = context.driver.find_elements(*HAM_MENU)
    print(menu)


@then('Verify that footer has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)
    links = context.driver.find_elements(*FOOTER_LINKS)
    print('\nLinks\n', links)
    numLinks = len(links)
    assert numLinks == expected_link_count, f'Expected {expected_link_count} links, but got {numLinks}'


@given('Open bestsellers page')
def open_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are 5 links')
def verify_links(context):
    links = context.driver.find_elements(*LINKS)
    assert len(links) == 5, 'Expected 5 links'


@then('Verify Sign In is clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')
