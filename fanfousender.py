#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
from fanfou import Fanfou
from config import consumer_key, client_secret
from config import resource_owner_key, resource_owner_secret

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
