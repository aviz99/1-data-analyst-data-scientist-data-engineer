# 09 / 10 / 2023
# Day - 26
# OOP Polymorphism & Dunder Method

# Polymorphism = Teknik di OOP dimana kita bisa menggunakan beberapa fitur dari beberapa class ke dalam sebuah fungsi atau ke dalam sebuah class lain
# dimana fungsi itu memiliki karakter dari object yang dia pakai


class Kucing:
    def __init__(self, nama):
        self.nama = nama

    def respon(self):
        return self.nama + " Meong-meong!"


class Anjing:
    def __init__(self, nama):
        self.nama = nama

    def respon(self):
        return self.nama + " Guk-guk!"


cimol = Kucing("Cimol")
bleki = Anjing("Bleki")

print(cimol.respon())
print(bleki.respon())

for binatang in [cimol, bleki]:
    print(type(binatang))
    print(binatang.respon())


def hewan_ngomong(binatang):
    print(binatang.respon())


hewan_ngomong(cimol)
hewan_ngomong(bleki)


# Dunder Method / Magic Method
# method yang memungkinkan digunakan oleh object bersangkutan
class Coba:
    def __init__(self, nama, angka, kata):
        self.nama = nama
        self.angka = angka
        self.kata = kata

    def cetak(self):
        return self.nama

    def __str__(self):
        return self.nama

    def __len__(self):
        return 100


coba = Coba("joko", 20, "sehat")
print(coba.cetak())

# Dunder Method
print(dir(coba))

print(coba.__str__())
print(str(coba))

print(coba.__len__())
print(len(coba))
