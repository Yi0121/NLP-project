import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://hk.finance.yahoo.com/quote/9992.HK/history/?period1=1609459200&period2=1750838777'
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page.Status code:{response.status_code}")
    exit()
soup = BeautifulSoup(html_content,'lxml')
data = soup.find_all("div",class_ = "table-container yf-1jecxey")

for tilte in data :
    


