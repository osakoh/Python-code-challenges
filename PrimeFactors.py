import time

"""
Prime numbers: numbers divisible by itself and 1. E.g 2, 3, 5, 7.
Used in  cryptography and number theory. cryptography and number theory.
Composite number: numbers that can be broken into smaller integers. E.g 4=2x2, 6=2x3
Unit number is 1
"""


def get_prime_factors(number):
    factors = []
    divisor = 2  # because 1 is a unit number

    if number == 1:
        return "1 is a unit number"

    while divisor <= number:
        if (number % divisor) == 0:
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1
    # show
    return factors


print(get_prime_factors(9))

"""
# check the speed of the function
t0 = time.time()

for n in range(1, 100000):
    get_prime_factors(n)

t1 = time.time()


print("Time spent: ", t1 - t0)
"""