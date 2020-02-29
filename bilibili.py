#!/usr/bin/env python
# -*- coding=utf-8 -*-
from concurrent.futures import ThreadPoolExecutor

__author__ = 'shikun'
__CreateAt__ = '2020/2/13-10:19'
import os


def download_pool(play_list):
    """
    线程池下载视频
    :param play_list: 下载视频列表
    :return:
    """
    with ThreadPoolExecutor(len(play_list)) as pool:
        pool.map(download, play_list)


def get_play_list():
    url = "https://www.bilibili.com/video/av15207431?p="
    data = []
    for i in range(1, 24):
        data.append(url + str(i))
    return data


def download(url):
    """
    下载视频
    :param url:
    :return:
    """
    path = r"E:\bilibili\造物小百科.第四季"
    command = "you-get %s -o  %s" % (url, path)
    print(command)
    resp = os.system(command)
    print(resp)


if __name__ == "__main__":
    pl_list = get_play_list()
    download_pool(pl_list)
