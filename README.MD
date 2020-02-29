# 分析下载腾讯视频

## 获取播放列表
- 通过F12调试，得到播放列表的Js
```buildoutcfg
play_list = document.querySelectorAll("body > div:nth-child(3) > div.site_container.container_main > div.container_inner > div > div.wrapper_main > div._playsrc_series > span > div > div > div:nth-child(1) > span>a")
for(var i=0;i< play_list.length;i++){console.log(play_list[i].href)}

```
- 然后把得到的列表复制到play_list.txt中即可
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

## 2020-2-8 更新说明
-  ```vqq.py``` 经过测试,不能下载会员视频
- ```ts_to_mp4.py``` 包含将ts合并为mp4,然后在把所有mp4合并成一个总的mp4文件,此处合并后,视频不完整,应该是下载的ts文件不完整

## 2020-2-9 
- 经过测试,使用[annie](https://github.com/iawia002/annie) 和cookie的方式成功下载会员视频
- cookie 内容必须为name=value;name=value的方式,最简单获取的方式就是抓包获取
- 最终验证结果是,用annie下载了会员的视频后，最终用ffmpeg合并时报错，就算合并成功后,也是播放不了

## 2020-2-13 更新
- b站视频下载成功

## 关于会员下载总结
- 非会员视频可以采用you-get和annie,会员的视频获取cookie去下载,经常不行

## 2020-2-29更新
- 新增对荔枝fm音频下载