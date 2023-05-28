from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
PROMISED_UP = 20
PROMISED_DOWN = 25
CHROME_DRIVER_PATH = "C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe"

TWITTER_USERNAME = "apasatron_fh"
TWITTER_PASSWORD = "quantum1421_"
class InternetSpeed:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)


        self.up = 0
        self.down = 0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button = self.driver.find_element_by_class_name("js-start-test")
        button.click()
    def tweet_at_provider(self):
        pass
bot = InternetSpeed(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
