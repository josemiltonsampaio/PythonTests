import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt0068646/fullcredits"

r = requests.get(url)

print(r.text)
