import math


def check_prime_num(num):
    """
    This function using "Wilson's theorem"
    "Wilson's theorem" -- it's easy method checking, but low optimized
    :returns True/False

    """
    if (math.factorial(num - 1) + 1) % num == 0:
        return True
    else:
        return False


def prime_numbers(end, start=2):
    """
    This function using only Python for "Optimized enumeration of divisors"
    :param end: to generation prime nums to "end" (inclusive)
    :param start: default=2, start position for generation
    :return: list-object with prime nums from range [start, end]
    """

    primes = []

    for num in range(start, end + 1):
        is_prime = True

        for divider in range(2, int(num**0.5) + 1):
            if num % divider == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


def write_prime_nums(end, start=2, filename='prime_nums.txt'):
    with open(filename, 'w') as f:
        f.write(str(prime_numbers(end=end, start=start)))
