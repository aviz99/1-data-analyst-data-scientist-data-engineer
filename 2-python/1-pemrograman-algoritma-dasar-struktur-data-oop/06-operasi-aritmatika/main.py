# 04/09/2023
# Day - 1
# Operasi Aritmatika

a = 10
b = 3

# operasi pertambahan +
hasil = a + b
print("Hasil dari", a, "+", b, "=", hasil)

# operasi pengurangan -
hasil = a - b
print("Hasil dari", a, "-", b, "=", hasil)

# operasi perkalian *
hasil = a * b
print("Hasil dari", a, "x", b, "=", hasil)

# operasi pembagian /
hasil = a / b
print("Hasil dari", a, "/", b, "=", hasil)

# operasi modulus sisa bagi %
hasil = a % b
print("Hasil dari", a, "modulus", b, "=", hasil)

# operasi eksponen perpangkatn **
hasil = a ** b
print("Hasil dari", a, "**(pangkat 2)", b, "=", hasil)

# operasi floor division pembagian secara kebawah atau pembulatan ke bawah //
hasil = a // b
print("Hasil dari a // b =", hasil)

# Prioritas operasi, operational presedence
x = 3
y = 2
z = 4

# KuPaKaBaMoFloTaKu ()kurung, **pangkat atau eksponen, *kali, /bagi, %modulus, //floor division, +tambah, -kurang
hasil = x ** y * (z + x) / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil2 = (x + y) * z
print(x, "+", y, "x", z, "=", hasil2)


