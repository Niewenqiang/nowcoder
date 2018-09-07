# -*- coding: utf-8 -*-
# 牛客
# 数串

import sys
a=[]
while 1:
    line = sys.stdin.readline().strip()
    if line:
        b = list(map(int, line.split()))
        a.append(b)
    else:
        break

for i in range(1,len(a),2):
    compare = lambda a, b: cmp(str(a) + str(b), str(b) + str(a))
    min_string = sorted(a[i], cmp=compare, reverse=True)
    print ''.join(str(s) for s in min_string)

