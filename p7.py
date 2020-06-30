"""10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10001st prime number?
"""


def chk_prime(num):
    """Check to see if the number is prime."""
    if num <= 1:
        return False

    if num == 2:
        return True

    num_lst = [x for x in range(1, num + 1)]

    for i in num_lst[1:-1]:

        if num % i == 0:
            return False

    return True


def main():
    """Print the 10001st prime number."""
    counter = 0
    num = 0

    while counter != 10_001:
        num += 1
        
        if chk_prime(num):
            counter += 1

    print(f'{counter}: {num}')


if __name__ == '__main__':
    main()
