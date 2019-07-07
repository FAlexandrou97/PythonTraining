import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features='html.parser')
''' Alternative method, reduce code
soup = BeautifulSoup.BeautifulSoup(requests.get(url).text)
'''
titles = soup.findAll('h2')
for title in titles:
    print("Title: ", title.getText())
