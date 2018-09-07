# -*- coding: utf-8 -*-
# 牛客
# Fibonacci数列

n = int(input())
x = 0
y = 1
while y < n:
    x, y = y, x+y
print(min(y-n, n-x))
