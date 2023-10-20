# 20 / 10 / 2023
# Day - 30
# Cara Advance Membuat Array
import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array(([1, 2, 3], [3, 4, 5]), dtype=float)


# membuat matrix dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2


def jumlah(baris, kolom):
    return kolom + baris


# b = np.fromfunction(fungsi, ukuranMatrix, tipe)
b = np.fromfunction(kuadrat, (1, 10), dtype=int)
c = np.fromfunction(jumlah, (4, 4), dtype=float)

# membuat array atau matrix dengan menggunakan iteration / iterable
iterable1 = (x * x for x in range(5))
iterable2 = (x * 2 for x in range(5))
d1 = np.fromiter(iterable1, dtype=int)
d2 = np.fromiter(iterable2, dtype=int)

# multitype array
# dtipe = [("nama","str-ukuran"),("tinggi", tipeData)]

dtipe = [("nama", "S255"), ("tinggi", int)]

data = [("ucup", 150), ("otong", 160), ("mario", 180)]

e = np.array(data, dtype=dtipe)

print(a)
print(b)
print(c)
print(d1)
print(d2)
print(e)
