# 17 / 10 / 2023
# Day - 28
# NumPy Array

import numpy as np

# membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

# vector range
# untuk membedakan range python dengan range numpy
# vector arange adalah mengenerate atau membuat array atau matrix atau vector dimana angka awal nya dan angka akhir nya bisa kita tentukan
# c = np.arange(batasBawah, batasAtas, langkahStep)
c = np.arange(1, 10, 2)

# linear space / linspace
# linspace / linear space adalah sebuah array 1 dimensi atau matrix 1 dimensi yang bisa kita tentukan dari awal sampai akhir dan jarak nya sama besar nya sebanyak angka yang kita tentukan
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
# sebuah matriks 2 dimensi matriks persegi dimana jumlah baris dan kolom nya sama
# dan matriks persegi ini ada sebuah angka diagonal dan nilai diagonal nya adalah 1
# semua matriks yang dikalikan dengan matriks identitas maka matriks nya tidak akan berubah
# artinya matriks nya tetap sama
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
