from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select


class web_driver():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('C:/Users/bogdasarova/IdeaProjects/chromedriver.exe'))
        self.driver.maximize_window()
        self.driver.get("http://admin.dev.pharm.torgi223.ru/sign-in")


    def login_adminka(self):
        username = "admin"
        password = "upWnH=4qL`)!\}2"

        time.sleep(2)
        self.driver.find_element(By.NAME, "email").click()

        self.driver.find_element(By.NAME,"email").send_keys(username)

        self.driver.find_element(By.NAME, "password").send_keys(password)

        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/button/p").click()
        time.sleep(3)

        if self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/h2"):
            print("Мы попали в админ панель")
        else:
            self.driver.find_element(By.XPATH,"/html/body/div/div/div/h1")
            print('Авторизация не удалась')


if __name__ == "__main__":
    trigger = web_driver()
    login_is_done = trigger.login_adminka()
    print(login_is_done)







