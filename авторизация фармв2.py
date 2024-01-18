from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# from selenium.webdriver.support.ui import Select


class web_driver():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('C:/Users/bogdasarova/IdeaProjects/chromedriver.exe'))
        self.driver.maximize_window()
        self.driver.get("http://admin.dev.pharm.torgi223.ru/sign-in")


    def login_pharmv2(self):
        username = "admin"
        password = "upWnH=4qL`)!\}2"

        time.sleep(2)
        self.driver.find_element(By.NAME, "email").click()
        time.sleep(2)
        self.driver.find_element(By.NAME,"email").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > form > button > p").click()

        return "Выполнен вход"


if __name__ == "__main__":
    trigger = web_driver()
    login_is_done = trigger.login_pharmv2()
    print(login_is_done)

    # pagination1 = trigger.pagination()
    # print(pagination1)




