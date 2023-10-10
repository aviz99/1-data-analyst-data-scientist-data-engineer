# 20 / 09 / 2023
# Day - 16
# __init__
# Satu file bersama dengan package

import sains
from sains.matematika import scientific


hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah: {hasil_tambah}")

hasil_kali = sains.matematika.kali(1, 2, 3, 4, 5)
print(f"Hasil kali: {hasil_kali}")

pangkat_exp = scientific.pangkat(3)
print(f"Hasil pangkat: {pangkat_exp(5)}")

hasil_fisika = sains.fisika.gaya(10, 9.8)
print(f"Hasil gaya: {hasil_fisika}")

# from sains import *

# hasil_tambah = matematika.basic.tambah(1, 2, 3, 4, 5)
# print(f"Hasil tambah: {hasil_tambah}")

# hasil_kali = matematika.basic.kali(1, 2, 3, 4, 5)
# print(f"Hasil kali: {hasil_kali}")

# hasil_fisika = fisika.gaya(10, 9.8)
# print(f"Hasil gaya: {hasil_fisika}")
