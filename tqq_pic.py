#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tqq import Tqq
import ConfigParser
import sys
import getopt
from os.path import expanduser

home = expanduser("~")
config = ConfigParser.ConfigParser()
with open(home + '/.send_wave/config.cfg', 'r') as cfgfile:
    config.readfp(cfgfile)
    try:
        access_token = config.get('tqq', 'access_token')
        oauth_consumer_key = config.get('tqq', 'oauth_consumer_key')
        openid = config.get('tqq', 'openid')
        clientip = config.get('tqq', 'clientip')
    except ConfigParser.NoOptionError, err:
        print "未配置tqq"
        exit(1)
    if not access_token or not oauth_consumer_key \
            or not openid or not clientip:
        print "未配置tqq"
        exit(1)


if __name__ == "__main__":
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

    tqq = Tqq(access_token=access_token,
               oauth_consumer_key=oauth_consumer_key,
               openid=openid,
               clientip=clientip)
    tqq.post_photo(photo_data, desc=desc)
