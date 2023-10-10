# 15 / 09 / 2023
# Day - 12
# Anonymous & Lambda Function


def f_angka(angka):
    return angka**2


# lambda function / lambda expression
# cara 1
# data = lambda argument: expression/aksi
kuadrat = lambda angka: angka**2
print(kuadrat(5))

# cara 2
pangkat = lambda num, pow: num**pow
print(pangkat(4, 2))

# kegunaan

# sorting list
data_list = ["Luffy", "Naruto", "Saitama", "Ichigo", "Deku"]
data_list.sort()
print(data_list)


# sorting berdasarkan panjang
# data_list.sort(key=method)
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(data_list)


# sorting menggunakan lambda function
data_list = ["Luffy", "Naruto", "Saitama", "Ichigo", "Deku"]
data_list.sort(key=lambda nama: len(nama))
print(data_list)


# filtering
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def kurang_dari_lima(angka):
    return angka < 5


# data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x: x < 7, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x: (x % 2 == 1), data_angka))
print(data_ganjil)

# kasus kelipatan 3
data_kel_tiga = list(filter(lambda x: (x % 3 == 0), data_angka))
print(data_kel_tiga)


# anonymous function
# currying <- Haskell Curry
def pangkat_aja(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat_aja(5, 2)
print(data_hasil)


# dengan currying
def pangkat_mulu(n):
    return lambda angka: angka**n


pangkat2 = pangkat_mulu(2)
print(pangkat2(50))
pangkat3 = pangkat_mulu(3)
print(pangkat2(100))
print(pangkat_mulu(4)(5))
