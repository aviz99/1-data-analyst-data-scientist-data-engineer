# 15 / 09 / 2023
# Day - 12
# Study Case 8 - Function

import os

# program menghitung luas & keliling persegi panjang


def header():
    """Fungsi Header"""
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")


def ambil_input_user():
    """Mengambil Input User"""
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))

    return lebar, panjang


def hitung_luas(lebar, panjang):
    """Menghitung Luas Persegi Panjang"""
    luas = lebar * panjang
    return luas


def hitung_keliling(lebar, panjang):
    """Menghitung Keliling Persegi Panjang"""
    keliling = 2 * (lebar + panjang)
    return keliling


def display(message, value):
    """tampilkan hasilnya"""
    print(f"hasil perhitungan {message} = {value}")


# Program Utama
while True:
    header()
    LEBAR, PANJANG = ambil_input_user()
    opsi = int(input("Pilih Hitung Persegi Panjang:\n1 LUAS\n2 KELILING: "))
    if opsi == 1:
        LUAS = hitung_luas(LEBAR, PANJANG)
        display("luas", LUAS)
    elif opsi == 2:
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("keliling", KELILING)

    apaLanjut = input("apakah anda ingin lanjut (y/n)? ")
    if apaLanjut == "n":
        break

print("Terima Kasih.")
