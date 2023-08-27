from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    driver = webdriver.Chrome()
    driver.get(link)

    driver.find_element(By.CSS_SELECTOR, '.btn').click()
    print('FIRST BUTTON CLICK OK')

    confirm = driver.switch_to.alert
    confirm.accept()
    print('ALERT ACCEPT OK')

    x = driver.find_element(By.ID, 'input_value').text
    print('GET X OK')

    driver.find_element(By.ID, 'answer').send_keys(calc(x))
    print('INPUT ANSWER OK')

    driver.find_element(By.CSS_SELECTOR, '.btn').click()
    print('SEND ANSWER OK')


except:
    print('ERROR')

finally:
    sleep(5)
    driver.quit()