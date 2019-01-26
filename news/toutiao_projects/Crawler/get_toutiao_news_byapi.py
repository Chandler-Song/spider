# -*- coding: utf-8 -*-
"""
Created on 2019-01-26 13:47
@author: Johnson
Email:593956670@qq.com
@software: PyCharm
"""
import requests
import random
import json
from Utils.keyword import keyword
from Utils.Util import insert_data,insert_data_apinews



class News:

    def __init__(self):
        self.id = ""
        self.title = ""
        self.tag = ""
        self.chinese_tag = ""
        self.source = ""
        self.source_url = ""
        self.content = ""
        #两会关键词
        self.keyword = ""
        #今日头条自带关键词
        self.keywords = ""


def toutiao_news_api(url):
    toutiao_data = requests.get(url).text
    data = json.loads(toutiao_data)
    global max_behot_time
    max_behot_time = data["next"]['max_behot_time']
    items = data['data']

    news_list = []
    link_head = 'http://toutiao.com'

    for n in items:
        if 'title' in n and n['tag'] != 'ad':
            news = News()
            news.title = n['title']
            print(news.title)
            news.tag = n['tag']
            news.source = n['source']
            news.source_url = link_head + n['source_url']

            news_list.append(news)
            #print(news.title, news.source_url, news.source, news.keyword, news.keywords)

    return news_list

global max_behot_time
max_behot_time = 0
while(1):
    print(max_behot_time)
    url = 'http://www.toutiao.com/api/pc/feed/?category=__all__&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B5D9F152FBC03&cp=59123B3CE0B3FE1'
    news_list = toutiao_news_api(url)
    #print(len(news_list))
    #insert_data_apinews(news_list)

