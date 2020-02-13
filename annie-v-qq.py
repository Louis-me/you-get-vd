#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
import threading
from concurrent.futures import ThreadPoolExecutor

__author__ = 'shikun'
__CreateAt__ = '2020/2/9-12:16'

lock = threading.Lock()


def get_play_list():
    play_list = []
    with open("play_list.txt") as f:
        for i in f.readlines():
            play_list.append(i.rstrip())
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
    # lock.acquire()
    cookies = "cookies.txt"
    command = "annie -retry 10 -c %s %s" % (cookies, url)
    # print(command)
    resp = os.system(command)
    print("==============")
    print(resp)
    # lock.release()


def generate_mp4list():
    walk_dir = os.getcwd()
    is_clear = True
    for root, subdirs, files in os.walk(walk_dir):
        for file in files:
            ex = file.split(".")
            if ex[-1].lower() == 'mp4':
                print(ex[0].split("["))
                if is_clear:
                    with open(ex[0].split("[")[0] + ".txt", "w", encoding="utf-8") as f1:
                        is_clear = False
                mp4_name = os.path.splitext(file)[0] + ".mp4"
                # 写入格式为：file  '将夜 第4集.mp4' 到mp4list.txt
                with open(ex[0].split("[")[0] + ".txt", "a+", encoding="utf-8") as f:
                    f.write("file  '%s' \n" % mp4_name)


# mp4list.txt中的数据生成mp4
def generate_mp4():
    walk_dir = os.getcwd()
    try:
        for root, subdirs, files in os.walk(walk_dir):
            for file in files:
                ex = file.split(".")
                if ex[-1].lower() == 'txt':
                    cmd = "ffmpeg -y -f concat -safe 0 -i %s -c copy mp4/%s.mp4" % (file, ex[0])
                    print(cmd)
                    os.system(cmd)

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    pl_list = get_play_list()
    # print(pl_list)
    download_pool(pl_list)
    generate_mp4list()
