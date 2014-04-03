#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from config import consumer_key, client_secret
except ImportError:
    print "需要在 config.py 填写 consumer_key 及 client_secret"
    exit(1)
