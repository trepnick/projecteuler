#!/usr/bin/env python

num = ''
i = 1

while len(num) <= 1000000:
    num += str(i)
    i += 1

result = int(num[1]) * int(num[10]) * int(num[100]) * int(num[1000]) * int(num[10000]) * int(num[100000]) * int(num[1000000])
print(result)