# 20 / 09 / 2023
# Day - 16
# Package
# Tempat untuk menyimpan program atau module - module kita

# import time

# t_start = time.time()
import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"hasil tambah: {hasil_tambah}")
hasil_kali = sains.matematika.kali(1, 2, 3, 4, 5)
print(f"hasil kali: {hasil_kali}")

# t_end = time.time()

# print(f"waktu big-O-Notation yang dieksekusi adalah: {t_end - t_start}")
gaya = fisika.gaya(90, 10)
print(f"gaya adalah: {gaya}")

style = force(90, 10)
print(f"gaya adalah: {style}")
