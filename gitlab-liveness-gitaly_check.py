import json
import sys
from pprint import pprint

jdata = open(sys.argv[1])

data = json.load(jdata)

if data['gitaly_check']['status'] == 'ok':
    print ('0 gitlab-liveness-gitaly_check - liveness-gitaly_check status: ' + data['gitaly_check']['status'])
else:
    print ('2 gitlab-liveness-gitaly_check - liveness-gitaly_check status: ' + data['gitaly_check']['status'])    
    
obj = data

def dump(obj, nested_level=0, output=sys.stdout):
    spacing = '   '
    if isinstance(obj, dict):
        print >> output, '%s{' % ((nested_level) * spacing)
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print >> output, '%s%s:' % ((nested_level + 1) * spacing, k)
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s: %s' % ((nested_level + 1) * spacing, k, v)
        print >> output, '%s}' % (nested_level * spacing)
    elif isinstance(obj, list):
        print >> output, '%s[' % ((nested_level) * spacing)
        for v in obj:
            if hasattr(v, '__iter__'):
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s' % ((nested_level + 1) * spacing, v)
        print >> output, '%s]' % ((nested_level) * spacing)
    else:
        print >> output, '%s%s' % (nested_level * spacing, obj)

dump(obj)

jdata.close()