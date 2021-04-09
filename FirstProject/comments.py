#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import requests
import time
import random

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

start_url = "https://movie.douban.com/top250"

f_cookies = open('cookie.txt', 'r')
cookies = {}
# sign up more !******************************insert****************
# cookies = ['', '', '', '']
# ********************************************
# don't know if workable so far
proxies = ['183.47.2.201:30278', '118.122.92.252:37901', '163.204.244.141:9999', '58.254.220.116:52470',
           '114.119.116.92:61066', '113.108.242.36:47713', '42.123.125.181:8088', '116.7.176.29:8118']

for line in f_cookies.read().split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value


def get_html_text(url, data):
    try:
        pro = {'http': random.choice(proxies)}
        # cookie = {'cookie': random.choice(cookies)}
        r = requests.get(url, params=data, headers=header, cookies=cookies, proxies=pro)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        print(r.status_code)


def get_each_info(url):
    count = 0
    filename = ''
    url = url + 'comments'
    for i in range(0, 500, 20):
        time.sleep(6)
        print("Page:", 1+i/20)
        data = {
            "start": i,
            "limit": 20,
            "sort": "new_score",
            "status": "P"
        }
        html = get_html_text(url, data)
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find('title')
        movie = title.string
        if filename.strip() == '':
            filename = movie + '.txt'
        tag = soup.find_all('span', 'short')

        for t in tag:
            count = count + 1
            with open(filename, 'a') as f:
                f.write(str(count))
                f.write(":")
                if t.string:
                    f.write(t.string)
                else:
                    f.write("\n")
                    continue
                f.write("\n")


def get_urls():
    for i in range(175, 250, 25):
        # time.sleep(5)
        number = 0
        data = {
            "start": i,
            "filter": ""
        }
        h = get_html_text(start_url, data)
        s = BeautifulSoup(h, "html.parser")
        t = s.find_all('span', 'title')
        u = ""
        for j in t:
            time.sleep(5)
            if u.strip() == '' or u != j.parent['href']:
                number = number + 1
                u = j.parent['href']
                # if i == 25 and number < 17:
                # continue
                # if i == 50 and number < 6:
                # continue
                # if i == 75 and number < 11:
                # continue
                # else:
                print("page:", i, "\t", "Movie No.", number)
                get_each_info(u)


get_urls()
