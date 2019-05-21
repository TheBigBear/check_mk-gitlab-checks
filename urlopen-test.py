#!/bin/python3

import sys
from urllib.request import Request, urlopen
from urllib.error import URLError
req = Request('https://git.ict.om.org/-/liveness')
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    obj = response.read()
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

        dump (obj)
            
