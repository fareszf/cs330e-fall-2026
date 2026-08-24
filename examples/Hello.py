#!/usr/bin/env python3

# --------
# Hello.py
# --------

"""
A simple Python starter program.

The UTCS machines currently use Python 3.12.3.
Students should install Python 3.12.x locally, preferably Python 3.12.3,
to match the course environment as closely as possible.

The following commands are intended for the UTCS Linux machines.
They should also work on macOS Terminal, but may not work as written
on Windows Command Prompt or PowerShell.
"""


def main():
    """Run the program."""
    print("Nothing to be done.")


if __name__ == "__main__":
    main()


"""
-----------------------------------------------------------------------------
Sample terminal session / commands
-----------------------------------------------------------------------------

This file is named Hello.py.

On the UTCS Linux machines, check the Python version:

    $ python3 --version
    Python 3.12.3

Run the program with python3:

    $ python3 Hello.py
    Nothing to be done.

Make the program executable:

    $ chmod ugo+x Hello.py

Then run it directly:

    $ ./Hello.py
    Nothing to be done.

Run the program with the Python profiler:

    $ python3 -m cProfile Hello.py
    Nothing to be done.
         5 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 Hello.py:1(<module>)
        1    0.000    0.000    0.000    0.000 Hello.py:20(main)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}



If python does not work on Windows, try the Python Launcher instead:

    py --version
    py Hello.py

The first line of this file,

    #!/usr/bin/env python3

is called a shebang. On Linux/macOS, it tells the operating system to run
this file using python3 when the file is executed directly.

The block

    if __name__ == "__main__":
        main()

means: call main() only when this file is run directly as a program.

If this file is imported as a module, main() is not called automatically.

Example:

    $ python3
    >>> import Hello
    >>> Hello.main()
    Nothing to be done.
    >>> quit()

To get interactive Python help:

    $ python3
    Python 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] on linux
    ...
    >>> help()
    Welcome to Python 3.12's help utility! If this is your first time using
    Python, you should definitely check out the tutorial at
    https://docs.python.org/3.12/tutorial/.
    ...
    To quit this help utility and return to the interpreter,
enter "q" or "quit".

    help> range
    Help on class range in module builtins:

    class range(object)
     |  range(stop) -> range object
     |  range(start, stop[, step]) -> range object
     |
     |  Return an object that produces a sequence of integers from start (inclusive)
     |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
     |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
     |  These are exactly the valid indices for a list of 4 elements.
     |  When step is given, it specifies the increment (or decrement).
     |
     |  Methods defined here:
     |
     |  __bool__(self, /)
     |      True if self else False
     |
     |  __contains__(self, key, /)
     |      Return bool(key in self).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
    ...
    help> quit
    >>> quit()

To see The Zen of Python:

    $ python3
    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

    >>> quit()

Python was created by Guido van Rossum and first released in 1991.

Python is procedural, object-oriented, dynamically typed, and garbage collected.
-----------------------------------------------------------------------------
"""