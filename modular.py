"""
1) math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
2) math.log2()	Returns the base-2 logarithm of x
3) math.isclose()	Checks whether two values are close to each other, or not
4) math.ceil()	Rounds a number up to the nearest integer
5) math.gamma()	Returns the gamma function at x
"""
# 1
import math
a =  math.perm(12,2)
print(a)
# 2
b = math.log2(16)
print(b)
# 3
c = math.isclose(2,2)
d = math.isclose(2,3)
print(c)
print(d)
# 4
e = math.ceil(2.90002)
f = math.ceil(-2.90002)
print(e)
print(f)
# 5
g = math.gamma(5)
print(g)