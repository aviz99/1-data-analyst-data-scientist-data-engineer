# 15 / 09 / 2023
# Day - 12
# Function Default Argument
# def fungsi(argument = nilai default):


# contoh 1
def say_hello(nama="Black"):
    print(f"Hallo {nama}")


say_hello("Asep Komarudin")
say_hello()


# fungsi dengan 1 argument biasa dan 1 default argument
# contoh 2
def sapa_dia(nama, pesan="Apa kabar?"):
    print(f"hai {nama}, {pesan}")


sapa_dia("Jacquelyn", "Hai Cantik")
sapa_dia("Florencia")


# contoh 3
def hitung_pangkat(angka, bil_pangkat=2):
    hasil = angka**bil_pangkat
    return hasil


print(hitung_pangkat(2, 4))
result = hitung_pangkat(bil_pangkat=3, angka=5)
print(f"hasil dari: {result}")


# contoh 4
def ini_fungsi(nilai1=1, nilai2=2, nilai3=3, nilai4=4):
    hasil = nilai1 + nilai2 + nilai3 + nilai4
    return hasil


print(ini_fungsi())
print(ini_fungsi(nilai3=10))
