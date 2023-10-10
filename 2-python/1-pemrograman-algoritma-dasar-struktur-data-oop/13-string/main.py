# 07/09/2023
# Day - 4
# String

data = "Ini adalah string"
print(data)
print(type(data),"\n")

# 1. Cara membuat string

# a. Menggunakan single quote '...'
dataStringSatu = 'Ini menggunakan single quote.'
print(dataStringSatu)

# b. Menggunakan double quote '...'
dataStringDua = "Ini menggunakan double quote."
print(dataStringDua)

print("Samsul kemarin melakukan sholat jum'at pada hari jum'at.\n")
print('Ujang pernah berkata "Janganlah kamu berharap apa yang kamu harapkan karena apa yang kamu harapkan tidak sesuai apa yang kamu harapkan.\n"')

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# Backslash
print("C:\\user\\Ucup")

# Tab
print("Ucup\tOtong")

# Backspace
print("Ucup \bOtong")

# newLine
print("Baris pertama.\nBaris kedua.") # LF => Line Feed => Dipakai oleh unix, macos, linux
print("Baris pertama.\rBaris kedua.") # CR => Carriage Return => Dipakai oleh commodore, acorn, lisp
print("Baris pertama.\r\nBaris kedua.\n") # CRLF => Carriage Return Line Feed => Dipakai oleh windows

# 3. String literal atau raw

# Hati-Hati
print('C:\new folder') # akan salah pathnya

# Menggunakan RAW String
print(r'C:\new folder')

# Multiline Literal String
print("""
Nama : Muhaimin
Kelas : 3 SMP
""")

# Multiline Literal String dan RAW
print(r"""
Nama : Muhaimin
Kelas : 3 SMP\new normal
Website : www.muhaiminwowmania.com/newID
""")