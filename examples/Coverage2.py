#!/usr/bin/env python3

# ------------
# Coverage2.py
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
        self.assertEqual(cycle_length(2), 2)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
-----------------------------------------------------------------------------
Sample terminal session / commands
-----------------------------------------------------------------------------

This file is named Coverage2.py.

This file contains one unit test:

    self.assertEqual(cycle_length(2), 2)

Run the test under coverage with branch coverage enabled:

    $ coverage run --branch Coverage2.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

Then show the coverage report with missing lines:

    $ coverage report -m
    Name           Stmts   Miss Branch BrPart  Cover   Missing
    ----------------------------------------------------------
    Coverage2.py      16      1      4      1    90%   18
    ----------------------------------------------------------
    TOTAL             16      1      4      1    90%

Only cycle_length(2) is tested.

For n = 2, the while loop runs once and takes the even branch:

    if (n % 2) == 0:
        n = n // 2

The odd branch is not covered:

    else:
        n = (3 * n) + 1

This example has better coverage than Coverage1.py, but it still does not
cover every branch.
-----------------------------------------------------------------------------
"""