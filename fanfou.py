#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests_oauthlib import OAuth1Session


class Fanfou(OAuth1Session):
    def __init__(self, api_key, api_secret, oauth_token, oauth_token_secret):
        self.prefixurl = "http://api.fanfou.com/"
        self.msg_url = self.prefixurl + "statuses/update.json"
        self.photo_url = self.prefixurl + "photos/upload.json"
        super(Fanfou, self).__init__(api_key, client_secret=api_secret,
                    resource_owner_key=oauth_token,
                    resource_owner_secret=oauth_token_secret)

    def post_msg(self, msg):
        payload = {'status': msg}
        ret = self.post(self.msg_url, data=payload)
        if ret.status_code != 200:
            print(ret.content)
        return ret

    def post_photo(self, photo_data, desc=None):
        files = {'photo': photo_data}
        extra = {'status': desc}
        ret = self.post(self.photo_url, files=files, data=extra)
        if ret.status_code != 200:
            print(ret.content)
        return ret
