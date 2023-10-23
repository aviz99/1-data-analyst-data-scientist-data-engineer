# 18 / 10 / 2023
# Day - 29
# Indexing, Slicing & Iteration

import numpy as np

a_array_biasa = np.arange(10) ** 2
print(a_array_biasa)

# mengambil nilai
print(f"elemen ke-1 dari a adalah: {a_array_biasa[0]}")
print(f"elemen ke-7 dari a adalah: {a_array_biasa[6]}")
print(f"elemen terakhir dari a adalah: {a_array_biasa[-1]}")

# slicing
print(
    f"elemen dari 1 sd 6 adalah: {a_array_biasa[0:6]}"
)  # exclusive dia mengambil dari nilai awal sampai nilai sebelum akhir
print(f"elemen dari ke-4 sd terakhir: {a_array_biasa[3:]}")
print(f"elemen dari awal sd ke-5: {a_array_biasa[:5]}")

# iteration
for i in a_array_biasa:
    print(f"value: {i}")

# bilangan distrbusi uniform (0-1)
b_bil_acak = np.random.rand(4)

# bilangan distrbusi uniform (0-1) matriks 2 dimensi
b_bil_acak_matriks2D = np.random.rand(5, 4)

print(b_bil_acak)
print("\n")
print(b_bil_acak_matriks2D)
print("\n")

# bilangan distrbusi normal (gaussian)
c_bil = np.random.randn(10)

# bilangan distrbusi normal (gaussian) matriks 2 dimensi
c_bil_matriks2D = np.random.randn(4, 4)

print(c_bil)
print("\n")
print(c_bil_matriks2D)

# cara cepat
# from numpy.random import rand, randn, randint
# randn(6,2)
# randint(awal,akhir,nilaiYgInginDikeluarkan)
