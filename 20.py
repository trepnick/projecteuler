#!/usr/bin/env python

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

sum = sum([int(i) for i in str(fact(100))])

print(sum)