#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'shikun'
__CreateAt__ = '2020/2/6-20:53'

import os
from concurrent.futures import ThreadPoolExecutor

cookies = "cookies.txt"
download_path = r"e:\tx"


def get_play_list():
    play_list = []
    with open("play_list.txt") as f:
        for i in f.readlines():
            play_list.append(i[0:-1])
    return play_list


def download_pool(play_list):
    """
    线程池下载视频
    :param play_list: 下载视频列表
    :return:
    """
    with ThreadPoolExecutor(len(play_list)) as pool:
        pool.map(download, play_list)


def download(url):
    """
    下载视频
    :param url:
    :return:
    """
    # url = "https://v.qq.com/x/cover/rpup19lfbuf2skc/s0028fkasvx.html"
    resp = os.system(r'you-get -c %s  %s -o %s' % (cookies, url, download_path))
    print(resp)


if __name__ == "__main__":
    pl_list = get_play_list()
    download_pool(pl_list)
