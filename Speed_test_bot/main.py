import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
PROMISED_UP = 20
PROMISED_DOWN = 25
CHROME_DRIVER_PATH = "C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe"

TWITTER_USERNAME = "apasatron_fh"
TWITTER_PASSWORD = ""
class InternetSpeed:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)


        self.up = 0
        self.down = 0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button = self.driver.find_element_by_class_name("js-start-test")
        button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_class_name("upload-speed")
        self.down = self.driver.find_element_by_class_name("download-speed")
        print(self.up.text)
        print(self.down.text)
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_USERNAME)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()
bot = InternetSpeed(CHROME_DRIVER_PATH)
bot.get_internet_speed()

bot.tweet_at_provider()
