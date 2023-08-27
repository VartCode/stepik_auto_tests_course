from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    sleep(1)
    
    driver.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Ivan')
    driver.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Ivanov')
    driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('mail@mail.ru')
    print('DATA OK')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print('JOIN PATH OK')
    
    load_file = driver.find_element(By.ID, 'file')
    load_file.send_keys(file_path)
    print('LOAD FILE OK')

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    print('BUTTON CLICK OK')
    
except:
    print('ERROR')

finally:
    sleep(10)
    driver.quit()