#!/usr/bin/env python3

# ------------
# Coverage3.py
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
        self.assertEqual(cycle_length(3), 8)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
-----------------------------------------------------------------------------
Sample terminal session / commands
-----------------------------------------------------------------------------

This file is named Coverage3.py.

This file contains one unit test:

    self.assertEqual(cycle_length(3), 8)

Run the test under coverage with branch coverage enabled:

    $ coverage run --branch Coverage3.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

Then show the coverage report with missing lines:

    $ coverage report -m
    Name           Stmts   Miss Branch BrPart  Cover   Missing
    ----------------------------------------------------------
    Coverage3.py      16      0      4      0   100%
    ----------------------------------------------------------
    TOTAL             16      0      4      0   100%

Only cycle_length(3) is tested.

The sequence for 3 is:

    3, 10, 5, 16, 8, 4, 2, 1

This test covers both branches:

    n = n // 2
    n = (3 * n) + 1

This example reaches 100% coverage.

Important: 100% coverage means every measured line and branch was executed.
It does not prove that the program is correct for every possible input.
-----------------------------------------------------------------------------
"""