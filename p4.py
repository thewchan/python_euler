"""Largest palindrome product.

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def chk_palindrome(string):
    """Return Boolean if input string is a palindrome."""
    if len(string) <= 1:
        return True

    return (string[0] == string[-1]) * chk_palindrome(string[1:-1])


def main():
    """Print the largest palindrome product of two 3-digit numbers."""
    palindrome = 0

    for i in range(100, 1000):

        for j in range(100, 1000):
            product = i * j
            string = str(product)

            if chk_palindrome(string) and (int(string) > palindrome):
                palindrome = int(string)
    print(palindrome)


if __name__ == '__main__':
    main()
