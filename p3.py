"""Largest prime factor.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def factorize(num):
    """Return a list of factors."""
    factors = []
    for i in range(1, num + 1):

        if num % i == 0:

            if i in factors:
                break

            factors.append(i)
            factors.append(int(num / i))

    return factors


def main():
    """Print largest prime factor of 600851475143."""
    num = 600851475143
    factors = factorize(num)
    prime_factors = []

    for factor in factors:
        factor_list = factorize(factor)

        if len(factor_list) == 2:
            prime_factors.extend(factor_list)

    prime_factors = list(set(prime_factors))
    prime_factors.sort()
    print(prime_factors)


if __name__ == '__main__':
    main()
