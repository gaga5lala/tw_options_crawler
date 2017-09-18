"""
practice for python crawler
"""

url = "http://www.taifex.com.tw/chinese/3/3_2_2.asp"
print("crawler for Taiwan options")

import requests
from bs4 import BeautifulSoup

import argparse
import datetime

parser = argparse.ArgumentParser(description='Crawl options data at assigned date')
# TODO: validate date
parser.add_argument('--date', type=int, nargs=1, required=True,
    help='assigned date (format: YYYYMMDD)')

args = parser.parse_args()
args_date = datetime.datetime.strptime(str(args.date[0]), "%Y%m%d")

payload = {
    # TODO: 確認參數細項
    "qtype": 3,
    # 交易時段：1.一般交易時段 2.盤後交易時段
    "market_code": 1,
    # TODO: 確認參數細項
    "dateaddcnt": -1,
    "syear": args_date.year,
    "smonth": args_date.month,
    "sday": args_date.day,
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
for row in rows[1:-2]:
    cols = row.find_all('td')
    print(cols[1].text + ", " + cols[2].text + ", " + cols[3].text + ", " + cols[7].text + ", " + cols[12].text)

# TODO: save data