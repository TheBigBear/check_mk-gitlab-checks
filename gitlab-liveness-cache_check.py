#/bin/python2

import json
import sys
import subprocess
from pprint import pprint

jdata = subprocess.call(["curl", "-s", "https://localhost/-/liveness", "--insecure"])

data = json.load(jdata)

if data['cache_check']['status'] == 'ok':
    print ('0 gitlab-liveness-cache_check - liveness-cache_check status: ' + data['cache_check']['status'])
else:
    print ('2 gitlab-liveness-cache_check - liveness-cache_check status: ' + data['cache_check']['status'])    
    
jdata.close()
