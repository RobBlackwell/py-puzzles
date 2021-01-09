#!/usr/bin/env python3

# Luminescent being: A luminescent being from Alpha Centauri comes to
# your home to test humanity's intelligence. If you answer correctly,
# humanity may become part of a large intergalactic federation. Here's
# the problem that the alien writes on your front door, so that your
# neighbours may help.
#
# 1. Consider an integer N that is greater than 1.
# 2. Consider the integer M which is the square root of N.
# 3. Given that M is the sum of the digits of in N, what is N?
#
# Courtesy Cliff Pickover on Twitter.
#
# https://twitter.com/pickover/status/1347189058582282242?s=20


from itertools import count
import math


def sum_digits(n: int):
    "Return the sum of the digits in n."
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def solve():
    for n in count(2):
        m = math.sqrt(n)
        if m.is_integer() and (m == sum_digits(n)):
            return n


print(solve())
# 81
