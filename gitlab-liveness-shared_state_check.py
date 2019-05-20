#/bin/pythom2

import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['shared_state_check']['status'] == 'ok':
    print ('0 gitlab-liveness-shared_state_check - liveness-shared_state_check status: ' + data['shared_state_check']['status'])
else:
    print ('2 gitlab-liveness-shared_state_check - liveness-shared_state_check status: ' + data['shared_state_check']['status'])    

jdata.close()
