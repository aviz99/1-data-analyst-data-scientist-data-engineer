# 24 / 09 / 2023
# Day - 20
# String Slicing

# string kumpulan karakter yang terurut artinya string memiliki index yang bisa diambil

bil1 = 3.5
print(bil1)

# mengecek tipe data
tipe_bil = type(bil1)
print(tipe_bil)

# melakukan pembagian
bil2 = bil1 / 17
print(bil2)
tipe_bil_2 = type(bil2)
print(tipe_bil_2)

# melakukan modulus %
bil_mod = 13 % 8
print(f"hasil nya: {bil_mod}")

# melakukan perpangkatan / exponential
bil_exp = 9**4
print(f"hasil nya: {bil_exp}")

# melakukan operasi aritmatika gabungan
bil_op_math = 2 + 10 * 3 + 4 * 8 + 5
print(f"hasil penggabungan operator aritmatika adalah: {bil_op_math}")
bil_op_math_2 = (2 + 10) * (3 + 4) * (8 + 5)
print(f"hasil penggabungan operator aritmatika kedua adalah: {bil_op_math_2}")

# indexing & slicing
item_saya = ["ikan", "ayam", "bebek"]
print(f"item saya: {item_saya}")

# indexing
print(f"index ke-2 adalah: {item_saya[2]}")

# indexing pada string
indexing_str = "Belajar Python Itu Mudah"
print(f"index : {indexing_str[2]}")

# slicing pada string
print(f"index : {indexing_str[1:5]}")
# bila diikutkan semua
print(f"index : {indexing_str[:]}")
# [awal:akhir:jarak]
print(f"index : {indexing_str[2:-1:2]}")
# indexing mundur / reverse
print(f"index : {indexing_str[::-1]}")
# slicing pada list
item_ku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(item_ku)
# indexing dari awal sampai akhir
print(item_ku[3::3])
