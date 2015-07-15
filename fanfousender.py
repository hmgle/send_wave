#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
from fanfou import Fanfou
import ConfigParser
from os.path import expanduser

home = expanduser("~")
config = ConfigParser.ConfigParser()
with open(home + '/.send_wave/config.cfg', 'r') as cfgfile:
    config.readfp(cfgfile)
    try:
        consumer_key = config.get('fanfou', 'consumer_key')
        client_secret = config.get('fanfou', 'client_secret')
        resource_owner_key = config.get('fanfou', 'resource_owner_key')
        resource_owner_secret = config.get('fanfou', 'resource_owner_secret')
    except ConfigParser.NoOptionError, err:
        print "先运行fanfou_config.py"
        exit(1)
    if not resource_owner_secret or not resource_owner_key \
            or not consumer_key or not client_secret:
        print "先运行fanfou_config.py"
        exit(1)


if __name__ == "__main__":
    msg = ''
    for line in fileinput.input():
        msg += line

    fanfou = Fanfou(api_key=consumer_key,
               api_secret=client_secret,
               oauth_token=resource_owner_key,
               oauth_token_secret=resource_owner_secret)
    msglen = len(unicode(msg, 'utf-8'))
    if  msglen < 140:
        fanfou.post_msg(msg)
    else:
        msgs = [msg.decode('utf8')[i:i+132].encode('utf8')
                for i in range(0, msglen, 132)]
        for m in msgs:
            if m is msgs[0]:
                m = m + '(未完)'
            else:
                m = '接上条: ' + m
            fanfou.post_msg(m)
