# 15 / 09 / 2023
# Day - 12
# Args Function

# def data_fisik(nama, tinggi, berat):
#     print(f"nama: {nama},\ntinggi: {tinggi},\nberat: {berat}")


# data_fisik("Asep", 180, 70)

# def data_fisik2(data_list):
#     data = data_list.copy()
#     nama = data[0]
#     tinggi = data[1]
#     berat = data[2]
#     print(f"nama: {nama},\ntinggi: {tinggi},\nberat: {berat}")


# data_fisik2(["Ucha", 190, 72])

# ini adalah *args
# def fungsi(*args):


def data_fisik3(*args):  # args mengembalikan tuples
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"Nama: {nama},\nTinggi: {tinggi},\nBerat: {berat}\n")


data_fisik3("Ucha", 190, 72)


# studi kasus
def tambah(*data):
    # args memiliki tipe data nya tuples dan tuples bisa diiterasikan
    nilai_awal = 0
    for nilai in data:
        nilai_awal += nilai
    return nilai_awal


hasil = tambah(10, 20, 30, 40, 50, 60, 70, 80, 90)
print(f"hasil nya: {hasil}")

hasil2 = tambah(10, 5, 15)
print(f"hasil nya: {hasil2}")
