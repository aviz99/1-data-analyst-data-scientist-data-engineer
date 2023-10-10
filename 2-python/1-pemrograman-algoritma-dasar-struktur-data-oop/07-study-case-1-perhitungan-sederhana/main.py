# 04/09/2023
# Day - 1
# Study Case 1 - Konversi Satuan Temperatur

# Program konversi celsius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# celcius = float(input("Masukkan suhu ke dalam celcius :"))
# print("suhu adalah",celcius, "Celcius")

# reamur
# rumus = (4/5)C
# reamur = 4/5 * celcius
# print("suhu dalam reamur adalah",reamur, "Reamur")

# fahrenheit
# rumus = (9/5)C + 32
# fahrenheit = (9/5) * celcius + 32
# print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

# kelvin
# rumus = C + 273
# kelvin = celcius + 273
# print("suhu dalam kelvin adalah",kelvin, "Kelvin")

# Task 1
# Fahrenheit => Kelvin
fahrenheit = float(input("Masukkan suhu ke fahrenheit :"))
celcius = 5/9 * fahrenheit - 32
kelvin = celcius + 273
print("Suhu dalam fahrenheit adalah:", kelvin)

# Kelvin => Fahrenheit
kelvin = float(input("Masukkan suhu ke kelvin :"))
celcius = kelvin + 273
fahrenheit = 5/9 * celcius - 32
print("Suhu dalam kelvin adalah:", fahrenheit)