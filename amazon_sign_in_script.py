from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#open amazon website
driver.get('https://amazon.com/')

#locate and click 'Orders' link
driver.find_element(By.ID, 'nav-orders').click()

#Confirm that we see sign-in page
expected_result1 = 'Sign in'
actual_result1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result1 == actual_result1, f'Error: Expected {expected_result1}, but got {actual_result1}'

expected_result2 = True
actual_result2 = driver.find_element(By.ID, 'ap_email').is_displayed()
assert expected_result2 == actual_result2, f'Error: Expected to see email input box'


print("Test case passed")
#Quit driver
driver.quit()