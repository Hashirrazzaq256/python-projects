from bs4 import BeautifulSoup
import requests
from selenium import webdriver

import time
import lxml
header = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.89",
    "Accept-Encoding": "gzip, deflate, br",
}
response = requests.get(
    "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.84716973355808%2C%22east%22%3A-122.22184268359375%2C%22south%22%3A37.70334422496088%2C%22west%22%3A-122.64481631640625%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D",headers=header)
data = response.text
soup = BeautifulSoup(data,"lxml")

lists = soup.find_all(name="li", class_ = "ListItem-c11n-8-84-0__sc-10e22w8-0")


prices = soup.find_all(name="span", class_ = "PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
all_prices = [price.get_text().split("+")[0] for price in prices if "$" in price.text]


addresses = soup.find_all(name="address")
all_addresses = [address.get_text().split(" | ")[-1] for address in addresses]
all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)


CHROME_DRIVER_PATH = "C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
for n in range(len(all_links)):

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfggCzsmFPCVLN7xeCI_vBOWUFCMcKOXh_rclsskqQ72mm6ug/viewform?usp=sf_link")
    time.sleep(2)
    adress = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')


    adress.send_keys(all_addresses[n])
    rent.send_keys(all_prices[n])
    url.send_keys(all_links[n])
    submit.click()
