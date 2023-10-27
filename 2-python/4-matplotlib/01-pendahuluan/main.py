# 27 / 10 / 2023
# Day - 36
# Matplotlib Pendahuluan

# Matplotlib adalah sebuah library dipython digunakan untuk visualisasi
# sebuah grafis data

import matplotlib.pyplot as plt
import numpy as np

# print(plt.plot([10,20,30,40,50]))

x = [10,20,30,40,50]
y = np.array(x)**2

print(plt.plot(x, y))

# mendapatkan informasi tambahan
print(plt.xlabel("Sumbu X"))
print(plt.ylabel("Sumbu Y"))
print(plt.title("Judul Grafik"))

# membuat 2 grafik berdampingan
# print(plt.subplot(baris, kolom, plot ke berapa))
print(plt.subplot(121))
print(plt.plot(x, y, color="red"))
print(plt.xlabel("Sumbu X1"))
print(plt.ylabel("Sumbu Y1"))

print(plt.subplot(122))
print(plt.plot(y, x, color="blue"))
print(plt.ylabel("Sumbu Y2"))
print(plt.xlabel("Sumbu X2"))
print(plt.tight_layout())