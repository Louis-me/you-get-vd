#!/usr/bin/env python
# -*- coding=utf-8 -*-
import fake_useragent
import requests

__author__ = 'shikun'
__CreateAt__ = '2020/2/13-10:19'
import os
import time
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent #pip3 install fake-useragent
from bs4 import BeautifulSoup as bs

def download_pool(play_list):
    """
    线程池下载视频
    :param play_list: 下载视频列表
    :return:
    """
    start_time = time.time()
    # with ThreadPoolExecutor(len(play_list)) as pool:
    with ThreadPoolExecutor(50) as pool:
        result = pool.map(download, play_list)

    for i in result:
        pass
    end_time = time.time()
    print("sum time:%.2f second" % (end_time-start_time))

def get_header():
    location = 'fake_useragent.json'
    ua = fake_useragent.UserAgent(path=location)
    return ua.random


def get_play_list():
    data = []
    for i in range(1, 9):
        url = "https://www.lizhi.fm/user/3553776/p/%s.html" % i
        print(url)
        res = requests.get(url, verify=False, headers={'User-Agent': get_header(),
                                         'Host': 'www.lizhi.fm'}).content.decode('gb2312', errors='ignore')
        soup = bs(res, 'lxml')
        if i == 1:
            css = "body > div.wrap > div.frame > div:nth-child(6)>ul>li>a"
        else:
            css = 'body > div.wrap > div.frame > div:nth-child(4)>ul>li>a'
        a_href_obj = soup.select(css)
        for a_href in a_href_obj:
            data.append("https://www.lizhi.fm/" + a_href.get('href'))
    return data



def download(url):
    """
    下载视频
    :param url:
    :return:
    """
    path = r"E:\大宇茶馆话说唐朝"
    if not os.path.exists(path):
        os.mkdir(path)
        print("创建目录成功")
    command = "you-get %s -o   %s" % (url, path)
    print(command)
    resp = os.system(command)
    print(resp)


if __name__ == "__main__":
    pl_list = get_play_list()
    download_pool(pl_list)
