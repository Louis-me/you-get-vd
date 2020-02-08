#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'shikun'
__CreateAt__ = '2020/2/7-16:30'

import os


def to_mp4():
    """
    所有ts转换为mp4文件
    ts文件列表来源为idm下载腾讯视频
    :return:
    """
    count = 0
    with open("mp4list.txt", "w") as f1:
        pass
    for root, subdirs, files in os.walk(r"E:\demo\you-get-vd\ts"):
        for file in files:
            if file.split(".")[-1].lower() == 'ts':
                file_path = os.path.join(root, file)
                mp4_name = os.path.splitext(file)[0] + ".mp4"
                mp4_file_path = r"E:\demo\you-get-vd" + "\\" + mp4_name
                # 写入格式为：file  '将夜 第4集.mp4' 到mp4list.txt
                with open("mp4list.txt", "a+") as f:
                    f.write("file  '%s' \n" % mp4_name)
                if os.path.isfile(mp4_file_path):
                    continue
                # ffmpeg把所有ts文件转换为mp4
                os.system("ffmpeg -i " + "\"" + file_path + "\"" + " \"" + mp4_file_path + "\"")
                count = count + 1
                print(file_path)
    print("Done the total number of file was be converted: ", count)


# mp4list.txt中的数据生成mp4
def generate_mp4():
    os.system("ffmpeg -y -f concat -safe 0 -i mp4list.txt -c copy mp4/4.mp4")


if __name__ == "__main__":
    to_mp4()
    generate_mp4()
