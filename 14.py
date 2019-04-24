#!/usr/bin/env python

def collatz_length(num):
    if num == 1:
        return 1
    elif num % 2 == 0:
        return collatz_length(num // 2) + 1
    else:
        return collatz_length(3 * num + 1) + 1

result = [1,1]

for i in range(1,1000000):
    if collatz_length(i) > result[1]:
        result = i,collatz_length(i)

print(result)