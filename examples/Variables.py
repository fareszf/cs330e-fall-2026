#!/usr/bin/env python3

# ------------
# Variables.py
# ------------

print("Variables.py")

# Immutable object: rebinding doesn't affect the original variable
i = 2
v = i
assert i is v
v += 1
assert i == 2
assert v == 3

# Aliasing a mutable object
a = [2, 3, 4]
b = a
b[1] += 1
assert a == [2, 4, 4]
assert a is b

# Copying a list
a = [2, 3, 4]
b = a[:]
b[1] += 1
assert a == [2, 3, 4]
assert b == [2, 4, 4]
assert a is not b

# Slicing an entire tuple may return the same object
a = (2, 3, 4)
b = a[:]
assert a is b

# += mutates a list
a = [2, 3, 4]
b = a
b += [5]
assert a == [2, 3, 4, 5]
assert a is b

# + creates a new list
a = [2, 3, 4]
b = a
b = b + [5]
assert a == [2, 3, 4]
assert b == [2, 3, 4, 5]
assert a is not b

# += on a tuple creates a new tuple
a = (2, 3, 4)
b = a
b += (5,)
assert a == (2, 3, 4)
assert b == (2, 3, 4, 5)
assert a is not b

print("Done.")