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

# untuk mengetahui angka maksimal berdasarkan index
coba_1D = np.random.randint(0, 100, 20)
coba_2D = np.random.randint(0, 100, 20).reshape(4, 5)

print("\n")
print(coba_1D)
print("\n")
print(coba_2D)
print("\n")

# max()
print(coba_1D.max())
print(coba_2D.max())

# min()
print(coba_1D.min())
print(coba_2D.min())

# mengetahui sebuah index nya
print(coba_1D.argmax())
print(coba_2D.argmax())

print(coba_1D.argmin())
print(coba_2D.argmin())
print("\n")

# mengetahui dimensi array atau matriks
print(coba_1D.shape)
print(coba_2D.shape)
print("\n")

# mengetahui tipe data matriks atau array
print(coba_1D.dtype)
print("\n")

d_bil_matriks_2D = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

print(d_bil_matriks_2D)
print(d_bil_matriks_2D[0][0])
print(d_bil_matriks_2D[1])
print(d_bil_matriks_2D[2][2])
print(d_bil_matriks_2D[2, 2])
print(d_bil_matriks_2D[1:2, 1:])

# slicing dengan boolean di Numpy
e_bil_matriks = np.arange(1, 11)
print(e_bil_matriks)
print("\n")
print(f"boolean matriks bernilai:\n{e_bil_matriks > 5}")
