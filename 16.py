#!/usr/bin/env python

num = str(2**1000)
result = 0
for digit in num:
    result += int(digit)

print(result)