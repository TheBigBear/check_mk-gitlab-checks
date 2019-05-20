import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['redis_check']['status'] == 'ok':
    print ('0 gitlab-readiness-redis_check - readiness-redis_check status: ' + data['redis_check']['status'])
else:
    print ('2 gitlab-readiness-redis_check - readiness-redis_check status: ' + data['redis_check']['status'])    

jdata.close()