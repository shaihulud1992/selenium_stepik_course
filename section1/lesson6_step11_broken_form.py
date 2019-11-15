from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)
   
    first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")

    first_name.send_keys('Ivan')
    last_name.send_keys('Ivanov')
    email.send_keys('ivan@ivanov.ru')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)
