# 11 / 09 / 2023
# Day - 8
# List / Array nya Python

# list / kumpulan data int
data_integer = [1,2,3,4,5]
print(f"List integer : {data_integer}")

# list / kumpulan data str
data_string = ["Nofariza","Erik","Doddy","Dewi","Fitri"]
print(f"List string : {data_string}")

# list / kumpulan data float
data_float = [1.1, 2.2, 3.3, 4.4, 5.5]
print(f"List float : {data_float}")

# list / kumpulan data bool
data_boolean = [True, False]
print(f"List boolean : {data_boolean}")

# kita bisa memasukkan list dengan tipe data yang berbeda
data_type_mix = [100, 2.5, "Doddy", True]
print(f"List tipe data campuran : {data_type_mix}")

# cara alternatif membuat list
data_range = range(0,10,2) # range(startIndex,endIndex,increment)
print(data_range)
data_list = list(data_range)
print(data_list)

# cara membuat list dengan menggunakan iteration for loop, list comprehension
data_list_for = [i**2 for i in range(0,10)]
print(data_list_for)

# cara membuat list dengan menggunakan pengkondisian dan perulangan (Iteration & Conditional)
data_list_for_if = [i for i in range(0,10) if i != 5]
print(data_list_for_if)

data_list_for_if_genap = [i for i in range(0,10) if i % 2 == 0]
print(data_list_for_if_genap)

data_list_for_if_ganjil = [i for i in range(0,10) if i % 2 == 1]
print(data_list_for_if_ganjil)