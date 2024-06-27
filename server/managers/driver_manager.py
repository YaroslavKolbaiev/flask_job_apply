from selenium import webdriver


class DriverManager:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--verbose")
        chrome_options.add_argument("--log-path=chrome.log")
        self.driver = webdriver.Chrome(options=chrome_options)
