# 11 / 09 / 2023
# Day - 8
# More On Lists

barang = ["kunci", "ember", "jaket", "ban", "mobil"]
print(barang)

# Beberapa method yang bisa digunakan untuk memanipulasi lists / arrays

# Append
barang.append("sepeda")
print(barang)

# Mengakses data
data = "Ini string"
print(data[1])

# Menggabung data
barang.extend("laptop")
print(barang)

# Menambahkan data berdasarkan posisi yang ditentukan
barang.insert(4, "charger")
print(barang)

# Menghitung jumlah data
jumlahMobil = barang.count("mobil")
print(jumlahMobil)

# Menghapus data
barang.remove("ban")
print(barang)

# Membalik data
barang.reverse()
print(barang)

stuff = barang.copy()
stuff.append("gelas")
print(stuff)
print(barang)
