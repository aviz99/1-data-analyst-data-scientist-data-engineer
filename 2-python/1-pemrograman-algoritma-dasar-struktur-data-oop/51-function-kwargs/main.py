# 15 / 09 / 2023
# Day - 12
# Kwargs Function
def data_diri(**kwargs):  # mengembalikan dictionary dan mengambil data nya
    """fungsi dengan kwargs menghasilkan dictionary"""
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


data_diri(nama="asep", tinggi=183, berat=68)


# studi kasus
def math(*args, **kwargs):
    hasil = 0
    if kwargs["option"] == "tambah":
        for tambah in args:
            hasil += tambah
    elif kwargs["option"] == "kali":
        hasil = 1
        for kali in args:
            hasil *= kali
    else:
        print("Tidak ada operasi aritmatika")
    return hasil


hasil_tambah = math(1, 2, 3, 4, option="tambah")
print(f"hasil pertambahan: {hasil_tambah}")
hasil_kali = math(1, 2, 3, 4, option="kali")
print(f"hasil perkalian: {hasil_kali}")
