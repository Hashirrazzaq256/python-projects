import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
CHROME_DRIVER_PATH = "C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe"
INSTAGRAM_USERNAME = "_star_specie"
INSTAGRAM_PASSWORD = "python1421"
SIMILAR_ACCOUNT = "carsport_63"

class InstaFollowers:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(INSTAGRAM_USERNAME)
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/following/")
        time.sleep(2)
        div = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div)
            time.sleep(2)
    def follow(self):
        def follow(self):
            all_buttons = self.driver.find_elements_by_css_selector("li button")
            for button in all_buttons:
                try:
                    button.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()



insta = InstaFollowers(CHROME_DRIVER_PATH)
insta.login()
insta.find_followers()
insta.follow()

