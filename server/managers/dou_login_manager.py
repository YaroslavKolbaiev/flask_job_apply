import os

# from dotenv import load_dotenv
from time import sleep
from selenium.webdriver.common.by import By

# load_dotenv()

account_email = os.environ.get("DOU_ACCOUNT_EMAIL")
account_password = os.environ.get("DOU_ACCOUNT_PASSWORD")


class DouLoginManager:
    def __init__(self, driver):
        self.driver = driver
        self.account_email = os.environ.get("DOU_ACCOUNT_EMAIL")
        self.account_password = os.environ.get("DOU_ACCOUNT_PASSWORD")

    def login(self):
        self.driver.get("https://dou.ua")

        sleep(3)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-link"]')
        login_button.click()

        sleep(1)

        login_with_email_btn = self.driver.find_element(
            By.XPATH, '//*[@id="_loginByMail"]'
        )
        login_with_email_btn.click()

        sleep(1)

        email_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="_loginDialog"]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/input',
        )
        email_input.send_keys(account_email)

        sleep(1)

        password_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="_loginDialog"]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div[2]/div[1]/input',
        )

        password_input.send_keys(account_password)

        sleep(1)

        submit_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="_loginDialog"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/button',
        )
        submit_button.click()

        sleep(4)
