# 23 / 10 / 2023
# Day - 32
# Invers & Determinan
import numpy as np

# Invers Matrix
# jadi untuk membuktikan bahwa ini matrix invers atau bukan dilihat hasilnya adalah jika dikalikan matrix nya itu sendiri
# A, A**-1 = satuan
# atau hasil nya
# [
#   1   0
#   0   1
# ]
# matrix tidak semua nya punya invers
# Matrix Singular
# a = 0
# a**-1 = 1/0

a = np.array([(1, -1), (1, 1)])
print(a)

# invers matrix
a_inv = np.linalg.inv(a)
print(a_inv)
print(np.dot(a, a_inv))

# Determinan
# nilai dari si a nya
# determinan untuk sebuah matrix yang bisa di invers itu nilai nya akan bukan 0

a_det = np.linalg.det(a)
a_inv_det = np.linalg.det(a_inv)
print(a_det)
print(a_inv_det)

# digunakan untuk menyelesaikan persamaan linear
