# 20 / 10 / 2023
# Day - 30
# Stacking Matrix
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a_matrix = np.zeros((2, 3))
# a_matrix_warn = np.zeros((2, 2)) # tidak bisa harus sama ukuran matrix nya
b_matrix = np.ones((2, 3))

# Stacking Matrix Horizontal
# c = np.hstack((depanMatrix,belakangMatrix))
c = np.hstack((a, b))

# Stacking Matrix Vertical
# d = np.vstack((atasMatrix,bawahMatrix))
d = np.vstack((a, b))

c_matrix = np.hstack((a_matrix, b_matrix))
# c_matrix_warn = np.hstack((a_matrix_warn, b_matrix))
d_matrix = np.vstack((a_matrix, b_matrix))
# d_matrix_warn = np.vstack((a_matrix_warn, b_matrix))

print(c)
print(d)
print(c_matrix)
# print(c_matrix_warn)
print(d_matrix)
# print(d_matrix_warn)
