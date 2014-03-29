#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fanfou import Fanfou
from config import consumer_key, client_secret
from config import resource_owner_key, resource_owner_secret
import sys

if __name__ == "__main__":
    photo_data = sys.stdin

    fanfou = Fanfou(api_key=consumer_key,
               api_secret=client_secret,
               oauth_token=resource_owner_key,
               oauth_token_secret=resource_owner_secret)
    fanfou.post_photo(photo_data)
