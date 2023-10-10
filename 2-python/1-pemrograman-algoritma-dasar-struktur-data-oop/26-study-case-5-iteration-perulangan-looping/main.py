# 11 / 09 / 2023
# Day - 8
# Study Case 5 - Iteration / Perulangan

# Membuat Segitiga

sisi = 9

# Menggunakan FOR

# variable dummy
count = 1
print(5*"-"+"Awal FOR"+5*"-")
for i in range(sisi):
    print("*"*count)
    count += 1

print(5*"-"+"Akhir FOR"+5*"-")

# Menggunakan WHILE
print(5*"-"+"Awal WHILE"+5*"-")
count2 = 1
while True:
    print("*"*count2)
    count2 += 1
    
    if count2 > sisi:
        break

print(5*"-"+"Akhir WHILE"+5*"-")

# Menggunakan ganjil saja
# print(5*"-"+"Awal Ganjil"+5*"-")
count3 = 1
# while True:
#     if (count3%2):
        # Akan print jika nilai nya ganjil
    #     print("*"*count3)
    #     count3 += 1
    # else:
        # Akan kembali ke atas jika nilai nya ganjil
        # count3 += 1
        # continue
    
    # Akan break jika count melebihi sisi
#     if count3 > sisi:
#         break

# print(5*"-"+"Akhir Ganjil"+5*"-")

print(5*"-"+"Awal Ganjil"+5*"-")
count3 = 1
spasi = int(sisi/2)
while True:
    if (count3%2):
        # Akan print jika nilai nya ganjil
        print(" "*spasi,"+"*count3)
        spasi -= 1
        count3 += 1
    else:
        # Akan kembali ke atas jika nilai nya ganjil
        count3 += 1
        continue
    
    # Akan break jika count melebihi sisi
    if count3 > sisi:
        break

print(5*"-"+"Akhir Ganjil"+5*"-")

print(5*"-"+"Awal Ketupat"+5*"-")
count4 = 1
spasi2 = 5
while count4<=sisi:
    if (count4%2):
        print(' '*spasi2,'*'*count4)
        spasi2 -= 1
    count4 += 1
spasi2 = 2
x = sisi - 1
while x<=sisi:
    if (x%2):
        print(' '*spasi2,'*'*x)
        spasi2 += 1
    x -= 1
    if x == 0:
        break


print(5*"-"+"Akhir Ketupat"+5*"-")