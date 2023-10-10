# 05 / 10 / 2023
# Day - 25
# Package Numpy PIP
# package operasi matematika matriks
# kegunaan nya adalah bisa membuat matriks
import numpy as np

list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

# matriks sederhana
print(f"list_a: {list_a}")
# print(list_a**2)
print(f"vector a: {vector_a}")
print(f"vector a kuadrat 2: \n{vector_a**2}")
print(f"vector a kali 5: \n{vector_a * 5}")

# matriks 2 dimensi
matrix_b = np.array([(1, 2), (3, 4)])
print(f"matrix b: \n{matrix_b}")
print(f"matrix b kuadrat 2: \n{matrix_b**2}")

# matriks zeros / matriks kosong
zeros_c = np.zeros((2, 2))
print(f"matriks zeros c: \n{zeros_c}")

# matriks ones / satu matriks satu
ones_d = np.ones((2, 2))
print(f"matriks ones d: \n{ones_d}")

# menjumlahkan seluruh matriks / melakukan operasi matriks
jumlah = matrix_b + matrix_b**2 + ones_d
print(jumlah)
