from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
website_content = response.text
soup = BeautifulSoup(website_content, "html.parser")
print(soup.find(name="span", class_="titleline"))
first_anchor = soup.find('a')
first_anchor_text = first_anchor.text
anchor_tags = soup.find_all('a')
second_anchor_text = anchor_tags[1].text
















import lxml
# with open("website.html" ,encoding="utf8") as file:
#     data = file.read()
# soup = BeautifulSoup(data, 'html.parser')
# anchors = soup.find_all(name="a")
# # for a in anchors:
# #     print(a.get("href"))
# # print(soup.find(name="h3", class_= "heading"))
# url = soup.select_one(selector="p a")
# print(url)
