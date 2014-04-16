#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
from weibo import Weibo
import ConfigParser

config = ConfigParser.ConfigParser()
with open('config.cfg', 'r') as cfgfile:
    config.readfp(cfgfile)
    try:
        access_token = config.get('weibo', 'access_token')
    except ConfigParser.NoOptionError, err:
        print "未配置weibo"
        exit(1)
    if not access_token:
        print "未配置weibo"
        exit(1)


if __name__ == "__main__":
    msg = ''
    for line in fileinput.input():
        msg += line

    weibo = Weibo(access_token=access_token)
    msglen = len(unicode(msg, 'utf-8'))
    if  msglen < 140:
        weibo.post_msg(msg)
    else:
        msgs = [msg.decode('utf8')[i:i+132].encode('utf8')
                for i in range(0, msglen, 132)]
        for m in msgs:
            if m is msgs[0]:
                m = m + '(未完)'
            else:
                m = '接上条: ' + m
            weibo.post_msg(m)
