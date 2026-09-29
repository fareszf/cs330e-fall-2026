#!/usr/bin/env python3

# ------------
# Operators.py
# ------------

# https://docs.python.org/3.8/library/operator.html

from operator import add

print("Operators,py")

# ---------- Arithmetic ----------
a, b = 5, 2
print("negation   :", -a)            # -5
print("addition   :", a + b)         # 7
print("add() func :", add(a, b))     # 7
print("in‑place   :", end=" "); a += b; print(a)  # 7
print("division   :", 5 / 2)         # 2.5 (float)
print("floor div  :", 5 // 2)        # 2
print("modulus    :", 5 % 2)         # 1
print("exponent   :", 2 ** 3)        # 8

# ---------- Bitwise ----------
x, y = 10, 12          # 1010, 1100
print(\"shift left :\", 2 << 3)        # 16
print(\"bitwise ~  :\", ~x)            # -11
print(\"AND        :\", x & y)         # 8
print(\"OR         :\", x | y)         # 14
print(\"XOR        :\", x ^ y)         # 6

# ---------- Boolean / Comparison ----------
print("chain compare:", 2 < 3 < 7 < 8)   # True
a, b, c = True, True, False
print("logical and:", a and b)           # True
print("logical or :", a or c)            # True
print("logical not:", not c)             # True

# ---------- Sequence Ops ----------
lst = [1, 2, 3]
tup = (1, 2, 3)
s   = "abc"

print("indexing   :", lst[1])        # 2
print("concat str :", s + s)        # "abcabc"
print("concat list:", lst + lst)     # [1,2,3,1,2,3]
print("rep tuple  :", tup * 2)       # (1,2,3,1,2,3)

#-----------------------------------
print("Done.")
