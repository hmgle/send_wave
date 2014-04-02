#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import quote, urlencode
import urllib2
import time
import uuid
import hmac, hashlib
from config import consumer_key, client_secret

def get_token():
    URL = 'http://fanfou.com/oauth/request_token'

    params = [
        ('oauth_consumer_key', consumer_key),
        ('oauth_nonce', uuid.uuid4().hex),
        ('oauth_signature_method', 'HMAC-SHA1'),
        ('oauth_timestamp', int(time.time())),
    ]

    params.sort()

    p = 'GET&%s&%s' % (quote(URL, safe=''), quote(urlencode(params)))
    signature = hmac.new(client_secret + '&', p,
                    hashlib.sha1).digest().encode('base64').rstrip()

    params.append(('oauth_signature', quote(signature)))

    h = ', '.join(['%s="%s"' % (k, v) for (k, v) in params])

    r = urllib2.Request(URL, headers={'Authorization': 'OAuth realm="", %s' % h})

    data = urllib2.urlopen(r).read()
    token, secret = [pair.split('=')[1] for pair in data.split('&')]

    return token, secret

if __name__ == '__main__':
    print get_token()
