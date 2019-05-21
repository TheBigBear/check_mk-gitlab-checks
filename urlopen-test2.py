#!/bin/python3

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import sys

with urlopen('https://git.ict.om.org/-/liveness') as response:
    response = response.read()

    obj = response

    print (response)

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
