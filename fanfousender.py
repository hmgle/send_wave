#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
from requests_oauthlib import OAuth1Session
from config import consumer_key, client_secret
from config import resource_owner_key, resource_owner_secret

postmsgurl = 'http://api.fanfou.com/statuses/update.json'
fanfou = OAuth1Session(consumer_key,
                       client_secret=client_secret,
                       resource_owner_key=resource_owner_key,
                       resource_owner_secret=resource_owner_secret)
msg = ''
for line in fileinput.input():
    msg += line

payload = {'status': msg}

r = fanfou.post(postmsgurl, data=payload)
print r.status_code
