# 12 / 09 /2023
# Day - 9
# Packing & Unpacking List
# a = 10
# b = 20
# c = 30
# d = [a,b,c]
# print(f"List d : {d}")

# Packing List
a, b, c = 10, 20, 30
d = [a, b, c]
print("\n"+5*"="+"DATA LIST YANG SUDAH DIPACKING"+5*"=")
print(f"Data d : {d}")

# Unpacking List
data = [10,20,30]
d,e,f = data
print("\n"+5*"="+"DATA LIST YANG SUDAH DIUNPACKING"+5*"=")
print(f"d : {d}\ne : {e}\nf : {f}")