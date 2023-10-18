# 18 / 10 / 2023
# Day - 29
# Perkalian Matriks

import numpy as np

# contoh perkalian matriks
# A
# [
#  a11 a12
#  a21 a22
# ]
# B
# [
#  b11 b12
#  b21 b22
# ]
# A * B
# [
#   a11*b11 + a12*b21   a11*b12 + a12*b21
#   a21*b12 + a22*b21   a21*b12 + a22*b22
# ]

a = np.array(([1, 2], [3, 4]))
b = np.ones([2, 2])
c = np.array(([1, 2, 5], [3, 4, 6]))
d = np.ones([3, 1])
print(f"matriks A:\n{a}")
print(f"matriks B:\n{b}")
print(f"matriks C:\n{c}")
print(f"matriks D:\n{d}")

# perkalian matriks
hasil1 = np.dot(a, b)
hasil2 = a.dot(b)
hasil3 = np.dot(c, d)
hasil4 = c.dot(d)
print(f"hasil-1 :\n{hasil1}")
print(f"hasil-2 :\n{hasil2}")
print(f"hasil-3 :\n{hasil3}")
print(f"hasil-4 :\n{hasil4}")
