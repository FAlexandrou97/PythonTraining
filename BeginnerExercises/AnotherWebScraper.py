import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
soup = BeautifulSoup(requests.get(url).text, features='html.parser')
paragraphs = soup.findAll('p')
for paragraph in paragraphs:
    print(paragraph.getText())
