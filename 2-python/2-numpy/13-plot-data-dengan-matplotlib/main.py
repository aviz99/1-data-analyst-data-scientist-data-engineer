# 23 / 10 / 2023
# Day - 32
# Plot Data Dengan Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# menginsatall matplotlib
# masuk ke terminal
# ketikan "pip install matplotlib"
# harus konek internet

# persamaan garis
# Y = 2 * x + 3

x_garis = np.arange(0, 11, 1)
y_garis = 2 * x_garis + 3
print(x_garis)
print(y_garis)

plt.figure(1)
plt.plot(x_garis, y_garis)
# plt.show()

# lingkaran
jari2 = 5
sudut = np.linspace(0, 2 * np.pi, 100)
x_ling = jari2 * np.cos(sudut)
y_ling = jari2 * np.sin(sudut)

plt.figure(2)
plt.plot(x_ling, y_ling)
plt.show()
