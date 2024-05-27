from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")

print(driver.title)

search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys('pycon')
search_box.send_keys(Keys.RETURN)

# Find elements with tag <li>
results = driver.find_elements(By.TAG_NAME, 'li')
print(len(results))