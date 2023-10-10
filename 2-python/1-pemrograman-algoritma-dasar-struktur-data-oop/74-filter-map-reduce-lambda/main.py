# 25 / 09 / 2023
# Day - 21
# Filter, Map & Lambda


# map
def kali(num):
    return num * 10


print(kali(35))

angka = [2, 4, 6]
for i in map(kali, angka):
    print(i)

simpan_list = list(map(kali, angka))
print(simpan_list)

# map pada tuples
angka_tuples = (31, 61, 91)
print(angka_tuples)
simpan_tuples = tuple(map(kali, angka_tuples))
print(simpan_tuples)


# map pada string
# map menghasilkan string atau variable integer float
def jumlahKata(kata):
    if len(kata) % 2 == 0:
        return "INI ANGKA GENAP"
    else:
        return "INI ANGKA GANJIL"


print(jumlahKata("abcdefghijklmnopqrstuvwxyz"))

list_kata = ["anggi", "norman", "nindy"]
print(list_kata)
list_kata_map = list(map(jumlahKata, list_kata))
print(list_kata_map)


# filter
# filter menghasilkan boolean
def cekGenap(num):
    return num % 2 == 0


print(cekGenap(8))

nomor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nomor)
cek_nomor_genap = list(filter(cekGenap, nomor))
print(cek_nomor_genap)

for item in filter(cekGenap, nomor):
    print(item)

# lambda expression
ini_lambda_fungsi = lambda bilangan: bilangan**2
print(ini_lambda_fungsi(6))

pangkat_lambda = list(map(lambda x: x**2, angka))
print(pangkat_lambda)

genap_lambda = list(filter(lambda num: num % 2 == 0, nomor))
print(genap_lambda)
