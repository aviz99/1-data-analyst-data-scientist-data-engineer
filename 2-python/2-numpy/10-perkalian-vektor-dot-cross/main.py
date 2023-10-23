# 23 / 10 / 2023
# Day - 32
# Perkalian Vektor Dot & Cross
import numpy as np

a_dot = np.array([1, 3])
b_dot = np.array([2, 1])

# perkalian dot
c_dot = np.dot(a_dot, b_dot)
print(c_dot)

# perkalian cross
a_cross = np.array([1, 2, 0])
b_cross = np.array([2, 1, 0])

c_cross1 = np.cross(a_cross, b_cross)
c_cross2 = np.cross(b_cross, a_cross)
print(c_cross1)
print(c_cross2)
