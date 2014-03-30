#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fanfou import Fanfou
from config import consumer_key, client_secret
from config import resource_owner_key, resource_owner_secret
import sys
import getopt

def main():
    short_opts = 's:'
    opts = ['desc=']
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    desc = None
    for opt, arg in opts:
        if opt in ('-s', '--desc'):
            desc = arg
        else:
            print(help)
            sys.exit(1)

    photo_data = sys.stdin

    fanfou = Fanfou(api_key=consumer_key,
               api_secret=client_secret,
               oauth_token=resource_owner_key,
               oauth_token_secret=resource_owner_secret)
    fanfou.post_photo(photo_data, desc=desc)


if __name__ == "__main__":
    main()
