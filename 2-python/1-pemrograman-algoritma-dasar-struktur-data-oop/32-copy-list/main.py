# 11 / 09 / 2023
# Day - 8
# Copy List

# Teknik menduplikat list
data = ["C++","Java","Python","PHP"]
print(f"data : {data}")

dataDua = data # pass by reference / mengubah nama list tetapi address nya sama
print(f"data dua = {dataDua}")

# kita akan merubah member dari a

# ini akan merubah kedua list
data[1] = "Haskell"
dataDua.sort()
print(f"data : {data}")
print(f"data dua = {dataDua}")

# address dari kedua list
print(f"address data : {hex(id(data))}")
print(f"address dataDua : {hex(id(dataDua))}")

# menduplikat list dengan copy

print("Membuat list dataTiga dengan data.copy()")
dataTiga = data.copy() # full duplikat / data baru

print(f"address data : {hex(id(data))}")
print(f"address dataDua : {hex(id(dataDua))}")
print(f"address dataTiga : {hex(id(dataTiga))}")

print(f"data : {data}")
print(f"data dua = {dataDua}")
print(f"data tiga = {dataTiga}")

print("Kita ubah data 0")
dataTiga[0] = "Javascript"

print(f"data : {data}")
print(f"data dua = {dataDua}")
print(f"data tiga = {dataTiga}")

print("Kita ubah data 2")
dataTiga[2] = "Ruby"

print(f"data : {data}")
print(f"data dua = {dataDua}")
print(f"data tiga = {dataTiga}")