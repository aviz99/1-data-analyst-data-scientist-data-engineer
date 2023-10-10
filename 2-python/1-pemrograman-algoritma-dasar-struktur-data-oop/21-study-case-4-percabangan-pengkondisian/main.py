# 09 / 09 / 2023
# Day - 6
# Study Case 4 - Percabangan IF, ELIF & ELSE Statement Kalkulator Sederhana
print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"="+"\n")

angka1 = float(input("Masukkan angka 1 : "))
operator = input("operator (+, -, *, /) : ")
angka2 = float(input("Masukkan angka 2 : "))

# Percabangan
if operator == "+":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"{angka1} * {angka2} = {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"{angka1} / {angka2} = {hasil}")
else:
    print("Operator yang anda masukkan salah!")




