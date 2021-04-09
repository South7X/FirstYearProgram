#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import re


class Maoyan():
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 '
                      '(KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
        'Host': 'm.maoyan.com'
    }

    def __init__(self, url, time, count):
        self.url = url
        self.time = time
        self.count = count

    def get_html(self):
        r = requests.get(self.url, headers=self.header)
        j = json.loads(r.text)
        return j

    def get_data(self, j):  # 引用函数时的参数一定要与此处的参数 j 类型相同，不然怎么在原函数改动都没用的（血的教训：
                            # 改bug不要一直盯着error line看）
        s = j["cmts"]
        for data in s:
            self.count = self.count + 1
            star = data['score']
            comment = data['content']
            self.write_file(comment, star)
        return self.count

    def write_file(self, comment, star):
        filename = '上海堡垒' + '.txt'
        with open(filename, 'a') as f:
            f.write(str(star))
            f.write(":")
            f.write(comment)
            f.write("\n")


# get the movies' names
# def soup_start_urls():
#    number = 0
#    for i in range(0, 100, 10):
#        data = {
#            "offset": i
#        }
#        html = get_html(start_url, data)
#        soup = BeautifulSoup(html, "html.parser")
#        tags = soup.find_all('data-act', 'boarditem-click')
#        u = ''
#        for t in tags:
#            if u.strip() == '' or u != t['href']:
#                number = number + 1
#                u = t['href']
#                filename = t['title']
#                movie_id = re.match(r'[0-9]+', u)
#                print("page:", i/10+1, "\t", "Movie No.", number)
#                get_comments(movie_id, filename)


def get_comments():
    offset = 0
    tim = '2019-08-09'
    day = range(9, 32)
    number = 0
    count = 0
    page_num = int(21000 / 15)
    for i in range(page_num):
        url = 'http://m.maoyan.com/mmdb/comments/movie/342903.json?' \
              '_v_=yes&offset={0}&startTime={1}%2023%3A59%3A59'.format(offset, tim)
        s = Maoyan(url, tim, count)
        comment = s.get_html()
        if comment["total"] == 0 or comment["cmts"] is None:
            tim = '2019-08-%d' % day[number]    # 修改爬下一天时，记得改完所有的相关参数
            offset = 0
            number = number + 1
            continue
        count = s.get_data(comment)     # 不能用全局变量解决全部评论计数问题，给函数加了个返回值传递count
        print(count)
        offset = offset + 15


# separate each sentence and delete the punctuation
def separate():
    filename = ['烈火英雄', '蜘蛛侠：英雄远征', '银河补习班', '千与千寻', '哪吒之魔童降世', '速度与激情：特别行动']
    # filename = ['上海堡垒']
    # r = '(\d)|(\d\.\d)'
    # r2 = '(^\d:)|(^\d\.\d:)'
    r2 = '^[A-Z]'
    record = ''
    # pattern = re.compile(r)
    # rr = '(！+|!+|\.+|。+|,+|，+|？+|\?+|\(+|\)+|（+|）+|,+|\s)'
    for name in filename:
        f = open(name+'.tsv', "r")
        # new_name = name + '去标点.txt'
        # ff = open(new_name, "a")
        # final_name = name + '分句.txt'
        new_name = name + '_单行.tsv'
        for line in f.readlines():
            pattern = re.compile(r2)
            m = pattern.match(line)
            ff = open(new_name, 'a')
            if m is not None:
                w = re.sub('\n', '|', record)
                w2 = re.sub('\|$', '\n', w)
                ff.write(w2)
                # change = re.sub(r2, '', line)
                record = line
            else:
                record += line

            """"
            m = pattern.match(line)
            if m is not None:
                x = int(2*float(m.group()))
                ff = open(new_name, 'a')
                if x <= 4:
                    write = re.sub(r2, 'L\t', line)
                elif x <= 7:
                    write = re.sub(r2, 'M\t', line)
                else:
                    write = re.sub(r2, 'H\t', line)
                ff.write(write)
            
            # process_1 = re.sub(r2, '', line)     # 去序号
            # process_2 = re.sub(rr, '\n', process_1)     # 去标点
            # ff.write(process_2)
        
        # 去多余的空行
        f1 = open(new_name, "r")
        for line in f1.readlines():
            f2 = open(final_name, 'a')
            if line == '\n':
                line = line.strip("\n")
            f2.write(line)
        """


if __name__ == '__main__':
    # get_comments()
    separate()

