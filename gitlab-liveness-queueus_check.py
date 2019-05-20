import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['queues_check']['status'] == 'ok':
    print ('0 gitlab-liveness-queues_check - liveness-queues_check status: ' + data['queues_check']['status'])
else:
    print ('2 gitlab-liveness-queues_check - liveness-queues_check status: ' + data['queues_check']['status'])    

jdata.close()