import matplotlib.pyplot as plt


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


def difference_neighboring(list_):
    differences = []
    for n in range(1, len(list_)):
        differences.append(list_[n] - list_[n - 1])
    return differences


start = 2
end = 1000000
primes = prime_numbers(end=end, start=start)
difference = difference_neighboring(primes)
x = [n for n in range(1, len(difference) + 1)]
y = difference
# plotting
plt.title(f'difference between neighbors prime nums (from range [{start}, {end}])')
plt.xlabel('n')
plt.ylabel('diff')
plt.grid()
plt.plot(x, y)
plt.show()
