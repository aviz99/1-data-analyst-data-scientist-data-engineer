# 20 / 10 / 2023
# Day - 30
# Manipulasi Matriks
import numpy as np

a = np.array(([1, 2, 3], [4, 5, 6]))

print(f"matrix a dengan ukuran: {a.shape}")
print(a)

# Transpose Matrix
# baris diubah jadi column
print(f"transpose matrix dari a:\n{a.transpose()}")
print(np.transpose(a))
print(a.T)

# Vector Baris / Flattern Array
# diubah secara horizontal
print(f"flatern matrix a:\n{a.ravel()}")
print(np.ravel(a))


# Reshape Matrix
# diubah secara dipotong-potong
# mengembalikan nilai yang sudah di-reshape
print(f"reshape matrix a:\n{a.reshape(3,2)}")
print(a.reshape(6, 1))

# Resize Matrix
# merubah seluruh matrix a nya
print(f"resize matrix a:")
a.resize(3, 2)
print(a)
print(f"matrix a dengan ukuran: {a.shape}")
