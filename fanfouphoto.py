#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fanfou import Fanfou
import sys
import getopt
import ConfigParser
from os.path import expanduser

home = expanduser("~")
config = ConfigParser.ConfigParser()
with open(home + '/.send_wave/config.cfg', 'r') as cfgfile:
    config.readfp(cfgfile)
    try:
        consumer_key = config.get('fanfou', 'consumer_key')
        client_secret = config.get('fanfou', 'client_secret')
        resource_owner_key = config.get('fanfou', 'resource_owner_key')
        resource_owner_secret = config.get('fanfou', 'resource_owner_secret')
    except ConfigParser.NoOptionError, err:
        print "先运行fanfou_config.py"
        exit(1)
    if not resource_owner_secret or not resource_owner_key \
            or not consumer_key or not client_secret:
        print "先运行fanfou_config.py"
        exit(1)


def main():
    help = 'Usage: %s [option]' % sys.argv[0]
    help += '''\noption:
    -h | --help                                 display this information
    -s | --desc "photo description"             discription the photo
    '''
    short_opts = 'hs:'
    opts = ['help', 'desc=']
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        print(err)
        print(help)
        sys.exit(1)

    desc = None
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help)
            sys.exit()
        elif opt in ('-s', '--desc'):
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
