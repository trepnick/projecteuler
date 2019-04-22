#!/usr/bin/env python

from sympy.ntheory import primefactors

num = 600851475143

fact = primefactors(num)

print(fact[-1])