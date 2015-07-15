install::
	mkdir -p ~/.send_wave
	cp -p config.cfg.example ~/.send_wave/config.cfg
	cp *.py /usr/local/bin/

uninstall::
	-rm -rf ~/.send_wave
	-rm -f /usr/local/bin/fanfou_config.py
	-rm -f /usr/local/bin/fanfouphoto.py
	-rm -f /usr/local/bin/fanfou.py
	-rm -f /usr/local/bin/fanfousender.py
	-rm -f /usr/local/bin/request_token.py
	-rm -f /usr/local/bin/tqq_msg.py
	-rm -f /usr/local/bin/tqq_pic.py
	-rm -f /usr/local/bin/tqq.py
	-rm -f /usr/local/bin/weibo_msg.py
	-rm -f /usr/local/bin/weibo_pic.py
	-rm -f /usr/local/bin/weibo.py
