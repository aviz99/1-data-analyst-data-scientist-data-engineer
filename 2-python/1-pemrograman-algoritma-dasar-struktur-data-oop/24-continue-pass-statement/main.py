# 09 / 09 / 2023
# Day - 6
# Control Flow Iteration / Iterasi / Perulangan - Continue, Pass & Break

# pass => dia berfungsi sebagai dummy, tidak akan dieksekusi

# bilangan = 0

# while bilangan < 5:
#     bilangan += 1
#     if bilangan == 3:
        # pass # ini tidak akan dieksekusi
    # print(bilangan)

# continue 
bilangan = 0

print(f"bilangan sekarang => {bilangan}")

while bilangan < 5:
    bilangan += 1
    print(f"bilangan sekarang => {bilangan}") # aksi 1

    if bilangan == 3:
        print("Lanjut")
        continue # akan lanjut ke step selanjutnya
    print(f"angka ke-{bilangan}") # aksi 2
print("STOP!!!")