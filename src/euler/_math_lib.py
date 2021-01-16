import math


def _gcd(a: int, b: int) -> int:
    if b:
        return _gcd(b, a % b)
    return a


def _lcm(a: int, b: int) -> int:
    return a * b // _gcd(a, b)


def _eratosthenes(limit: int) -> list[int]:

    prime = [True for i in range(limit)]
    p = 2
    while p ** 2 <= limit:
        if prime[p] == True:
            for i in range(p * 2, limit, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return [i for i in range(limit) if prime[i]]
