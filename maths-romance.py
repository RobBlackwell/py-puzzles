#!/usr/bin/env python3

# Mathematical romance. Your sweetheart turns to you and says "I will
# marry you if you can solve my mathematical challenge. Consider a
# multi-digit integer N which is a power of 2. Moreover, each digit of
# N is also a power of 2. What is N?"
#
# Courtesy Cliff Pickover on Twitter.
# https://twitter.com/pickover/status/1347372641884270594?s=12

from itertools import count
import math


def digits(n: int):
    "Return a generator of all digits in n."
    while n:
        yield (n % 10)
        n //= 10


def is_multi_digit(n: int):
    return n > 9


def is_power_of_two(n: int):
    return math.log2(n).is_integer()


def solve():
    for i in count(0):
        n = 2 ** i
        if is_multi_digit(n) & all([is_power_of_two(i) for i in digits(n)]):
            return n


print(solve())
# 128
