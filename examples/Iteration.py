#!/usr/bin/env python3

# ------------
# Iteration.py
# ------------

from itertools import count

print("Iteration.py")

# iterable, but not iterator
a = [2, 3, 4]
assert hasattr(a, "__iter__")
assert not hasattr(a, "__next__")

s = 0
for v in a:
    s += v
assert s == 9


# rebinding loop variable does not change list
a = [2, 3, 4]
for v in a:
    v += 1
assert a == [2, 3, 4]


# mutating referenced objects does change them
a = [[2], [3], [4]]
for v in a:
    v += [5]
assert a == [[2, 5], [3, 5], [4, 5]]


# tuple unpacking
a = [(2, "abc"), (3, "def"), (4, "ghi")]
s = 0
for u, v in a:
    s += u
assert s == 9


# sets are iterable
a = {2, 3, 4}
s = 0
for v in a:
    s += v
assert s == 9


# dictionaries iterate over keys
d = {2: "abc", 3: "def", 4: "ghi"}

s = 0
for k in d:
    s += k
assert s == 9

assert set(d.keys())   == {2, 3, 4}
assert set(d.values()) == {"abc", "def", "ghi"}
assert set(d.items())  == {
    (2, "abc"),
    (3, "def"),
    (4, "ghi")}


# range is reusable and indexable
x = range(2, 10, 2)

assert hasattr(x, "__iter__")
assert not hasattr(x, "__next__")
assert hasattr(x, "__getitem__")

assert list(x) == [2, 4, 6, 8]
assert x[0] == 2


# for-else
for v in range(10):
    if v == 5:
        break
else:
    assert False


# iterator
x = count(0)

assert hasattr(x, "__iter__")
assert hasattr(x, "__next__")
assert not hasattr(x, "__getitem__")

s = 0
for v in x:
    if v == 5:
        break
    s += v

assert s == 10

print("Done.")