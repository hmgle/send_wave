# Send_wave

## 简介

一个方便命令行发送**饭否**消息的工具。

## 配置

	cp config.cfg.example config.cfg

然后用编辑器打开`config.cfg`, 根据自己申请的AppKey填写相关选项， 然后:

	python config.cfg

根据提示输入用户名和密码。

## 使用示例

发送一条消息：

	echo "明天会不一样哟！" | ./fanfousender.py

超过140字自动分多次发完。

上传一张照片：

	cat photo_name.png | ./fanfouphoto.py
	# 或 cat photo_name.png | ./fanfouphoto.py -s "照片描述"
