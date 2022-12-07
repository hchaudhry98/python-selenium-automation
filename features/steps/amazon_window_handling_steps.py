from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")
PRIVACY_TITLE = (By.XPATH, "//h1[contains(text(), 'Privacy Notice')]")


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref'
                       '=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_og_window(context):
    context.og_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_to_newly_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    context.driver.switch_to.window(current_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.presence_of_element_located(PRIVACY_TITLE))


@then('User can close new window and switch back to original')
def close_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.og_window)