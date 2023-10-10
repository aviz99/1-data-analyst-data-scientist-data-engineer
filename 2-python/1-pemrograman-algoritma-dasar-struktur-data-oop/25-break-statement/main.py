# 09 / 09 / 2023
# Day - 6
# Control Flow Iteration / Iterasi / Perulangan - Continue, Pass & Break

# bilangan = 0
# while bilangan < 5:
#     bilangan += 1
#     print(f"bilangan sekarang => {bilangan}")

#     if bilangan == 3:
#         print("Lanjut")
#         break

#     print(f"Angka ke-{bilangan}")
# print("STOP!!!")

data_int = int(input("Hitung sampai : "))
angka = 0
while True:
    angka += 1
    print(f"count : {angka}")

    if angka == data_int:
        print("Lanjut")
        break

    print(f"Angka ke-{angka}")
print("FINISH!!!")