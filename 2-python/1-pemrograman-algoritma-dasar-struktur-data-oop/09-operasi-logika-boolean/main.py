# 05/09/2023
# Day - 2
# Operasi Logika Atau Boolean

# not, or, and, xor

# NOT
print("===== NOT =====")
a = False
c = not a
print("Data a :",a)
print("---------- NOT")
print("data c =", c)


# OR (Jika salah satu nilai bernilai TRUE maka menghasilkan TRUE)
print("===== OR =====")
a = False
b = False
c = a or b
print(a,"OR", b, "=", c)
a = False
b = True
c = a or b
print(a,"OR", b, " =", c)
a = True
b = False
c = a or b
print(a," OR", b, "=", c)
a = True
b = True
c = a or b
print(a," OR", b, " =", c)


# AND (Kedua nilai harus bernilai TRUE maka menghasilkan TRUE)
print("===== AND =====")
a = False
b = False
c = a and b
print(a,"AND", b, "=", c)
a = False
b = True
c = a and b
print(a,"AND", b, " =", c)
a = True
b = False
c = a and b
print(a," AND", b, "=", c)
a = True
b = True
c = a and b
print(a," AND", b, " =", c)

# XOR (Akan TRUE jika salah satu TRUE, sisanya FALSE)
print("===== XOR =====")
a = False
b = False
c = a ^ b
print(a,"XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a,"XOR", b, " =", c)
a = True
b = False
c = a ^ b
print(a," XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a," XOR", b, " =", c)

# Chained Comparison
i = 15

# Cara normal
# banding_nilai = (i >= 15) and (i <= 30)
# print(f"Hasil : {banding_nilai}")

# Cara sederhana
# val operator data operator val
# compare_value = 20 <= i <= 30
# print(f"Hasil : {compare_value}")

compare_value = 20 <= i <= 30
print(f"Hasil : {compare_value}")
