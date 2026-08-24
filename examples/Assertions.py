#!/usr/bin/env python3

# -------------
# Assertions.py
# -------------

# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert-stmt

def cycle_length (n) :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

print("Assertions.py")

assert cycle_length( 1) == 1
assert cycle_length( 5) == 6
assert cycle_length(10) == 7

print("Done.")

""" #pragma: no cover
$ python Assertions.py
Assertions.py
Traceback (most recent call last):
  File "Assertions.py", line 23, in <module>
    assert cycle_length( 1) == 1
  File "Assertions.py", line 18, in cycle_length
    assert c > 0
AssertionError



$ python -O Assertions.py
Assertions.py
Done.
"""
