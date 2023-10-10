# 07/09/2023
# Day - 4
# Format String

# contoh generic
# string
nama = "Nofariza"
format_str = f"hello {nama}"
print(format_str)

# angka / numerik
angka = 2005.5
format_str = f"ini angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"ini nilai boolean = {boolean}"
print(format_str)

# bilangan bulat
bilangan_bulat = 15
format_str = f"ini adalah bilangan bulat = {bilangan_bulat:d}"
print(format_str)

# bilangan ribuan
bilangan_ribuan = 2000000
format_str = f"ini adalah bilangan ribuan = {bilangan_ribuan:,}"
print(format_str)

# bilangan desimal
bilangan_desimal = 2005.54321
format_str = f"ini adalah bilangan desimal = {bilangan_desimal:.2f}"
print(format_str)

# menampilkan leading zero
bilangan_desimal = 2005.54321
format_str = f"ini adalah bilangan desimal = {bilangan_desimal:010.3f}"
print(format_str)

# menampilkan tanda + -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat percentage %
percentage = 0.045
format_percentage = f"percentage = {percentage:.2%}"
print(format_percentage)

# melakukan operasi aritmatika didalam placeholder
price = 10000
total = 5

format_string = f"price total = Rp. {price*total:,}"
print(format_string)

# format angka lain binary, octal, hexadesimal
bilangan = 255
format_binary = f"binary = {bin(bilangan)}"
format_octal = f"octal = {oct(bilangan)}"
format_hexadesimal = f"hexadesimal = {hex(bilangan)}"

print(format_binary)
print(format_octal)
print(format_hexadesimal)