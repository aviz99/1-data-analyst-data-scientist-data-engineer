# 04/09/2023
# Day - 1
# Operator Komparasi

# Setiap hasil dari operasi komparasi adalah boolean true / false

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari (>)
print("========== Lebih Besar Dari (>) ==========")
hasil = a > 3
print(a,">","3","=",hasil)
hasil = b > 3
print(b,">","3","=",hasil)
hasil = b > 2
print(b,">","2","=",hasil)

# kurang dari (<)
print("========== Kurang Dari (<) ==========")
hasil = a < 3
print(a,"<","3","=",hasil)
hasil = b < 3
print(b,"<","3","=",hasil)
hasil = b < 2
print(b,"<","2","=",hasil)

# lebih dari sama dengan (>=)
print("========== Lebih Dari Sama Dengan (>=) ==========")
hasil = a >= 3
print(a,">=","3","=",hasil)
hasil = b >= 3
print(b,">=","3","=",hasil)
hasil = b >= 2
print(b,">=","2","=",hasil)

# kurang dari sama dengan (<=)
print("========== Kurang Dari Sama Dengan (<=) ==========")
hasil = a < 3
print(a,"<=","3","=",hasil)
hasil = b <= 3
print(b,"<=","3","=",hasil)
hasil = b <= 2
print(b,"<=","2","=",hasil)

# sama dengan dari (==)
print("========== Sama Dengan Dari (==) ==========")
hasil = a == 3
print(a,"==","3","=",hasil)
hasil = b == 3
print(b,"==","3","=",hasil)
hasil = b == 2
print(b,"==","2","=",hasil)

# tidak sama dengan dari (!=)
print("========== Tidak Sama Dengan Dari (!=) ==========")
hasil = a != 3
print(a,"!=","3","=",hasil)
hasil = b != 3
print(b,"!=","3","=",hasil)
hasil = b != 2
print(b,"!=","2","=",hasil)

# is sebagai komparasi object identity
print("========== Object Identity (is) ==========")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))
hasil = x is y
print("x is y =", hasil)

j = 5 # ini adalah assignment membuat object
i = 6
print("nilai j =",j,"id = ",hex(id(j)))
print("nilai i =",i,"id = ",hex(id(i)))
hasil1 = j is not i
print("j is not i =", hasil1)


