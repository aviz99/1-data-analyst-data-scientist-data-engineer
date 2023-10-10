# 09 / 09 / 2023
# Day - 6
# Control Flow Iterasi / Iteration / Perulangan - For Loop Statement

# for kondisi:
#      aksi

# ini dengan list (array)
# bilangan = [0,1,2,3,4] # Ini list (array)

# for i in bilangan:
#     print(f"Bilangan ke-{i}")

# ini dengan range
# kumpulan_bilangan = 1

# for i in range(kumpulan_bilangan,10):
#     print(f"Bilangan ke-{i}")

# ini menggunakan string
# data_str = "Nofariza"

# for huruf in data_str:
#     print(huruf)

no_angkot = 1
jumlah_angkot = 10
for i in range(no_angkot,jumlah_angkot + 1):
        if i == 8 or i == 4:
            print(f"Angkot No.{i} sedang lembur.")
        elif i == 5 or i == 7:
            print(f"Angkot No.{i} sedang tidak beroperasi.")
        else:
            print(f"Angkot No.{i} beroperasi dengan baik.")


# segitiga_bintang_1 = 5
# segitiga_bintang_2 = 6

# for i in range(segitiga_bintang):
#     for j in range(i+1):
#         print('* ', end='')
#     print('')

# for i in range(0, segitiga_bintang_1):
#     for j in range(0, i + 1):
#         print('* ', end='')
#     print('')

# for i in range(0, segitiga_bintang_2):
#     for j in range(0, i - 1):
#         print('* ', end='')
#     segitiga_bintang_2 -= 1
#     print('')