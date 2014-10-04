# Send_wave

## 简介

一个方便命令行发送**饭否**消息的工具。

## 配置

	cp config.cfg.example config.cfg

然后用编辑器打开`config.cfg`, 根据自己申请的AppKey填写相关选项， 然后:

	python fanfou_config.py

根据提示输入用户名和密码。

## 使用示例

发送一条消息：

	echo "明天会不一样哟！" | ./fanfousender.py

超过140字自动分多次发完。

上传一张照片：

	cat photo_name.png | ./fanfouphoto.py
	# 或 cat photo_name.png | ./fanfouphoto.py -s "照片描述"

## Tip

* 定时发送消息:
	```console
$ crontab -l # 每天8点问好
0 8 * * * cd /home/send_wave_dir && (echo "每天问声好，维持下知名度。\n大家早上好.\n-芝麻" | ./fanfousender.py)
	```

* 直接把大段文本作为图片发送:

		cat input_txt | txt2bmp | convert - png:- | ./fanfouphoto.py

	其中的 `txt2bmp` 是一个将文本转换为bmp图片的工具，发布在: https://github.com/hmgle/txt2bmp

* 用 `fortune` 产生一句随机的趣话， 再用 `cowsay`
加上一个公牛图案，作为png图片发送:

		fortune | cowsay | txt2bmp | convert - png:- | ./fanfouphoto.py
