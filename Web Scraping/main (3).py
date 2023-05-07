from bs4 import BeautifulSoup
import openai
import lxml
with open("website.html" ,encoding="utf8") as file:
    data = file.read()
soup = BeautifulSoup(data, 'html.parser')
print(soup.title)
