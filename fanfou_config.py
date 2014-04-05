#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from config import consumer_key, client_secret
except ImportError:
    print "需要在 config.py 填写 consumer_key 及 client_secret"
    exit(1)

import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import getpass


def xauth(consumer_key, client_secret, username, password):
    oauth = OAuth1(consumer_key, client_secret)
    params = {}
    params["x_auth_username"] = username
    params["x_auth_password"] = password
    params["x_auth_mode"] = 'client_auth'
    request_token_url = 'http://fanfou.com/oauth/access_token'
    r = requests.post(url=request_token_url, auth=oauth, data=params)
    credentials = parse_qs(r.content)
    oauth_token = credentials.get('oauth_token')[0]
    oauth_secret = credentials.get('oauth_token_secret')[0]
    print "token: " + oauth_token
    print "secret: " + oauth_secret

if __name__ == '__main__':
    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")
    xauth(consumer_key, client_secret, username, password)
