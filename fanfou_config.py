#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import getpass
import ConfigParser
from os.path import expanduser


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
    return {"oauth_token": oauth_token, "oauth_secret": oauth_secret}

if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    home = expanduser("~")
    with open(home + '/.send_wave/config.cfg', 'r') as cfgfile:
        config.readfp(cfgfile)
        try:
            consumer_key = config.get('fanfou', 'consumer_key')
            client_secret = config.get('fanfou', 'client_secret')
        except ConfigParser.NoOptionError, err:
            print "需在config.cfg填写consumer_key和client_secret"
            exit(1)
        if not consumer_key or not client_secret:
            print "需在config.cfg填写consumer_key和client_secret"
            exit(1)
        try:
            resource_owner_key = config.get('fanfou', 'resource_owner_key')
            resource_owner_secret = config.get('fanfou', 'resource_owner_secret')
        except ConfigParser.NoOptionError, err:
            resource_owner_key = ''
            resource_owner_secret = ''
        if resource_owner_key and resource_owner_secret:
            exit(0)

        username = raw_input("Username: ")
        password = getpass.getpass("Password: ")
        token = xauth(consumer_key, client_secret, username, password)
        config.set('fanfou', 'resource_owner_key', token['oauth_token'])
        config.set('fanfou', 'resource_owner_secret', token['oauth_secret'])

    config.write(open(home + '/.send_wave/config.cfg', 'wb'))
