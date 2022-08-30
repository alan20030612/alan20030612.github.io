from bs4 import BeautifulSoup as bs
import requests
import urllib.parse
import datetime
import sqlite3
import lxml


def web_sc(page):
    url1 = 'https://www.ptt.cc/bbs/HardwareSale/index'
    url2 = '.html'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/103.0.0.0 Safari/537.36'
    }

    full_record = []
    for i in range(int(page)):
        url_main = url1 + url2
        r = requests.get(url_main, headers=header)
        source1 = bs(r.text, 'lxml')
        index = source1.select('div.action-bar div.btn-group-paging a')[1]['href']
        index1 = index[-9:-5]

        url = url1 + str(int(index1) - i) + url2

        rr = requests.get(url, headers=header)
        main_source = bs(rr.text, 'lxml')

        a = []
        b = []
        c = []
        d = []

        data1 = main_source.select('div.r-ent div.title')
        for j in range(len(data1)):
            try:
                title = data1[j].text.strip()
                a.append(title)
            except IndexError:
                a.append('')

        data2 = main_source.select('div.r-ent div.title a')
        for j in range(len(data2)):
            title_url = data2[j]['href']
            article_url = "https://www.ptt.cc/" + str(title_url)
            b.append(article_url)

        data3 = main_source.select('div.r-ent div.date')
        for j in range(len(data3)):
            date = data3[j].text.strip()
            c.append(date)

        data4 = main_source.select('div.r-ent div.author')
        for j in range(len(data4)):
            author = data4[j].text.strip()
            d.append(author)

        for k in range(len(b)):
            full_record.append(dict(header=a[k], author=d[k], date=c[k], url=b[k]))

    return full_record
