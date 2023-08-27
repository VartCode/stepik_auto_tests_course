from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

#link = 'http://suninjuly.github.io/selects1.html'
link = 'https://suninjuly.github.io/selects2.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    sleep(1)
    num1 = driver.find_element(By.ID, 'num1').text
    num2 = driver.find_element(By.ID, 'num2').text
    sum = int(num1) + int(num2)
    print(sum)

    select = Select(driver.find_element(By.CSS_SELECTOR, '.custom-select'))
    select.select_by_value(str(sum))

    driver.find_element(By.CSS_SELECTOR, 'button').click()
except:
    print('Error.')

finally:
    sleep(5)
    driver.quit()