#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

start_url = "https://movie.douban.com/top250"


def get_html_text(url, data):
    try:
        # pro = {'http': random.choice(proxies)}
        # cookie = {'cookie': random.choice(cookies)}
        r = requests.get(url, params=data, headers=header)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        print(r.status_code)


def get_urls():
    filename = 'Name.txt'
    for i in range(0, 275, 25):
        # time.sleep(5)
        number = 0
        data = {
            "start": i,
            "filter": ""
        }
        h = get_html_text(start_url, data)
        s = BeautifulSoup(h, "html.parser")
        t = s.find_all('span', 'title')
        name = ""
        for j in t:
            if name.strip() == '' or name != j.string:
                number = number + 1
                name = j.string
                if name.strip()[0] == "/":
                    continue
                with open(filename, 'a') as f:
                    f.write(name)
                    f.write("\n")
                print("page:", i, "\t", "Movie No.", number)
                # get_each_info(u)


get_urls()
