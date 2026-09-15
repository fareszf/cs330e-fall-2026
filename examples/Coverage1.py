#!/usr/bin/env python3

# ------------
# Coverage1.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(1), 1)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
-----------------------------------------------------------------------------
Sample terminal session / commands
-----------------------------------------------------------------------------

This file is named Coverage1.py.

This file introduces coverage.py.
It contains one unit test:

    self.assertEqual(cycle_length(1), 1)

Run the test under coverage with branch coverage enabled:

    $ coverage run --branch Coverage1.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

Then show the coverage report with missing lines:

    $ coverage report -m
    Name           Stmts   Miss Branch BrPart  Cover   Missing
    ----------------------------------------------------------
    Coverage1.py      16      4      4      1    65%   15-19
    ----------------------------------------------------------
    TOTAL             16      4      4      1    65%

Only cycle_length(1) is tested.

For n = 1, the while loop does not run:

    while n > 1:

Therefore, the body of the loop is not covered.

The missing lines are:

    if (n % 2) == 0:
        n = n // 2
    else:
        n = (3 * n) + 1
    c += 1

This example shows that a passing unit test does not necessarily mean that
all lines or branches of the code were tested.
-----------------------------------------------------------------------------
"""