# -*- coding: utf-8 -*-
# 牛客
# 水仙花数

import sys
a=[]
while 1:
    line = sys.stdin.readline().strip()
    if line:
        b = list(map(int, line.split()))
        a.append(b)
    else:
        break
d = []
for i in range(len(a)):
    start = a[i][0]
    end = a[i][1]
    for j in range(start, end+1):
        value = (j//100) ** 3 +((j-(j//100)*100)//10) ** 3 + (j-(j//100)*100-((j-(j//100)*100)//10)*10) ** 3
        if value == j:
            d.append(j)
    if d == []:
        print('no')
    else:
        print(" ".join([str(x) for x in d]))
    d = []




