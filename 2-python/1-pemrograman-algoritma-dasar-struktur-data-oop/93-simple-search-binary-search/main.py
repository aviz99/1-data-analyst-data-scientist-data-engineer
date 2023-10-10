# 15 / 09 / 2023
# Day - 12
# Simple Search & Binary Search


# Kita harus menampung sekumpulan nilai yang ditampung ke dalam array / list
# Dimana posisi pertama diawali dengan index 0
# Posisi kedua berisi index 1 dan seterusnya
# Disini terdapat suatu function dengan nama binary_search
# Fungsi ini akan menerima 2 buah parameter.
# Parameter pertama ini berupa sorted array / sorted list (array terurut)
# Lalu, parameter kedua berisi item yang akan dicari
# Dan bilamana, item nya terdapat didalam list tadi maka function ini akan mengembalikan posisi dari item tersebut didalam listnya
# Disini untuk setiap tahapan pencarian kita akan memantau posisi dari array nya / list nya.
# Binary Search
# def binary_search(listArray, item):
#     low = 0
#     high = len(listArray) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = listArray[mid]
#         if guess < item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None


# listku = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Kasus 1 => nilai yang dicari ada di list nya
# print(f"Nilai yang dicari adalah: {binary_search(listku, 3)}")
# Kasus 2 => nilai yang dicari tidak ada di list nya
# print(f"Nilai yang dicari adalah: {binary_search(listku, 0)}")


# Binary Search part 2
def binary_search_2(data, value):
    low = 0
    high = len(data) - 1
    temp = False
    while low <= high and not temp:
        mid = (low + high) // 2
        # membandingkan value yang ketemu
        if data[mid] == value:
            temp = True
            print(f"Nilai {value} ketemu di index ke-{mid}")
        # membuang sisa yang tidak dibutuhkan
        else:
            # jika value yang dicari lebih kecil dari value mid
            if value < data[mid]:
                high = mid - 1
            # jika value yang dicari lebih besar dari mid
            else:
                low = mid + 1
    return temp


data_angka = [10, 30, 40, 5, 50, 65, 77, 69, 94, 100]
# harus di sorting dulu
data_angka.sort()
print(data_angka)

print(binary_search_2(data_angka, 10))
