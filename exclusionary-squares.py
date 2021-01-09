#!/usr/bin/env python3

# An exclusionary square is an integer with distinct digits whose
# square is made up of digits not included in itself:
#
# Courtesy Cliff Pickover
# http://sprott.physics.wisc.edu/pickover/extremec.html


def digits(n: int):
    "Return a generator of all digits in n."
    while n:
        yield (n % 10)
        n //= 10


def distinct(a: list):
    "Return True if the list a has distinct elements."
    return len(set(a)) == len(a)


def is_exclusionary_square(n: int):
    """Return true if n has distinct digits and its square is made up
    of digits not included in itself."""
    return distinct(list(digits(n))) and (
        set(digits(n)).intersection(set(digits(n * n))) == set()
    )


assert is_exclusionary_square(639172)
assert not is_exclusionary_square(639173)


def solve(n: int):
    "Find exclusionary squares up to n."
    for i in range(1, n):
        if is_exclusionary_square(i):
            yield i


print(list(solve(1000000)))
# [2, 3, 4, 7, 8, 9, 17, 18, 24, 29, 34, 38, 39, 47, 53, 54, 57, 58,
# 59, 62, 67, 72, 79, 84, 92, 94, 157, 158, 173, 187, 192, 194, 209,
# 237, 238, 247, 253, 257, 259, 307, 314, 349, 359, 409, 437, 459,
# 467, 547, 567, 612, 638, 659, 672, 673, 689, 712, 729, 738, 739,
# 749, 789, 807, 812, 813, 814, 834, 853, 854, 862, 904, 924, 1547,
# 1607, 1807, 2087, 2107, 2108, 2349, 2398, 2538, 3087, 3108, 3157,
# 3158, 3249, 3257, 3409, 3467, 3487, 3862, 3879, 3892, 3908, 3968,
# 4209, 4253, 5187, 5307, 5349, 5467, 5607, 5812, 6172, 6357, 6572,
# 6579, 6712, 6739, 6912, 6952, 7018, 7284, 7362, 7392, 7853, 7894,
# 7908, 7954, 8039, 8124, 8439, 15094, 15467, 20359, 21058, 21598,
# 24759, 24853, 25749, 34759, 37659, 38924, 54187, 63257, 63259,
# 63852, 65038, 73609, 73862, 76409, 203879, 639172]
