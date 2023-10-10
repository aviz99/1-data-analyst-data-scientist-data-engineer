# 14 / 09 / 2023
# Day - 11
# Study Case 7 - Dictionary

# Membuat program input dari user menggunakan dictionary
# fromkeys

# Cara mengotomatis tampilan hasil output program hilang
# os

import datetime
import os
import string
import random

# template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks lulus':0,
    'lahir':datetime.datetime(1111,11,11)
}

# membuat dictionary baru
# data kosong
data_mahasiswa = {}

# input data mahasiswa
while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    # mengambil data dari user
    # membuat dictionary kosong dengan menggunakan key dari dictionary mahasiswa template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks lulus'] = int(input("SKS Lulus: "))
    tahun_lahir = int(input("Tahun Lahir (YYYY): "))
    bulan_lahir = int(input("Bulan Lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal Lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)

    # key selalu update tidak me-replace data yang lama (mengenerate key yang berbeda)
    NOKEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    # memasukkan data yang sudah dibuat ke dalam data mahasiswa
    data_mahasiswa.update({NOKEY:mahasiswa})

    # Header
    print(f"{'No.':<5} {'Nama':<20} {'NIM':^9} {'SKS Lulus':^10} {'Lahir':<10}")
    print(58*"-")

    for mahasiswa in data_mahasiswa:
        NOKEY = mahasiswa

        nama = data_mahasiswa[NOKEY]['nama']
        nim = data_mahasiswa[NOKEY]['nim']
        sks_lulus = data_mahasiswa[NOKEY]['sks lulus']
        lahir = data_mahasiswa[NOKEY]['lahir'].strftime("%x")

        print(f"{NOKEY:<5} {nama:<20} {nim:^9} {sks_lulus:^10} {lahir:<10}")

    print("\n")
    # mengecek apakah ingin lanjut atau tidak
    is_done = input("Tambah lagi (y/n)? ")
    if is_done == "n":
        break
print("\nTERIMA KASIH.")