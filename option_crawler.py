# -- coding: utf-8 --

"""
practice for python crawler
"""

import requests
from bs4 import BeautifulSoup

import argparse
import datetime

import pandas as pd

import os
from os import mkdir
from os.path import isdir

class OptionCrawler():
    def __init__(self, date, url="http://www.taifex.com.tw/chinese/3/3_2_2.asp", data_dir="data"):
        self.date = self._parse_date(date)
        self.url = url
        self.data_dir = data_dir
        self.data = None

    # convert string to datetime object
    def _parse_date(self, date):
        return datetime.datetime.strptime(date, "%Y%m%d")

    def start(self):
        self._get_data()

    def _get_data(self):
        payload = {
            # TODO: 確認參數細項
            "qtype": 2,
            # 交易時段：1.一般交易時段 2.盤後交易時段
            "market_code": 0,
            # TODO: 確認參數細項
            # "dateaddcnt": -1,
            "syear": self.date.year,
            "smonth": self.date.month,
            "sday": self.date.day,
            # 契約
            "commodity_idt": "TXO",
        }
        print(payload)

        req = requests.post(self.url, data=payload)
        req.encoding="utf-8"

        soup = BeautifulSoup(req.text, 'html.parser')

        # soup.find(class="table_c")
        tables = soup.find_all("table")
        optionTable = tables[2]

        # skip last 2 line
        df = pd.read_html(str(optionTable),header=0)[0].iloc[:-2]

        # select specific columns
        df = (df[df.columns[[1, 2, 3, 7, 8, 12]]])
        self.data = df

    def _get_dir_path(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        data_dir_path = script_path + "/" + self.data_dir
        if not isdir(data_dir_path):
            mkdir(data_dir_path)
        return data_dir_path

    def save(self):
        dir_path = self._get_dir_path()
        # file_name = dir_path + '/' + f'{self.date.strftime("%Y%m%d")}.csv'
        file_name = dir_path + '/' + '{dt}.csv'.format(dt=self.date.strftime('%Y%m%d'))
        self.data.to_csv(file_name, index=False, sep=',', encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description='Crawl options data at assigned date')
    # TODO: validate date
    parser.add_argument('--date', type=int, nargs=1, required=True,
        help='assigned date (format: YYYYMMDD)')

    args = parser.parse_args()

    crawler = OptionCrawler(str(args.date[0]))
    crawler.start()
    crawler.save()

if __name__ == '__main__':
    print("crawler for Taiwan options")
    main()
