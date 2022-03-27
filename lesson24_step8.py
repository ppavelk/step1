from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xml.dom.minidom import Element
from selenium import webdriver
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    browser.implicitly_wait(5)

    WebDriverWait(browser, 100).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element_by_id('book').click()

    #message = browser.find_element_by_id("verify_message")

    #assert "successful" in message.text
   
   
   
   
    #first_window = browser.window_handles[0]
    #browser.find_element_by_tag_name('button').click()
    
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    
    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_id('solve').click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

