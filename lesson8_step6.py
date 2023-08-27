from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    x = driver.find_element(By.CSS_SELECTOR, '#input_value.nowrap').text
    print(x)
    answer = calc(x)
    print(answer)
    
    driver.find_element(By.ID, 'answer').send_keys(answer)
    print('ANSWER')
    driver.find_element(By.ID, 'robotCheckbox').click()
    print('ROBOT CHECK')
    
    radio = driver.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    print('ROBOTS RADIO')
    button = driver.find_element(By.TAG_NAME, 'button')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click() 

    #driver.execute_script("document.title = 'CHANGED TITLE'; alert('HELLO');")


except:
    print('Error')

finally:
    sleep(5)
    driver.quit()