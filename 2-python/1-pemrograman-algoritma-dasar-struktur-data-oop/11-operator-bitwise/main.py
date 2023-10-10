# 06/09/2023
# Day - 3
# Operator Bitwise / Operator Binary

a = 9
b = 5

# Bitwise OR ( | )
c = a | b
print("\n========OR========")
print("nilai :",a," , binary :",format(a,"08b"))
print("nilai :",b," , binary :",format(b,"08b"))
print("---------------------------- (|)")
print("nilai :",c," , binary :",format(c,"08b"))

# Bitwise AND ( & )
c = a & b
print("\n========AND========")
print("nilai :",a," , binary :",format(a,"08b"))
print("nilai :",b," , binary :",format(b,"08b"))
print("---------------------------- (&)")
print("nilai :",c," , binary :",format(c,"08b"))

# Bitwise XOR ( ^ )
c = a ^ b
print("\n========XOR========")
print("nilai :",a," , binary :",format(a,"08b"))
print("nilai :",b," , binary :",format(b,"08b"))
print("---------------------------- (^)")
print("nilai :",c," , binary :",format(c,"08b"))

# Bitwise NOT ( ~ )
c = ~a
print("\n========NOT========")
print("nilai :",a," , binary :",format(a,"08b"))
print("---------------------------- (~)")
print("nilai :",c," , binary :",format(c,"08b"))
print("---------------------------- (^)")
d = 0b0000001001
e = 0b1111111111
print("Nilai :",e^d," , binary :",format(e^d,"08b"))

# Shifting

# shift right (>>)
c = a >> 5
print("\n========SHIFT RIGHT========")
print("nilai :",a," , binary :",format(a,"08b"))
print("---------------------------- (>>)")
print("nilai :",c," , binary :",format(c,"08b"))

# shift left (<<)
c = a << 5
print("\n========SHIFT LEFT========")
print("nilai :",a," , binary :",format(a,"08b"))
print("---------------------------- (<<)")
print("nilai :",c," , binary :",format(c,"08b"))
