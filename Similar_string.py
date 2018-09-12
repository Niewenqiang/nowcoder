# -*- coding: utf-8 -*-

# 相似字符串

def solve(S, T):
    if not S or not T:
        return 0
    if len(S) < len(T):
        return 0
    count = 0
    for i in range(len(S) - len(T) + 1):
        if isSomorphic(S[i:i+len(T)], T):
            count += 1
    return count
def isSomorphic(S, T):
    return len(set(S)) == len(set(T)) == len(set(zip(S, T)))

print solve('ababcba', 'xyx')
