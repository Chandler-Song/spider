#coding:gbk
import numpy as np
import pandas as pd
import pymongo
from datetime import datetime
# from urllib.parse import urlencode
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import time
from itertools import product
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # ָ��Ĭ������
plt.rcParams['axes.unicode_minus'] = False  # �������ͼ���Ǹ���'-'��ʾΪ���������
from pprint import pprint
import csv
import requests
from collections import Counter
import jieba
# from wordcound import WordCloud
import os
import json
import csv
from pprint import pprint
import requests
import xlwt
import threading
# from functools import namedtuple
from concurrent import futures
import time

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36',
}

# ר����Ϣ API
url = 'https://zhuanlan.zhihu.com/api/columns/passer/posts?limit=100&'
req = requests.get(url, headers=headers).json()

result = []
headers = ('����', '������ҳ', '���±���', '���µ�ַ', '����ʱ��', '��ͬ��', '������')

for r in req:
    author = r['author']['name']                        # ����
    author_url = r['author']['profileUrl']              # ������ҳ
    title = r['title']                                  # ���±���
    url = 'https://zhuanlan.zhihu.com' + r['url']       # ���µ�ַ
    post_time = r['publishedTime']                      # ����ʱ��
    likes = r['likesCount']                             # ��ͬ��
    comments = r['commentsCount']                       # ������
    result.append((author, author_url, title, url, post_time, likes, comments))

pprint(result)


