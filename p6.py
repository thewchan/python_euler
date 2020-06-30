"""Sum square difference.

The sum of the squares of the first ten natural numbers is:

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def main():
    """Print difference between sum of squares and squares of sums."""
    nums = [x for x in range(1, 101)]
    sqr_sum = sum(nums) ** 2
    sum_sqr = sum(list(map(lambda x: x**2, nums)))
    print(abs(sum_sqr - sqr_sum))


if __name__ == '__main__':
    main()
