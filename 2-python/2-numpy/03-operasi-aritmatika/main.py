# 17 / 10 / 2023
# Day - 28
# Operasi Aritmatika

import numpy as np

# list python
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

# array numpy
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([6, 7, 8, 9, 10])

# elementwise operation
# operasi nya itu perelemen

# penjumlahan
tambah_list = list_a + list_b
tambah_array = array_a + array_b

# pengurangan
# kurang_list = list_a - list_b # tidak bisa dioperasikan
kurang_array = array_a - array_b

# perkalian
# kali_list = list_a * list_b # tidak bisa dioperasikan
kali_array = array_a * array_b

# pembagian
# bagi_list = list_a / list_b # tidak bisa dioperasikan
bagi_array = array_a / array_b

# kuadrat
# kuadrat_list = list_a**2 # tidak bisa dioperasikan
kuadrat_array = array_a**2

print(f"penjumlahan list:\n{tambah_list}")
print(f"penjumlahan array:\n{tambah_array}")
# print(f"pengurangan list:\n{kurang_list}") # tidak bisa dioperasikan
print(f"pengurangan array:\n{kurang_array}")
# print(f"perkalian list:\n{kali_list}") # tidak bisa dioperasikan
print(f"perkalian array:\n{kali_array}")
# print(f"pembagian list:\n{bagi_list}") # tidak bisa dioperasikan
print(f"pembagian array:\n{bagi_array}")
# print(f"kuadrat list:\n{kuadrat_list}")  # tidak bisa dioperasikan
print(f"kuadrat array:\n{kuadrat_array}")


# multidimensi
array_c = np.array(([1, 2, 3], [4, 5, 6]))
array_d = np.array(([7, 8, 9], [-1, -2, -3]))

hasil_multidimensi = array_c + array_d
print(f"array multidimensi:\n{hasil_multidimensi}")
