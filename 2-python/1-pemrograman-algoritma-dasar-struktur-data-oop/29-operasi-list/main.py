# 11 / 09 / 2023
# Day - 8
# Operasi List

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data angka :\n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"Jumlah angka 4 pada data angka : {jumlah_data_4}")
print(f"Jumlah angka 3 pada data angka : {jumlah_data_3}")

# ambil posisi data (index)
data = ["C++","Java","Python","PHP"]
print(f"Data : {data}")
    # data.index(item)
data_piton = data.index("Python")
data_jawa = data.index("Java")
print(f"Index Python : {data_piton}")
print(f"Index Java : {data_jawa}")

# mengurutkan list
print(f"data angka sebelum diurutkan :\n{data_angka}")
data_angka.sort()
print(f"data angka sesudah diurutkan :\n{data_angka}")
print(f"Data sebelum diurutkan: {data}")
data.sort()
print(f"Data sesudah diurutkan: {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"Data dan data angka dibalik :\n{data}\n{data_angka}")