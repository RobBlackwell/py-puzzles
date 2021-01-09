#!/usr/bin/env python3

# Your mission: find positive integer solutions for this equation,
# with each variable being a single digit.
# A x B x C = C x D x E = E x F x G
#
# Courtesy Cliff Pickover on Twitter.
#
# https://twitter.com/pickover/status/1346617186702532610
#
# We further assume that A, B, C, D, E, F and G are unique.


def unique(a, b, c, d, e, f, g):
    x = [a, b, c, d, e, f, g]
    return len(x) == len(set(x))


def test(a, b, c, d, e, f, g):
    return unique(a, b, c, d, e, f, g) and ((a * b * c) == (c * d * e) == (e * f * g))


def solve():
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    for e in range(1, 10):
                        for f in range(1, 10):
                            for g in range(1, 10):
                                if test(a, b, c, d, e, f, g):
                                    yield (a, b, c, d, e, f, g)


print(next(solve()))
# (1, 8, 9, 2, 4, 3, 6)


print(list(solve()))
# [(1, 8, 9, 2, 4, 3, 6),
# (1, 8, 9, 2, 4, 6, 3),
# (3, 6, 4, 2, 9, 1, 8),
# (3, 6, 4, 2, 9, 8, 1),
# (6, 3, 4, 2, 9, 1, 8),
# (6, 3, 4, 2, 9, 8, 1),
# (8, 1, 9, 2, 4, 3, 6),
# (8, 1, 9, 2, 4, 6, 3)]
