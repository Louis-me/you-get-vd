# 分析下载腾讯视频

## 获取播放列表
- 通过F12调试，得到播放列表的Js为：
```buildoutcfg
play_list = document.querySelectorAll("body > div:nth-child(3) > div.site_container.container_main > div.container_inner > div > div.wrapper_main > div._playsrc_series > span > div > div > div:nth-child(1) > span>a")
for(var i=0;i< play_list.length;i++){console.log(play_list[i].href)}

```
## 导出登录腾讯视频的会员cookie
- 使用cookies.txt插件

## 安装依赖文件
-  安装[you-get](https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E)```pip3 install you-get```
- [FFmpeg](https://www.ffmpeg.org/)

## 执行命令下载

- 会员下载,需要用到cookie

```you-get -c d:\cookies.txt https://v.qq.com/x/cover/rpup19lfbuf2skc/y002856bq4f.html -o e:\tx```

## 运行代码
- 直接运行vqq.py中代码
- 爱奇艺的会员视频无法下载