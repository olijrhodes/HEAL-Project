import requests
from bs4 import BeautifulSoup
import requests
from pprint import pprint


url = 'https://www.england.nhs.uk/news/'
response = requests.get(url)


html = response.content
soup = BeautifulSoup(html, "html.parser")

results = soup.find_all("article", attrs={"class":"post group"})
for item in results:
    header = item.find_all("h2")
    print(header)