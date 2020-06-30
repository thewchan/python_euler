"""Special Pythagorean triplet.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt


def chk_py(a, b):
    """Return Boolean if the two input result in a Pythagorean Triplet."""
    c = sqrt(a**2 + b**2)

    if c != int(c):
        return False

    return True


def main():
    """Find Pythagorean triplet in which their sum is 1000."""
    for a_ in range(1, 1001):

        for b_ in range(1, 1001):

            if a_ >= b_:
                continue

            if chk_py(a_, b_):
                c_ = sqrt(a_**2 + b_**2)
                sum_py = a_ + b_ + c_

                if int(sum_py) == 1000:
                    a = a_
                    b = b_
                    c = int(c_)

    print(f'{a}^2 + {b}^2 = {int(sqrt(a**2 + b**2))}^2, c = {c}')
    print(f'{a} + {b} + {c} = 1000')
    print(f'{a} × {b} × {c} = {a * b * c}')


if __name__ == '__main__':
    main()
