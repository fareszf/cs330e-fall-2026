#!/usr/bin/env python3

# -------------
# Assertions.py
# -------------

# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert-stmt


def cycle_length(n):
    assert n > 0
    c = 0
    while n > 1:
        if (n % 2) == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c


print("Assertions.py")

assert cycle_length(1) == 1
assert cycle_length(5) == 6
assert cycle_length(10) == 7

print("Done.")


"""
-----------------------------------------------------------------------------
Sample terminal session / commands
-----------------------------------------------------------------------------

This file is named Assertions.py.

This program intentionally contains an assertion that fails.

The function starts with:

    c = 0

When n is 1, the while loop does not run:

    while n > 1:

Therefore, c is still 0 when this assertion is reached:

    assert c > 0

Run the program on UTCS Linux or macOS Terminal:

    $ python3 Assertions.py
    Assertions.py
    Traceback (most recent call last):
      File "/u/fares/.../Assertions.py", line 25, in <module>
        assert cycle_length(1) == 1
               ^^^^^^^^^^^^^^^
      File "/u/fares/.../Assertions.py", line 19, in cycle_length
        assert c > 0
               ^^^^^
    AssertionError


The traceback shows two important things:

    assert cycle_length(1) == 1

This is the line that called the function.

    assert c > 0

This is the assertion inside the function that actually failed.

Run the program with Python optimization enabled:

    $ python3 -O Assertions.py
    Assertions.py
    Done.

The -O option runs Python in optimized mode.

In optimized mode, Python disables assert statements. Therefore, Python skips:

    assert n > 0
    assert c > 0
    assert cycle_length(1) == 1
    assert cycle_length(5) == 6
    assert cycle_length(10) == 7

Because those assert statements are skipped, the program reaches:

    print("Done.")

-----------------------------------------------------------------------------
"""