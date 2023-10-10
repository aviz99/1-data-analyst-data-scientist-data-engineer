# 21 / 09 / 2023
# Day - 16
# Exception, Error, Try & Except
# Kita akan menghandle atau mengkendalikan error runtime

# data_input = int(input("masukkan angka: "))
# hasil = 10 / data_input
# print(hasil)
# file = open("data.txt", "r")

# exception akan terjadi saat program mengalami error saat
# runtime

# contoh sederhana untuk menangkap exception
# try:
#       aksi

from math import nan

## contoh sederhana
# data_input = int(input("masukkan angka: "))
# hasil = nan

# try:
#     hasil = 10 / data_input
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

# contoh di aplikasi

while True:
    angka = int(input("masukkan angka pembagi: "))
    try:
        hasil = 10 / angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)?")
        if is_done == "n":
            break
    except:
        print("pembagi nol, silahkan masukkan input lagi")

print("Terima Kasih Program 1.")

# contoh aplikasi kedua untuk membuat data file data.txt
try:
    with open("data.txt", "r") as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("file baru")

print("Terima Kasih Program 2.")
