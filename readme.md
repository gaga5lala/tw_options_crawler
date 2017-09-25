# Taiwan Options Exchange Crawler

爬取 [臺灣期貨交易所](http://www.taifex.com.tw/chinese/3/3_2_2.asp) 臺指選擇權資料的爬蟲。

## Setup

```
$ git clone https://gitlab.com/Backtest_Development/tw_options_crawler.git

$ cd tw_options_crawler

$ pip install -r requirements.txt
```

## Usage

### Command

爬指定日期

```
$ python option_crawler.py --date YYMMDD

e.g.

$ python option_crawler.py --date 20170919
```
