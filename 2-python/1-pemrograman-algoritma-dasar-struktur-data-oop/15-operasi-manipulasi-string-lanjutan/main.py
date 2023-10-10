# 07/09/2023
# Day - 4
# Operasi manipulasi string lanjutan

# Operator dalam bentuk methods

# A. merubah case dari string
# merubah semua ke uppercase
salam = "bro!"
print("normal = "+ salam)
salam = salam.upper()
print("uppercase = "+ salam)

# merubah semua ke lowercase
sayHi = "HAI"
print("uppercase = "+ sayHi)
sayHi = sayHi.lower()
print("lowercase = "+ sayHi)

# B. pengecekkan dengan menggunakan is
# pengecekan dengan menggunakan islower() & isupper()
sayHello = "hello"
cek_lower = sayHello.islower() # hasilnya bool
print(sayHello + " is lower = " + str(cek_lower))
cek_upper = sayHello.isupper() # hasilnya bool
print(sayHello + " is upper = " + str(cek_upper))
cek_upper = sayHello.isidentifier() # hasilnya bool
print(sayHello + " is string = " + str(cek_upper))

# isalpha() => untuk mengecek apakah semua nya huruf
# isnum() => untuk mengecek angka / numerik & huruf
# isdecimal() => untuk mengecek apakah semua nya angka / numerik
# isspace() => untuk mengecek spasi, tab, newline
# istitle() => untuk mengecek semua kata dimulai dengan huruf besar

judul = "It Is okay Not To be Okay"
cek_judul = judul.istitle() # hasilnya bool
print(judul + " is title = " + str(cek_judul))

# C. ngecek komponen startswith() & endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))
cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

# C. penggabungan komponen join() & split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ':'.join(pisah)
print(gabung)

gabung = '|'.join(pisah)
print(gabung)

gabung = '!'.join(pisah)
print(gabung)

gabungan = "aku:sayang:kamu"
print(gabungan.split(":"))

# D. alokasi karakter rjust(), ljust(), center()
kanan = "Nofariza".rjust(10)
print("'"+kanan+"'")

kiri = "Dimas".ljust(10)
print("'"+kiri+"'")

tengah = "Erik".center(20,"=")
print("'"+tengah+"'")

# kebalikannya => strip()
tengahCoy = tengah.strip("=") # menghilangkan / menghapus tanda (=)
print("'"+tengahCoy+"'")
kananCoy = kanan.strip()
print("'"+kananCoy+"'")