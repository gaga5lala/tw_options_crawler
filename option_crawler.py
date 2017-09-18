"""
practice for python crawler
"""

url = "http://www.taifex.com.tw/chinese/3/3_2_2.asp"
print("crawler for Taiwan options")

import requests
from bs4 import BeautifulSoup

# TODO: flexible change datetime

payload = {
    # TODO: 確認參數細項
    "qtype": 3,
    # 交易時段：1.一般交易時段 2.盤後交易時段
    "market_code": 1,
    # TODO: 確認參數細項
    "dateaddcnt": -1,
    "syear": 2017,
    "smonth": 9,
    "sday": 12,
    # 契約
    "commodity_idt": "TXO",
    }

req = requests.post(url, data=payload)
soup = BeautifulSoup(req.text, 'html.parser')

# soup.find(class="table_c")
tables = soup.find_all("table")
optionTable = tables[2]

rows = optionTable.find_all('tr')

# skip first line and last line
for row in rows[1:-1]:
    cols = row.find_all('td')
    print(cols[1].text + ", " + cols[2].text + ", " + cols[3].text + ", " + cols[7].text + ", " + cols[12].text)

# TODO: save data