#!/bin/python2

import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['db_check']['status'] == 'ok':
    print ('0 gitlab-liveness-db_check - liveness-db_check status: ' + data['db_check']['status'])
else:
    print ('2 gitlab-liveness-db_check - liveness-db_check status: ' + data['db_check']['status'])    

jdata.close()
