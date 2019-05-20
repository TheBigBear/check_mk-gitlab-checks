import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['gitaly_check']['status'] == 'ok':
    print ('0 gitlab-readiness-gitaly_check - readiness-gitaly_check status: ' + data['gitaly_check']['status'])
else:
    print ('2 gitlab-readiness-gitaly_check - readiness-gitaly_check status: ' + data['gitaly_check']['status'])    

jdata.close()