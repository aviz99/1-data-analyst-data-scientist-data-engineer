# 17 / 10 / 2023
# Day - 28
# NumPy Array

import numpy as np

# membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

# vector range
# untuk membedakan range python dengan range numpy
# c = np.arange(batasBawah, batasAtas, langkahStep)
c = np.arange(1, 10, 2)

# linear space / linspace
# kita bagi
# d = np.linspace(batasAwal, batasAkhir, mauDibagiBerapa)
d = np.linspace(1, 10, 4)

# array multidimensi / matriks
e = np.array([(1, 2, 3), (4, 5, 6)])

# matriks nol
f = np.zeros((5, 5))

# matriks nilai satu
g = np.ones((5, 5))

# matriks identitas
h1 = np.identity(5)
h2 = np.eye(5)

print(f"vector array:\n{a}")
print(f"vector array dengan desimal:\n{b}")
print(f"vector range:\n{c}")
print(f"linspace:\n{d}")
print(f"matriks:\n{e}")
print(f"matriks nilai 0:\n{f}")
print(f"matriks nilai 1:\n{g}")
print(f"matriks identitas identity:\n{h1}")
print(f"matriks identitas eye:\n{h2}")
