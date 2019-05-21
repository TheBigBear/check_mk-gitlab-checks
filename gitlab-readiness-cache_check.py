#!/bin/pythom2

import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['cache_check']['status'] == 'ok':
    print ('0 gitlab-readiness-cache_check - readiness-cache_check status: ' + data['cache_check']['status'])
else:
    print ('2 gitlab-readiness-cache_check - readiness-cache_check status: ' + data['cache_check']['status'])    

jdata.close()
