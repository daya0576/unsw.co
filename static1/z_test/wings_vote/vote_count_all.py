#!/usr/bin/python3.5

import re
import os
import urllib.request
from datetime import datetime, timezone, timedelta
import json
import time
from bs4 import BeautifulSoup

vote_url = 'http://survey.sports.sina.com.cn/result/115601.html'


def get_html(url):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('gb2312')
    # with open('origin_file.html') as f:
    #     html = f.read()
        soup = BeautifulSoup(html, 'html.parser')

        result = soup.find('div', id='JS_Content_01')
        result = result.find_all('dl', class_='item')

    return result


def get_final_data(html):
    shot = {}
    for item in html:
        m = re.search(r'<dt>(.+)</dt>', str(item))
        title = m.group(1)

        m = re.findall(r'<div class="options">(.+)</div>', str(item))
        options = m
        m = re.findall(r'<div class="data cf29">(.+)%</div>', str(item))
        data = m

        # print(title)
        # print(options)
        # print(data)

        vote_result = {}
        for i in range(len(options)):
            vote_result[options[i]] = '%.4f' % (float(data[i]) / 100)
        # print(vote_result)

        shot[title] = vote_result

    return shot


def get_bj_time():
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    bj_dt = bj_dt.strftime("%m-%d %H:%M")
    print(bj_dt)
    return bj_dt


if __name__ == '__main__':
    while True:
        html_result = get_html(vote_url)
        # print(html_result[0])
        final_result = get_final_data(html_result)
        print(final_result)

        bj_dt = get_bj_time()
        file_name = os.path.join('vote_trend_all', str(bj_dt))
        if not os.path.exists(file_name):
            with open(file_name, 'w') as f:
                json.dump(final_result, f)

        time.sleep(60 * 30)




