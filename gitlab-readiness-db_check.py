#/bin/python2

import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['db_check']['status'] == 'ok':
    print ('0 gitlab-readiness-db_check - readiness-db_check status: ' + data['db_check']['status'])
else:
    print ('2 gitlab-readiness-db_check - readiness-db_check status: ' + data['db_check']['status'])    

jdata.close()
