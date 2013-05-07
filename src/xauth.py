# import sys, urllib, oauth, re
import sys, urllib, re
import oauth.oauth as oauth
# import httplib
from urllib2 import Request, urlopen

consumer_key = '...'   # api key
consumer_secret = '...'  # api secret
access_token_url = 'http://fanfou.com/oauth/access_token'
verify_url = 'http://api.fanfou.com/account/verify_credentials.xml'

def request_to_header(request, realm=''):
    """Serialize as a header for an HTTPAuth request."""
    auth_header = 'OAuth realm="%s"' % realm
    # print auth_header + " " + str(sys._getframe().f_lineno)
        # Add the oauth parameters.
    if request.parameters:
        for k, v in request.parameters.iteritems():
            if k.startswith('oauth_') or k.startswith('x_auth_'):
                auth_header += ', %s="%s"' % (k, oauth.escape(str(v)))
    return {'Authorization': auth_header}

# get username and password from command line
username = sys.argv[1]
passwd = sys.argv[2]

consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)
params = {}
params["x_auth_username"] = username
params["x_auth_password"] = passwd
params["x_auth_mode"] = 'client_auth'
request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                     http_url=access_token_url,
                                                     parameters=params)
signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
request.sign_request(signature_method, consumer, None)
headers=request_to_header(request)

signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
request.sign_request(signature_method, consumer, None)
headers=request_to_header(request)

resp = urlopen(Request(access_token_url, headers=headers))
token = resp.read()
print token  # access_token got

m = re.match(r'oauth_token=(?P<key>[^&]+)&oauth_token_secret=(?P<secret>[^&]+)', token)
if m:
    oauth_token = oauth.OAuthToken(m.group('key'), m.group('secret'))
    request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                     token=oauth_token,
                                                     http_url=verify_url)
    request.sign_request(signature_method, consumer, oauth_token)
    headers=request_to_header(request)
    resp = urlopen(Request(verify_url, headers=headers))
    resp = resp.read()
    print resp
