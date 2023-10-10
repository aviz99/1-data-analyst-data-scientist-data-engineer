# 05/09/2023
# Day - 2
# Study Case 2 - Komparasi & Logika

# Membuat gabungan area rentang dari angka

# ++++++3----------10++++++
# Kasus digabungkan

# inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau\nlebih besar dari 10 :\n"))

# +++++++3--------
# Memeriksa angka kurang dari 3
# isKurangDari = (inputUser < 3)
# print("Kurang dari 3 :",isKurangDari)

# ----------10++++++
# Memeriksa angka lebih dari 10
# isLebihDari = (inputUser > 10)
# print("Lebih dari 10 :",isLebihDari)

# ++++++3----------10++++++
# isGabung = isKurangDari or isLebihDari
# print("Jika digabungkan maka akan menghasilkan :",isGabung)


# print("\n",10*"=","\n")
# ----------3++++++++++10--------
# Kasus irisan
# input = float(input("Masukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10 :\n"))

# ----------3++++++++++++++++
# Lebih dari 3
# isGreaterThan = input > 3
# print("Lebih dari 3 :",isGreaterThan)

# # +++++++10----------------
# Kurang dari 10
# isLessThan = (inputUser < 10)
# print("Kurang dari 10 :",isLessThan)

# ----------3++++++++++10--------
# isJoin = isGreaterThan and isLessThan
# print("Jika digabungkan maka akan menghasilkan :",isJoin)

# ==============================================

# 06/09/2023
# Day - 3
# Task 2
print("====== Task 2 =======")
print("\n")

print("====== NUMBER 1 =======")
inputUser1 = float(input("Masukkan angka yang bernilai\nlebih besar dari 0, \nkurang dari 5,\nlebih besar dari 8 dan\nkurang dari 11:\n"))

# --------0+++++++++
# Memeriksa angka lebih dari 0
isGreaterThanZero = (inputUser1 > 0)
print("Lebih dari 0 :",isGreaterThanZero)

# ++++++++5---------
# Memeriksa angka kurang dari 5
isLessThanFive = (inputUser1 < 5)
print("Kurang dari 5 :",isLessThanFive)

# --------8+++++++++
# Memeriksa angka kurang dari 5
isGreaterThanEight = (inputUser1 > 8)
print("Lebih dari 8 :",isGreaterThanEight)

# ++++++++11---------
# Memeriksa angka kurang dari 11
isLessThanEleven = (inputUser1 < 11)
print("Kurang dari 11 :",isLessThanEleven)

# --------0+++++++++5---------
isJoinFirstNoOne = isGreaterThanZero and isLessThanFive
print("Jika digabungkan maka akan menghasilkan :",isJoinFirstNoOne)

# --------8+++++++++11---------
isJoinSecondNoOne = isGreaterThanEight and isLessThanEleven
print("Jika digabungkan maka akan menghasilkan :",isJoinSecondNoOne)

# --------0+++++++++5---------8+++++++++11---------
isJoinThirdNoOne = isJoinFirstNoOne or isJoinSecondNoOne
print("Jika digabungkan maka akan menghasilkan :",isJoinThirdNoOne)

print("\n")

print("====== NUMBER 2 =======")
inputUser2 = float(input("Masukkan angka yang bernilai\nkurang dari 0, \nlebih dari 5,\nkurang dari 8 atau\nlebih dari 11:\n"))

# ++++++++0---------
# Memeriksa angka kurang dari 5
isLessThanZero = (inputUser2 < 0)
print("Kurang dari 0 :",isLessThanZero)

# --------5+++++++++
# Memeriksa angka lebih dari 5
isGreaterThanFive = (inputUser2 > 5)
print("Lebih dari 5 :",isGreaterThanFive)

# ++++++++8---------
# Memeriksa angka kurang dari 8
isLessThanEight = (inputUser2 < 8)
print("Kurang dari 8 :",isLessThanEight)

# --------11+++++++++
# Memeriksa angka lebih dari 11
isGreaterThanEleven = (inputUser2 > 11)
print("Lebih dari 11 :",isGreaterThanEleven)

# ++++++++0---------5+++++++++
isJoinFirstNoTwo = isLessThanZero or isGreaterThanFive
print("Jika digabungkan maka akan menghasilkan :",isJoinFirstNoTwo)

# ++++++++8---------11+++++++++
isJoinSecondNoTwo = isLessThanEight or isGreaterThanEleven
print("Jika digabungkan maka akan menghasilkan :",isJoinSecondNoTwo)

# ++++++++0---------5+++++++++8---------11+++++++++
isJoinThirdNoTwo = isJoinFirstNoTwo and isJoinSecondNoTwo
print("Jika digabungkan maka akan menghasilkan :",isJoinThirdNoTwo)
