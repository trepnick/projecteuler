import math
from logging import getLogger

log = getLogger("rich")


def problem_one() -> int:
    solution = 0
    max_num = 1000
    for num in range(max_num):
        if num % 3 == 0 or num % 5 == 0:
            solution += num
    return solution


def problem_two() -> int:
    ans = 0
    max_num = 4000000

    def fib(max_num):
        a = 1
        b = 1
        next_val = a + b
        while next_val < max_num:
            yield next_val
            a = b
            b = next_val
            next_val = a + b

    for i in fib(max_num):
        if i % 2 == 0:
            ans += i

    return ans


def problem_three() -> int:
    n = 600851475143

    def get_prime_factors(number):
        # create an empty list and later I will
        # run a for loop with range() function using the append() method to add elements to the list.
        prime_factors = []

        # First get the number of two's that divide number
        # i.e the number of 2's that are in the factors
        while number % 2 == 0:
            prime_factors.append(2)
            number = number / 2

        # After the above while loop, when number has been
        # divided by all the 2's - so the number must be odd at this point
        # Otherwise it would be perfectly divisible by 2 another time
        # so now that its odd I can skip 2 ( i = i + 2) for each increment
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            while number % i == 0:
                prime_factors.append(int(i))
                number = number / i

        # Here is the crucial part.
        # First quick refreshment on the two key mathematical conjectures of Prime factorization of any non-Prime number
        # Which is - 1. If n is not a prime number AT-LEAST one Prime factor would be less than sqrt(n)
        # And - 2. If n is not a prime number - There can be AT-MOST 1 prime factor of n greater than sqrt(n).
        # Like 7 is a prime-factor for 14 which is greater than sqrt(14)
        # But if the above loop DOES NOT go beyond square root of the initial n.
        # Then how does that greater than sqrt(n) prime-factor
        # will be captured in my prime factorization function.
        # ANS to that is - in my first for-loop I am dividing n with the prime number if that prime is a factor of n.
        # Meaning, after this first for-loop gets executed completely, the adjusted initial n should become
        # either 1 or greater than 1
        # And if n has NOT become 1 after the previous for-loop, that means that
        # The remaining n is that prime factor which is greater that the square root of initial n.
        # And that's why in the next part of my algorithm, I need to check whether n becomes 1 or not,
        if number > 2:
            prime_factors.append(int(number))

        return prime_factors

    ans = get_prime_factors(n)[-1]
    return ans


def problem_four() -> int:
    def decreasing_products(a, b):
        for c in range(a):
            for d in range(b):
                yield c * d

    ans = 0
    for i in decreasing_products(1000, 1000):
        if str(i) == str(i)[::-1] and i > ans:
            ans = i
    return ans


def problem_five() -> int:
    from functools import reduce

    return reduce(_lcm, range(1, 21))


def problem_six() -> int:
    sum_squares: int = 0
    square_sums: int = 0
    for i in range(1, 101):
        sum_squares += i ** 2
        square_sums += i
    square_sums = square_sums ** 2
    return abs(sum_squares - square_sums)


def problem_seven() -> int:
    def nth_prime(n: int):
        prime_list = [2]
        num = 3
        while len(prime_list) < n:
            for p in prime_list:
                if num % p == 0:
                    break
            else:
                prime_list.append(num)
            num += 2
        return prime_list[-1]

    return nth_prime(10001)


def problem_eight() -> int:
    from functools import reduce

    num: str = "73167176531330624919225119674426574742355349194934\
    96983520312774506326239578318016984801869478851843\
    85861560789112949495459501737958331952853208805511\
    12540698747158523863050715693290963295227443043557\
    66896648950445244523161731856403098711121722383113\
    62229893423380308135336276614282806444486645238749\
    30358907296290491560440772390713810515859307960866\
    70172427121883998797908792274921901699720888093776\
    65727333001053367881220235421809751254540594752243\
    52584907711670556013604839586446706324415722155397\
    53697817977846174064955149290862569321978468622482\
    83972241375657056057490261407972968652414535100474\
    82166370484403199890008895243450658541227588666881\
    16427171479924442928230863465674813919123162824586\
    17866458359124566529476545682848912883142607690042\
    24219022671055626321111109370544217506941658960408\
    07198403850962455444362981230987879927244284909188\
    84580156166097919133875499200524063689912560717606\
    05886116467109405077541002256983155200055935729725\
    71636269561882670428252483600823257530420752963450".replace(
        " ", ""
    )

    current_ans = 0
    for i, j in enumerate(num[:-13]):
        new_ans = reduce((lambda x, y: int(x) * int(y)), num[i : i + 13])
        current_ans = new_ans if new_ans > current_ans else current_ans

    return current_ans


def _unsolved() -> str:
    return "No solution has been provided yet!"


all_solutions = [
    _unsolved,
    problem_one,
    problem_two,
    problem_three,
    problem_four,
    problem_five,
    problem_six,
    problem_seven,
    problem_eight,
]


def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def _lcm(a: int, b: int) -> int:
    return a * b // _gcd(a, b)
