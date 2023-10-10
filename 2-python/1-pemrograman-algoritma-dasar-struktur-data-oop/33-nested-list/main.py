# 11 / 09 / 2023
# Day - 8
# Nested List
data_nol = [1,2]
data_satu = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa : {data_list_biasa}")

list_2D = [data_nol,data_satu,5,6,7]
print(f"List dua dimensi : {list_2D}")

# contoh penggunaan
peserta_0 = ["doddy",29,"Laki-laki"]
peserta_1 = ["nofariza",26,"Laki-laki"]
peserta_2 = ["erik",24,"Laki-laki"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"Peserta lomba kelereng :\n{list_peserta}")

for peserta in list_peserta:
    print(f"nama\t\t: {peserta[0]}")
    print(f"umur\t\t: {peserta[1]}")
    print(f"jenis kelamin\t: {peserta[2]}\n")

# Ada permasalahan dengan reference
list_copy = list_peserta.copy()
print(f"Peserta :\n{list_copy}")
peserta_0[0] = "Clara"
print(f"Peserta :\n{list_copy}")
print(f"Peserta :\n{list_peserta}")
