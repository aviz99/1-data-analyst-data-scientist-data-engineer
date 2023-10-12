# 12 / 10 / 2023
# Day - 27
# Bubble Sort
# Bubble Sort adalah sebuah algoritma pengurutan atau algoritma sorting yang dapat menukarkan posisi data yang telah dibandingkan sesuai dengan kriteria yang diinginkan
# Secara garis besar nya Bubble Sort ini membandingkan 2 nilai secara ascending (dari nilai terkecil ke nilai terbesar) maupun descending (nilai terbesar ke nilai terkecil)

angka_urut = [3, 7, 1, 2, 9, 5, 67, 45, 76, 31, 99, 95, 90]
print(angka_urut)

# bubble sort ascending
# def bubble_sort_asc(angka):
#     for i in range(len(angka) - 1, 0, -1):
#         print("langkah")
#         for j in range(0, len(angka) - 1):
#             # membandingkan nilai secara ascending
#             if angka[j] > angka[j + 1]:
#                 # ditukar antar nilai
#                 angka[j], angka[j + 1] = angka[j + 1], angka[j]
#         print(angka)


# bubble sort descending
def bubble_sort_desc(angka):
    for i in range(len(angka) - 1, 0, -1):
        print("langkah")
        for j in range(0, len(angka) - 1):
            # membandingkan nilai secara ascending
            if angka[j] < angka[j + 1]:
                # ditukar antar nilai
                angka[j], angka[j + 1] = angka[j + 1], angka[j]
        print(angka)


bubble_sort_desc(angka_urut)
