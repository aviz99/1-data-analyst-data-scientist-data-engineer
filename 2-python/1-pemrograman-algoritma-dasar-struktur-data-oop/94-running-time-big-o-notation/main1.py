# 18 / 09 / 2023
# Day - 15
# Running Time & Big O-Notation

# Pada kasus kali ini kita akan melakukan loop sebuah nilai yang terkait dengan Big O notation
import time

val = 1000
val_sepuluh_ribu = 10000

start_time = time.time()

start_val = 0
for value in range(val_sepuluh_ribu):
    for nilai in range(val_sepuluh_ribu):
        start_val += 0

end_time = time.time()

lama_waktu = end_time - start_time
print("elapsed %s seconds ..." % lama_waktu)


# def hitung_angka(a, b):
#     return a + b


# print(f"Hasil nya: {hitung_angka(5,5)}")
