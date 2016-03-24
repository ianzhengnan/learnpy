

import re

r = 'kkk_ian@kaka.com'
m = re.match(r'^([a-zA-Z0-9\.?\_?\-?]+)@([a-zA-Z]+)(\.?)(com|net|org|cn)$(\.?)(cn)?', r)

if m:
    print(m)
else:
    print('Not march')

