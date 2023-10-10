# 21 / 09 / 2023
# Day - 19
# Read External File Open & With

## Membaca file external
print(3 * "=", " Membaca file txt ", 3 * "=")
# file = open(namaData,mode)
file = open("data.txt", mode="r")  # w bisa mendelete text file txt

# readable = memastikan file bisa dibaca atau tidak
print(f"status read : {file.readable()}")

# writeable = memastikan file bisa ditulis / diketik atau tidak
print(f"status write : {file.writable()}")

# read = baca seluruh file
print(file.read())

# readline = membaca sebaris sebaris
# readline sudah punya \n atau enter
# print(file.readline())  # baris pertama
# print(file.readline())  # baris kedua
# menghilangkan enter
# print(file.readline(), end="")  # baris kedua
# print(file.readline(), end="")  # baris kedua

## baca semua baris tetapi menghasilkan list
# print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")

## cara membuka file dipython secara simple

print("\n", 3 * "=", " Membaca file txt dengan with ", 3 * "=")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah file sudah diclose : {file.closed}")
print(f"apakah file sudah diclose : {file.closed}")
