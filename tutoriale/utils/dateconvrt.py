#!/usr/bin/env python
# -*- coding: utf-8 -*
from re import search
import time as tm


def cdate(time):

    # 2017-9-1
    if search('\d{4}-\d{1,2}-\d{1,2}', time):
        return search('\d{4}-\d{1,2}-\d{1,2}', time).group()

    # 2017 September  1
    elif search('\d{4}\s[a-zA-Z]{4,}\s\d{1,2}', time):
        string = '%Y %B %d'
        time=search('\d{4}\s[a-zA-Z]{4,}\s\d{1,2}', time)
    # 2017 1 September
    elif search('\d{4}\s\d{1,2}\s[a-zA-Z]{4,}', time):
        string = '%Y %d %B'
        time=search('\d{4}\s\d{1,2}\s[a-zA-Z]{4,}', time)
    # 1 September 2017
    elif search('\d{1,2}\s[a-zA-Z]{4,}\s\d{4}', time):
        string = '%d %B %Y'
        time=search('\d{1,2}\s[a-zA-Z]{4,}\s\d{4}', time)
    # September 1 2017
    elif search('[a-zA-Z]{4,}\s\d{1,2}\s\d{4}', time):
        string = '%B %d %Y'
        time=search('[a-zA-Z]{4,}\s\d{1,2}\s\d{4}', time)
    # 2017 Sep 1
    elif search('\d{4}\s[a-zA-Z]{3}\s\d{1,2}', time):
        string = '%Y %b %d'
        time=search('\d{4}\s[a-zA-Z]{3}\s\d{1,2}', time)
    # 2017 1 Sep
    elif search('\d{4}\s\d{1,2}\s[a-zA-Z]{3}', time):
        string = '%Y %d %b'
        time=search('\d{4}\s\d{1,2}\s[a-zA-Z]{3}', time)
    # 1 Sep 2017
    elif search('\d{1,2}\s[a-zA-Z]{3}\s\d{4}', time):
        string = '%d %b %Y'
        time=search('\d{1,2}\s[a-zA-Z]{3}\s\d{4}', time)
    # Sep 1 2017
    elif search('[a-zA-Z]{3}\s\d{1,2}\s\d{4}', time):
        string = '%b %d %Y'
        time=search('[a-zA-Z]{3}\s\d{1,2}\s\d{4}', time)
    # September 2017
    elif search('[a-zA-Z]{4,}\s\d{4}', time):
        string = '%B %Y'
        time=search('[a-zA-Z]{4,}\s\d{4}', time)
    # 2017 September
    elif search('\d{4}\s[a-zA-Z]{4,}', time):
        string = '%Y %B'
        time=search('\d{4}\s[a-zA-Z]{4,}', time)
    # Sep 2017
    elif search('[a-zA-Z]{3}\s\d{4}', time):
        string = '%b %Y'
        time=search('[a-zA-Z]{3}\s\d{4}', time)
    # 2017 Sep
    elif search('\d{4}\s[a-zA-Z]{3}', time):
        string = '%Y %b'
        time=search('\d{4}\s[a-zA-Z]{3}', time)
    time=time.group()
    # 处理成'XXXX（年）-XX(月)-XX（日）'时间格式
    time = tm.strptime(time, string)
    time = tm.strftime("%Y-%m-%d", time)
    return time

