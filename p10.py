"""Summation of primes.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from math import sqrt


# def chk_prime_simple(num):
#     """Check to see if the number is prime."""
#     if num <= 1:
#         return False

#     if num == 2:
#         return True

#     num_lst = [x for x in range(1, num + 1)]

#     for i in num_lst[1:-1]:

#         if num % i == 0:
#             return False

#     return True


# def chk_prime_adv(num, prime_list):
#     """Check to see if number is prime, more efficient."""
#     sqrt_num = sqrt(num)
#     num_lst = [x for x in range(1, num + 1)]
#     prime_list = set(prime_list)
#     factor_lst = list(filter(lambda x: x in prime_list, num_lst))
#     factor_lst = list(filter(lambda x: x <= sqrt_num, factor_lst))

#     for factor in factor_lst:

#         if num % factor == 0:
#             return False

#     return True


def chk_prime_6k(num):
    """Check to see if number is prime, even more efficient."""
    if num <= 3:
        return num > 1

    elif (num % 2 == 0) or (num % 3 == 0):
        return False

    i = 5

    while i**2 <= num:

        if (num % i == 0) or (num % (i + 2) == 0):
            return False

        i += 6

    return True


def main():
    """Print sum of all primes below 2,000,000."""
    num = 1
    prime_list = []

    while num < 2_000_000:

        # if num < 200:

        #     if chk_prime_simple(num):
        #         prime_list.append(num)
        #         print(num) #, end='\r')
        #     num += 1

        # elif num < 20_000:

        #     if chk_prime_adv(num, prime_list):
        #         prime_list.append(num)
        #         print(num) #, end='\r')
        #     num += 1

        # else:

        #     if chk_prime_6k(num):
        #         prime_list.append(num)
        #         print(num) #, end='\r')
        #     num += 1

        if chk_prime_6k(num):
            prime_list.append(num)
            print(num)

        num += 1

    print(sum(prime_list))


if __name__ == '__main__':
    main()
