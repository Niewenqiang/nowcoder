# -*- coding: utf-8 -*-

# 中国电信笔试
# 反转数字

import sys
while 1:
    line = sys.stdin.readline().strip()
    if line:
        b = line
    else:
        break
def reverse(x):
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[1:][::-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0
print reverse(int(b))
