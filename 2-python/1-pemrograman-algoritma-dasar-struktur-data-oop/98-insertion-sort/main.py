# 12 / 10 / 2023
# Day - 27
# Insertion Sort
# Insertion Sort adalah membandingkan data kedua dengan data pertama berdasarkan data yang paling rendah
# apabila data kedua lebih kecil maka tukar posisi
# begitu seterusnya sampai tidak ada lagi data yang dapat dipindahkan


def insertion_sort(data):
    # Insertion Sort Descending
    # validasi nilai
    # for i in range(len(data) - 1, -1, -1):
    # value = data[i]
    # data yang ingin diinsertion sort kan
    # hole = i
    # validasi data membandingkan data yang paling rendah
    # while hole < (len(data) - 1) and data[hole + 1] > data[hole]:
    #     data[hole] = data[hole + 1]
    #     hole = hole + 1
    #     data[hole] = value
    # print(data)

    # Insertion Sort Ascending
    for j in range(len(data) - 1, -1, -1):
        nilai = data[j]
        # data yang ingin diinsertion sort kan
        isi_data = j
        # validasi data membandingkan data yang paling rendah
        while isi_data < (len(data) - 1) and data[isi_data + 1] < data[isi_data]:
            data[isi_data] = data[isi_data + 1]
            isi_data = isi_data + 1
            data[isi_data] = nilai
        print(data)


angka = [2, 54, 38, 76, 23, 56, 84, 90]

print("Data yang akan disort:\n{}".format(angka))
# print("\nInsertion Sort Descending:")
# insertion_sort(angka)
print("\nInsertion Sort Ascending:")
insertion_sort(angka)
