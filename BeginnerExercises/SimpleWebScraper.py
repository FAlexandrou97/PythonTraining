import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features='html.parser')
titles = soup.findAll('h2')
for title in titles:
    print("Title: ", title.getText())
