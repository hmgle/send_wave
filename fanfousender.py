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
    fanfou.post_msg(msg)
