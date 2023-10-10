# 30 / 09 / 2023
# Day - 24
# OOP Magic Methods

# Magic Method


class Mangga:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # __repr__() = method untuk string tetapi belum diproduksi dan untuk debugging
    def __repr__(self):
        return f"Debug: {self.nama}\ndengan jumlah: {self.jumlah}"

    # __str__() = method untuk string tetapi sudah diproduksi
    def __str__(self):
        return f"Mangga: {self.nama}\ndengan jumlah: {self.jumlah}"

    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("mana lagi", 5)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)
