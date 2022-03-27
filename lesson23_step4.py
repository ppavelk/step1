from xml.dom.minidom import Element
from selenium import webdriver
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    first_window = browser.window_handles[0]
    browser.find_element_by_tag_name('button').click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    
    browser.find_element_by_id('answer').send_keys(y)

    button = browser.find_element_by_tag_name('button').click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

