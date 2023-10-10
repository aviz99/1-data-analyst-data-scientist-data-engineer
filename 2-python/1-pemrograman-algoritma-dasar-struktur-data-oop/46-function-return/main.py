# 14 / 09 / 2023
# Day - 11
# Function Return

# template function with return
# def nama_fungsi(argument):
#       badan fungsi / aksi
#       return output


# fungsi kuadrat
# def kuadrat(x):
#     output = x**2
#     return output

# y = kuadrat(5)
# print(y)

# print(kuadrat(6))

# z = 10 + kuadrat(7)
# print(z)


# fungsi tambah
# def tambah_bil(a, b):
#     return a + b

# hasil = tambah_bil(10, 8)
# print(hasil)


# fungsi dengan return banyak
def operasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi


tam, kur, kal, bag = operasi_matematika(9, 5)
print(f"Hasil tambah = {tam}")
print(f"Hasil kurang = {kur}")
print(f"Hasil kali = {kal}")
print(f"Hasil bagi = {bag}")
