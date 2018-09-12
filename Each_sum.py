# -*- coding: utf-8 -*-

# 中国电信笔试
# 阶乘结果位之和

import sys
while 1:
    line = sys.stdin.readline().strip()
    if line:
        b = line
    else:
        break
b = int(b)
i = b
while i >1:
    i = i - 1
    b = b * (i)
result = sum(int(i) for i in str(b) if i.isdigit())
print result