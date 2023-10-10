# 12 / 09 / 2023
# Day - 9
# Sets & Tuples

# Tuples
# Data Tuples tidak bisa diubah dan tidak bisa di manipulasi
# Digunakan untuk mengambil dan mengirimkan dari data tertentu secara konstan

data_tuples = (7, 8, 9, 10)
print(f"Ini Tuples : {data_tuples}")
# indexing pada tuples
print(f"Data Tuples : {data_tuples[1]}")
# merubah isi dari sebuah tuples

# re-assignment array  / merombak ulang isi tuples
data_tuples_ubah = data_tuples[0], data_tuples[1], "mangga", data_tuples[3]
print(f"Data Tuples yang diubah: {data_tuples_ubah}")

# merubah kedalam list
data_list = list(data_tuples)
print(data_list)
data_list[1] = "bayam"
print(f"Data Tuples yang diubah ke list: {data_list}")
data_tuples_baru_ubah = tuple(data_list)
print(f"Data Lists yang diubah ke tuples: {data_tuples_baru_ubah}")

# methods pada tuples
ini_tuples = (1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 5, 4, 6)
# menghitung isi item pada tuples
jml_tuples = ini_tuples.count(3)
print(f"jumlah angka 3 pada ini tuples: {jml_tuples}")
# melihat index nya
idx_tuples = ini_tuples.index(4)
print(f"index angka 4 pada ini tuples: {idx_tuples}")
# multiple assignment & tuples = kita bisa mengisikan beberapa variable sekaligus hanya dalam sekali perintah atau 1 baris
a, b, c, d = 1, 2, 3, 4
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")

e, f, g, h = "asik"
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")
print(f"h: {h}")

a, b = 1, 2
a, b = b, a
print(f"a: {a}")
print(f"b: {b}")

bag = ("rambutan", 41, 9.5, [1, 2, 3, 4, 5], True)
print(f"bag: {bag}")
item1, item2, item3, item4, item5 = bag
print(f"item 1: {item1}")
print(f"item 2: {item2}")
print(f"item 3: {item3}")
print(f"item 4: {item4}")
print(f"item 5: {item5}")
print(f"tipe data item 1: {type(item1)}")
print(f"tipe data item 2: {type(item2)}")
print(f"tipe data item 3: {type(item3)}")
print(f"tipe data item 4: {type(item4)}")
print(f"tipe data item 5: {type(item5)}")

# Sets (Himpunan) = sebuah tipe data untuk elemen yang bersifat unique (tanpa duplikasi) dan tidak berurutan
# Data collection yang tidak memiliki sebuah index
# Sets tidak bisa memiliki data yang sama
data_sets = {10, 4, 3, 2, 4, 7, 6, 5}
print(f"Ini Sets : {data_sets}")
data_sets.add("ayam")
data_sets.add("sapi")
data_sets.add("bebek")
print(f"Sets : {data_sets}")

# mengubah data ke sets
list_ku = [
    "singa",
    "gajah",
    "harimau",
    "rusa",
    "badak",
    "singa",
    "singa",
    "gajah",
    "rusa",
    "rusa",
    "rusa",
]
print(f"Listku: {list_ku}")
sets_ku = set(list_ku)
print(f"Listku ubah jadi sets: {sets_ku}")
