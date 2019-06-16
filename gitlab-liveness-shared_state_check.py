#!/bin/python3

import ssl
import urllib.request

import json
import sys
from pprint import pprint

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://localhost/-/liveness'
response = urllib.request.urlopen(url, context=ctx)
jdata = response   

data = json.load(jdata)

if data['shared_state_check']['status'] == 'ok':
    print ('0 gitlab-liveness-shared_state_check - liveness-shared_state_check status: ' + data['shared_state_check']['status'])
else:
    print ('2 gitlab-liveness-shared_state_check - liveness-shared_state_check status: ' + data['shared_state_check']['status'])    

jdata.close()
