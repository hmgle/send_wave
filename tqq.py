#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Tqq(object):
    def __init__(self, access_token, oauth_consumer_key, openid, clientip):
        self.access_token = access_token
        self.oauth_consumer_key = oauth_consumer_key
        self.openid = openid
        self.clientip = clientip
        self.prefixurl = "https://open.t.qq.com/api/"
        self.msg_url = self.prefixurl + "t/add"
        self.photo_url = self.prefixurl + "t/add_pic"

    def post_msg(self, msg):
        payload = {
            "content": msg,
            "format": "json",
            "access_token": self.access_token,
            "oauth_consumer_key": self.oauth_consumer_key,
            "openid": self.openid,
            "oauth_version": "2.a",
            "clientip": self.clientip,
            "scope": "all",
        }
        ret = requests.post(self.msg_url, data=payload)
        if ret.status_code != 200:
            print(ret.content)
        return ret

    def post_photo(self, photo_data, desc="no content"):
        files = {"pic": photo_data}
        extra = {
            "access_token": self.access_token,
            "oauth_consumer_key": self.oauth_consumer_key,
            "openid": self.openid,
            "oauth_version": "2.a",
            "scope": "all",
            "format": "json",
            "clientip": self.clientip,
            "content": desc,
        }
        ret = requests.post(self.photo_url, files=files, data=extra)
        if ret.status_code != 200:
            print(ret.content)
        return ret
