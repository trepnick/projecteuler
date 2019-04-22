#!/usr/bin/env python

fib = [1,2]
i = 1

while i < 4000000:
    i = fib[-1] + fib[-2]
    fib.append(i)

sum = 0

for i in fib:
    if i % 2 == 0:
        sum += i

print(sum)