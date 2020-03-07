from urllib.request import urlopen

import re

try:

    res = urlopen("XXXXXXXXXXXXXXXXXX").read()

    title = re.findall('<title>(.+)</title>', res)

    if res.getcode==403:

        print('403')

    print(title)

except Exception as e:

    print(e)
