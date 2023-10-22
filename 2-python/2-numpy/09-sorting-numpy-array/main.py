# 22 / 10 / 2023
# Day - 31
# Sorting Numpy Array

import numpy as np

# me-generate nilai atau angka secara acak di numpy
a = np.floor(np.random.randn(1, 6) * 10)
print(a)

# mencari nilai terkecil dan terbesar di numpy
print(f"nilai max dari a: {a.max()}")
print(f"posisi max dari a: {a.argmax()}")
print(f"nilai min dari a: {a.min()}")
print(f"posisi min dari a: {a.argmin()}")

# mensorting nilai di numpy
print(f"mengurutkan nilai a:\n{np.sort(a)}")
# mensorting secara argument
print(np.argsort(a))
print("\n")

# me-generate nilai atau angka secara acak di numpy
b = np.floor(np.random.randn(2, 2) * 10)
print(b)

# mencari nilai terkecil dan terbesar di numpy
print(f"nilai max dari b: {b.max()}")
print(f"posisi max dari b: {b.argmax()}")
print(f"nilai min dari b: {b.min()}")
print(f"posisi min dari b: {b.argmin()}")

# mensorting nilai di numpy
print(f"mengurutkan nilai b:\n{np.sort(b)}")
# mensorting secara argument
print(np.argsort(b))
print("\n")

dtipe = [("nama", "S10"), ("tinggi", int)]
data = [("Ucup", 170), ("Otong", 150), ("Mario", 160)]
c = np.array(data, dtype=dtipe)
print(c)
# mengurutkan berdasarkan tinggi
print(np.sort(c, order="tinggi"))
# mengurutkan berdasarkan nama
print(np.sort(c, order="nama"))
