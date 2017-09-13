"""
practice for python crawler
"""

url = "http://www.taifex.com.tw/chinese/3/3_2_2.asp"
print("crawler for Taiwan options")

import requests
from bs4 import BeautifulSoup
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

# soup.find(class="table_c")
tables = soup.find_all("table")
optionTable = tables[2]

rows = optionTable.find_all('tr')

idx = 0
# skip first line
for row in rows[1:]:
    if idx > 10:
       break
    cols = row.find_all('td')
    print(cols[1].text + ", " + cols[2].text + ", " + cols[3].text + ", " + cols[7].text + ", " + cols[12].text)
    idx += 1