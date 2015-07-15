#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
from tqq import Tqq
import ConfigParser
from os.path import expanduser

home = expanduser("~")
config = ConfigParser.ConfigParser()
with open(home + '/.send_wave/config.cfg', 'r') as cfgfile:
    config.readfp(cfgfile)
    try:
        access_token = config.get('tqq', 'access_token')
        oauth_consumer_key = config.get('tqq', 'oauth_consumer_key')
        openid = config.get('tqq', 'openid')
        clientip = config.get('tqq', 'clientip')
    except ConfigParser.NoOptionError, err:
        print "未配置tqq"
        exit(1)
    if not access_token or not oauth_consumer_key \
            or not openid or not clientip:
        print "未配置tqq"
        exit(1)


if __name__ == "__main__":
    msg = ''
    for line in fileinput.input():
        msg += line

    tqq = Tqq(access_token=access_token,
               oauth_consumer_key=oauth_consumer_key,
               openid=openid,
               clientip=clientip)
    msglen = len(unicode(msg, 'utf-8'))
    if  msglen < 140:
        tqq.post_msg(msg)
    else:
        msgs = [msg.decode('utf8')[i:i+132].encode('utf8')
                for i in range(0, msglen, 132)]
        for m in msgs:
            if m is msgs[0]:
                m = m + '(未完)'
            else:
                m = '接上条: ' + m
            tqq.post_msg(m)
