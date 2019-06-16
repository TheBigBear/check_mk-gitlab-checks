#!/bin/python3

import ssl
import urllib.request

import json
import sys
import os
from pprint import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://localhost/-/liveness'
response = urllib.request.urlopen(url, context=ctx)
jdata = response      

data = json.load(jdata)

if data['cache_check']['status'] == 'ok':
    print ('0 gitlab-liveness-cache_check - liveness-cache_check status: ' + data['cache_check']['status'])
else:
    print ('2 gitlab-liveness-cache_check - liveness-cache_check status: ' + data['cache_check']['status'])    
    
jdata.close()
