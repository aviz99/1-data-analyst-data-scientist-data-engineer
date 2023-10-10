# 09 / 09 / 2023
# Day - 6
# Control Flow Percabangan - ELIF Statement

# nama = input("Masukkan nama anda : ")

# if nama == "erik":  # Kondisi 1
    # print("Selamat Pagi, "+nama) # Aksi 1
# elif nama == "nofariza": # Kondisi 2
    # print("Selamat Malam, "+nama) # Aksi 2
# elif nama == "caca": # Kondisi 3
    # print("Ohayou Gozaimasu, "+nama) # Aksi 3
# elif nama == "jacquelyn": # Kondisi 4
    # print("Konbanwa, "+nama) # Aksi 4
# else: # aksi false
#     print("Anda bukan erik, nofariza, caca & jacquelyn")
# print("Program sudah berakhir")

# umur = int(input("Masukkan umur : "))

# if umur <= 10:
#     print("Anak-anak")
# elif umur <= 17:
#     print("Remaja")
# elif umur <= 50:
#     print("Dewasa")
# else:
#     print("Adi Yuswa")

# tekanan_darah = int(input("Masukkan tekanan darah anda : "))

# if tekanan_darah < 80:
#     print("Tekanan darah anda rendah")
# elif tekanan_darah <= 120:
#     print("Tekanan darah anda normal")
# else:
#     print("Tekanan darah anda tinggi")

# Nested ELSE
# tekanan_darah = int(input("Masukkan tekanan darah anda : "))

# if tekanan_darah < 80:
#     print("Tekanan darah anda rendah")
# else:
#     if tekanan_darah <= 120:
#         print("Tekanan darah anda normal")
#     else:
#         print("Tekanan darah anda tinggi")

# Nested IF
berat_badan = int(input("Masukkan berat badan anda : "))
tinggi_badan = int(input("Masukkan tinggi badan anda :"))

# syarat masuk polisi
if tinggi_badan > 170:
    print("Tinggi anda masuk kategori")
    if berat_badan > 80:
        print("Maaf anda terlalu berat")
    else:
        if berat_badan > 50:
            print("Berat badan anda masuk kategori")
        else:
            print("Maaf anda terlalu kurus")
else:
    print("Maaf anda tidak diterima")