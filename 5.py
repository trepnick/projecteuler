#!/usr/bin/env python

result = 1

for i in range(1,21):
    result *= i

while result % 2 == 0:
    result //= 2

print(result)