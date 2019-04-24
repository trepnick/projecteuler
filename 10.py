#!/usr/bin/env python

from sympy.ntheory import primerange

result = sum(primerange(0,2000000))

print(result)