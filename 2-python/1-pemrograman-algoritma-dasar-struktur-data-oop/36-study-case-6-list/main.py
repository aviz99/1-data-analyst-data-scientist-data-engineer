# 12 / 09 / 2023
# Day - 9
# Study Case 6 - List

# program daftar buku
print(5*"-"+"DAFTAR BUKU"+5*"-")
daftar_buku = []
while True:
    print("\nMasukkan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul, penulis]
    daftar_buku.append(buku_baru)
    
    print("\n\n","="*10,"DATA BUKU","="*10)
    for index,book in enumerate(daftar_buku):
        print(f"{index+1} | {book[0]} | {book[1]}")

    print("\n\n","="*20)
    # Keluar dari program
    isLanjut = input("Apakah anda ingin menambahkan ?(y/n)")

    if isLanjut == "n":
        break

print("TERIMA KASIH.")