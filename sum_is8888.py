# -*- coding: utf-8 -*-

# 中国电信笔试
# 满足abcd+bcda = 8888

result = []
for j in range(1000,8888):
    a = str(j)[1] + str(j)[2]+ str(j)[3] + str(j)[0]
    a = int(a)
    if a + j == 8888:
        result.append(j)
z = [i for i in '0808']
print ' '.join(z)
for x in result:
    c = [i for i in str(x)]
    print ' '.join(c)