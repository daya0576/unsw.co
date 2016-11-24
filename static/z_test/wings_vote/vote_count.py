#!/usr/bin/python3.5

import re
import urllib.request
from datetime import datetime
import json
import time

vote_url = 'http://survey.sports.sina.com.cn/result/115601.html'


def get_html(url):
    with urllib.request.urlopen(url) as f:
        html_result = ''
        for line in f:
            line = line.decode('gb2312')
            if 'displayValue=\'WINGS战队' in line:
                html_result += line
    return html_result


def get_vote_shot(html_result):
    vote_list = re.findall(r"displayValue='(.+?)'", html_result)
    now = datetime.now().strftime("%m-%d %H:%M")

    final_result = {"time": str(now)}
    vote_result = {}

    for item in vote_list:
        m = re.match(r"(.+)\((.+)%\)", item)

        n = m.group(1)
        c = '%.4f' % (float(m.group(2)) / 100)

        vote_result[n] = c

    final_result['vote_result'] = vote_result

    return final_result


if __name__ == '__main__':
    # html_result = get_html(vote_url)
    # with open('vote_trend.json', 'w') as f:
    #     json.dump([get_vote_shot(html_result)], f)
    # exit()

    while 1:
        # time.sleep(60 * 30)
        html_result = get_html(vote_url)
        # html_result = "myChart_bing_8.setDataXML(<chart baseFontSize='12' numberSuffix='%' showAboutMenuItem='0' decimals='2' chartTopMargin='0' chartBottomMargin='0' caption='' showValues='0' formatNumberScale='0' bgAlpha='0' startingAngle='60'><set label='1' value='59.6' displayValue='WINGS战队（电竞） (59.6%)' toolText=' (59.6%)' isSliced='1' /><set label='2' value='24.5' displayValue='邹市明（拳击） (24.5%)' toolText=' (24.5%)'/><set label='3' value='7.6' displayValue='丁俊晖（台球） (7.6%)' toolText=' (7.6%)'/><set label='4' value='5.7' displayValue='柯洁（围棋） (5.7%)' toolText=' (5.7%)'/><set label='5' value='2.6' displayValue='张弛（轮滑） (2.6%)' toolText=' (2.6%)'/></chart>"

        with open('vote_trend.json') as f:
            final_result = json.load(f)
        final_result.append(get_vote_shot(html_result))

        with open('vote_trend.json', 'w') as f:
            json.dump(final_result, f)

        print(len(final_result))







