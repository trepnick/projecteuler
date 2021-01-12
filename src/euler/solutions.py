import math


def problem_one():
    solution = 0
    max_num = 1000
    for num in range(max_num):
        if num % 3 == 0 or num % 5 == 0:
            solution += num
    return solution


def problem_two():
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


def problem_three():
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


def problem_four():
    def decreasing_products(a, b):
        for c in range(a):
            for d in range(b):
                yield c * d

    ans = 0
    for i in decreasing_products(1000, 1000):
        if str(i) == str(i)[::-1] and i > ans:
            ans = i
    return ans


def _unsolved():
    return "No solution has been provided yet!"


all_solutions = [_unsolved, problem_one, problem_two, problem_three, problem_four]
