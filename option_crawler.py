"""
practice for python crawler
"""

url = "http://www.taifex.com.tw/chinese/3/3_2_2.asp"
print("crawler for Taiwan options")

import requests
from bs4 import BeautifulSoup

# TODO: flexible change datetime

# FIXME: payload incorrect
payload = {
    "qtype": 3,
    "commodity_id": "TXOa",
    # commodity_id2
    "market_code": 1,
    # goday
    "dateaddcnt": -1,
    "DATA_DATE_Y": 2017,
    "DATA_DATE_M": 9,
    "DATA_DATE_D": 13,
    "syear": 2017,
    "smonth": 9,
    "sday": 13,
    "datestart": "2017/9/13",
    "MarketCode": 1,
    "commodity_idt": "TXO",
    # commodity_id2t
    # commodity_id2t2
    }

req = requests.post(url, data=payload)
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

# TODO: save data