#!/usr/bin/env python

result = 0

for i in range(999,1,-1):
    for j in range(999,1,-1):
        if i * j > result and str(i * j)[::-1] == str(i * j):
            result = i * j


print(result)