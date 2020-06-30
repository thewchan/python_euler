"""Smallest multiple.

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def chk_divisible(num):
    """Return Boolean if input number is divisible by 1-20."""
    nums = [x for x in range(1, 21)]

    for factor in nums:

        if num % factor != 0:
            return False

    return True


def main():
    """Print the first number divisible by all numbers between 1 to 20."""
    found = False
    try_num = 20

    while not found:

        if not chk_divisible(try_num):
            try_num += 1
            continue

        else:
            print(try_num)
            found = True


if __name__ == '__main__':
    main()
