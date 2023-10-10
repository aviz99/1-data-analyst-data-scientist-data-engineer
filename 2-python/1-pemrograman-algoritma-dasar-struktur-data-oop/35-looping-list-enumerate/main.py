# 11 / 09 / 2023
# Day - 8
# Looping List & Enumerate

# for loop
print("\n"+5*"="+"FOR LOOP"+5*"=")
data_int = [4,3,2,5,6,1]

for integer in data_int:
    print(f"angka : {integer}")

data_nama = ["clara","dinda","evelyn","florencia","giska"]

for nama in data_nama:
    print(f"nama : {nama}")

# for loop & range
print("\n"+5*"="+"FOR LOOP & RANGE"+5*"=")
data_angka = [10,5,4,2,6,5]
ukuran = len(data_angka)

for i in range(ukuran):
    print(f"angka ke-{data_angka[i]}")

# while
print("\n"+5*"="+"WHILE LOOP"+5*"=")
data_angka = [10,5,4,2,6,5]
ukuran = len(data_angka)
i = 0

while i < ukuran:
    print(f"angka ke-{data_angka[i]}")
    i += 1

# list comprehension
print("\n"+5*"="+"LIST COMPREHENSION"+5*"=")
data = ["cindy",1,2,3,"erik"]
angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(f"angka kuadrat : {angka_kuadrat}")
[print(f"data : {i}") for i in data]

# enumerate
# mengmabil index dan data nya
print("\n"+5*"="+"ENUMERATE"+5*"=")
data1 = ["dinda",1,2,3,"doddy"]
for index,data in enumerate(data1):
    print(f"index : {index}, data : {data}")
