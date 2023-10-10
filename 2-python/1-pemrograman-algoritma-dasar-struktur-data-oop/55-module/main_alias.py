# 20 / 09 / 2023
# Day - 16
# Module

from matematika import tambah as add
from matematika import kali as times
from matematika import pangkat as exp

# from matematika import *

import matematika as mathematics  # <---- bisa dilakukan juga

hasil_tambah = add(1, 2, 3, 4, 5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = mathematics.kali(1, 2, 3, 4, 5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = exp(3)
print(f"hasil pangkat 3 = {pangkat_3(3)}")
