# 06/09/2023
# Day - 3
# Operator Assignment / Operator Penugasan
# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 # 5 adalah assignment
b = 5
c = 5
d = 5
e = 10
f = 10
g = 5

# Operator Penugasan Aritmatika
print("========OPERATOR PENUGASAN ARITMATIKA========")
# Operator Penambahan ( += )
a += 1 # a = a + 1
print("nilai a = a + 1 =",a)

# Operator Pengurangan ( -= )
b -= 2 # b = b - 2
print("nilai b = b - 2 =",b)

# Operator Perkalian ( *= )
c *= 5 # c = c * 5
print("nilai c = c * 5 =",c)

# Operator Pembagian ( /= )
d /= 2 # d = d / 2
print("nilai d = d / 2 =",d)

# Operator Modulus ( %= )
e %= 3 # e = e % 3
print("nilai e = e % 3 =",e)

# Operator Floor Division ( //= )
f //= 3 # f = f // 3
print("nilai f = f // 3 =",f)

# Operator Eksponen / Perpangkatan ( **= )
g **= 3 # g = g ** 3
print("nilai g = g ** 3 =",g)

print("\n")

# Operator Penugasan Bitwise
print("======OPERATOR PENUGASAN BITWISE=======")

# Operator OR (|=)
h = True
print("nilai h =",h)
h |= False
print("nilai h = h | False =",h)
h = False
print("nilai h =",h)
h |= False
print("nilai h = h | False =",h,"\n")

# Operator AND (&=)
h = True
print("nilai h =",h)
h &= False
print("nilai h = h & False =",h)
h = True
print("nilai h =",h)
h &= True
print("nilai h = h & True =",h,"\n")

# Operator XOR (^=)
h = True
print("nilai h =",h)
h ^= False
print("nilai h = h ^ False =",h)
h = True
print("nilai h =",h)
h ^= True
print("nilai h = h ^ True =",h,"\n")

# Geser geser
i = 0b0100
print("nilai i =",format(i,"04b"))

# Operator Shift Right (>>=)
i >>= 2
print("nilai i = i >> 2 =",format(i,"04b"))

# Operator Shift Left (<<=)
i <<= 1
print("nilai i = i << 1 =",format(i,"04b"))