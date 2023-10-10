# 15 / 09 / 2023
# Day - 12
# Global & Local Scope

# Variable Global
nama = "Ali"  # Variable Global Scope


# akses variable global dalam fungsi
def say_hi():
    print(f"Hai,my name is {nama}")


say_hi()

# akses variable global dalam loop
for i in range(0, 5):
    print(f"loop {i} - {nama}")

# percabangan
if True:
    print(f"if menampilkan {nama}")


# Variable Local Scope
def fungsi_local():
    nama_local = "Ali"  # <- Variable Local Scope


fungsi_local()
# print(nama_local) # tidak bisa diakses

# contoh 1: penggunaan akses variable


def say_name():
    print(f"Hello {nama}")


nama = "Ali"
say_name()

# contoh 2: merubah variable global
angka = 0


def ubah_angka(nilai_baru):
    global angka  # fungsi ini mendapat akses merubah angka
    angka = nilai_baru


print(f"Ini sebelum: {angka}")
ubah_angka(10)
print(f"Ini sesudah: {angka}")


# contoh 3:
angka = 0
for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)
