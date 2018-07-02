#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(1, 2, 3)
print('Point:', p.x, p.y, p.z)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)