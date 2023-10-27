# 27 / 10 / 2023
# Day - 36
# Visualisasi Matplotlib Dengan OOP
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 20, 0.5)
y = x**2
print(x)
print(y)

# versi Matplotlib OOP

# versi 1
fig1 = plt.figure() # OOP
# axes = fig.add_axes([left, bottom, width, height])
# 0.1 = 10%
axes1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8]) # OOP
print(fig1)
print(axes1.plot(x, y))
print(axes1.set_xlabel("Sumbu X"))
print(axes1.set_ylabel("Sumbu Y"))
print(axes1.set_title("Judul Grafik"))

# menambahkan axes
fig2 = plt.figure()
axes2 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
axes3 = fig2.add_axes([0.2, 0.5, 0.3, 0.3])
print(fig2)
print(axes2.plot(x, y, color="red"))
print(axes2.set_xlabel("Sumbu X Besar"))
print(axes2.set_ylabel("Sumbu Y Besar"))
print(axes2.set_title("Judul Grafik Utama"))

print(axes3.plot(y, x, color="blue"))
print(axes3.set_ylabel("Sumbu Y Kecil"))
print(axes3.set_xlabel("Sumbu X Kecil"))
print(axes3.set_title("Judul Grafik Kecil"))

# versi 2
# fig3, axes4 = plt.subplots(nrows,ncols)
fig3, axes4 = plt.subplots(1, 2) # tuple unwrapping

# Plot for the first axes
print(axes4[0].plot(x, y, color="yellow"))
print(axes4[0].set_xlabel("Sumbu X1"))
print(axes4[0].set_ylabel("Sumbu Y1"))
print(axes4[0].set_title("Judul 1"))

# Plot for the second axes
print(axes4[1].plot(y, x, color="green"))
print(axes4[1].set_xlabel("Sumbu X2"))
print(axes4[1].set_ylabel("Sumbu Y2"))
print(axes4[1].set_title("Judul 2"))

# print(fig3, axes4)
print(plt.tight_layout())











