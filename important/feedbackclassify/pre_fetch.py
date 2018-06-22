#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
练习python urllib相关
'''
import requests


def requst_feedback_data():
    '''
    获取反馈信息
    '''
    r = requests.get(
        "http://ffilelogweb.huya.com/ajax/queryList?appId=200&page=1&pageSize=10000&isNotAutoFeedback=1")
    # print "response code:%s,json:%s" % (r.status_code, r.text[0:100])
    return r.text.encode('utf-8')
