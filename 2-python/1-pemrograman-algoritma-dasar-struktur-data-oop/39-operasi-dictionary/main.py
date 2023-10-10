# 12 / 09 / 2023
# Day - 9
# Operasi Dictionary
# Operator Dictionary

dict_mhs = {
    "nama" : "Doddy Ferdiansyah",
    "umur" : 20,
    "nrp" : 202331001,
    "email" : "doddy@gmail.com",
    "jurusan" : "Teknik Informatika"
}

# Mengetahui panjang dari dict
PANJANGDICT = len(dict_mhs)
print(f"panjang dari dict mhs adalah : {PANJANGDICT}")

# Mengecek key ada atau tidak
KEY = "nama"
CHECKKEY = KEY in dict_mhs
print(f"apakah ada nama di data dict mhs : {CHECKKEY}")

# Mengakses value atau read dengan menggunakan get
print(dict_mhs.get("nrp"))
print(dict_mhs.get("kota","Tidak Ada")) # cek key dengan message error

# mengubah (update) value di data dict
# Cara normal
dict_mhs["nama"] = "Sandhika Galih"
print(dict_mhs)

# Cara sederhana
dict_mhs.update({"nama" : "Doddy Ferdiansyah"})
print(dict_mhs)

# menambahkan sebuah value di data dict
# Cara normal
dict_mhs["alamat"] = "Bandung"
print(dict_mhs)

# Cara sederhana
dict_mhs.update({"ipk" : 3.5}) # kalau tidak ada di add aja
print(dict_mhs)

# menghapus value di data dict
del dict_mhs["nrp"]
print(dict_mhs)