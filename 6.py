#!/usr/bin/env python

sumsq = sum([num ** 2 for num in range(1,101)])

sqsum = sum(range(1,101)) ** 2

print (sqsum - sumsq)