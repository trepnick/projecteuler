import math


def gcd(a: int, b: int) -> int:
    if b:
        return gcd(b, a % b)
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def eratosthenes(limit: int) -> list[int]:

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
