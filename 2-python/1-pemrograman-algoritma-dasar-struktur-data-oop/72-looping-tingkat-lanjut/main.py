# 24 / 09 / 2023
# Day - 20
# Looping Tingkat Lanjut

# range = dilakukan untuk melakukan iterasi for loop
for item in range(1, 20, 3):
    print(item)

# range bisa mengenerate sebuah list
angka = list(range(1, 11))
print(angka)

# enumerate = digunakan untuk menunjuk index pada sebuah item di for loop
# enumerate menghasilkan tipe data tuples
kata_kata = "abcdefghij"
for nilai in enumerate(kata_kata):
    print(nilai)

# tuples unpacking
for a, b in enumerate(kata_kata):
    print(a)
    print(b)

# zip = digunbakan untuk menggabungkan satu atau lebih list
list_satu = [1, 2, 3, 4, 5]
list_dua = ["a", "b", "c", "d", "e"]
list_tiga = [100, 200, 300, 400, 500]

for val in zip(list_satu, list_dua, list_tiga):
    print(val)

# menggabungkan dan membentuk sebuah list menggunakan zip
for val in zip(list_satu, list_tiga):
    print(list(val))

# item checking = cara untuk mengambil sebuah nilai boolean ketika mengecek sebuah item didalam sebuah list, tuples, dsb
ini_string = "aku belajar"
print(ini_string)
cek_string = "o" in ini_string
print(cek_string)

# item checking bisa dilakukan untuk berbagai macam tipe data termasuk dictionary
kotak_dict = {"a": 100, "b": 200, "c": 300}
cek_kotak = "a" in kotak_dict
print(f"apakah a ada di kotak_dict: {cek_kotak}")

# mengecek beradasarkan values nya
cek_kotak_val = 200 in kotak_dict.values()
print(f"apakah nilai 200 ada di kotak_dict: {cek_kotak_val}")

# advanced for loop
ini_list = list()
for i in range(1, 11):
    ini_list.append(i)

print(ini_list)

# membuat list dengan for loop yang sederhana
# list = [namaIterator for namaIterableValue in range(jumlahTerminasi)]
ini_list_dua = [item for item in range(1, 11)]
print(ini_list_dua)

ini_list_tiga = [item**2 for item in range(1, 11)]
print(ini_list_tiga)

ini_list_empat = [(item**2 / 3) for item in range(1, 11)]
print(ini_list_empat)

# list comprehension
ini_list_lima = [item for item in range(1, 21)]
print(ini_list_lima)

# list comprehension dengan if
ini_list_enam = [item for item in range(1, 21) if item % 2 == 0]
print(ini_list_enam)

# list comprehension dengan if else 1 baris
ini_list_tujuh = [item if item % 2 == 0 else "ganjil" for item in range(1, 21)]
print(ini_list_tujuh)

# menggunakan for loop dengan if else biasa
ini_list_delapan = []
for i in range(1, 21):
    if i % 2 == 0:
        ini_list_delapan.append(i)
    else:
        ini_list_delapan.append("ganjil")
print(ini_list_delapan)
