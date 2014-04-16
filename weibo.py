#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Weibo(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.msg_url = "https://api.weibo.com/2/statuses/update.json"
        self.photo_url = "https://upload.api.weibo.com/2/statuses/upload.json"

    def post_msg(self, msg):
        payload = {
            "status": msg,
            "access_token": self.access_token,
        }
        ret = requests.post(self.msg_url, data=payload)
        if ret.status_code != 200:
            print(ret.content)
        return ret

    def post_photo(self, photo_data, desc="no content"):
        files = {"pic": photo_data}
        extra = {
            "access_token": self.access_token,
            "scope": "all",
            "status": desc,
        }
        ret = requests.post(self.photo_url, files=files, data=extra)
        if ret.status_code != 200:
            print(ret.content)
        return ret
