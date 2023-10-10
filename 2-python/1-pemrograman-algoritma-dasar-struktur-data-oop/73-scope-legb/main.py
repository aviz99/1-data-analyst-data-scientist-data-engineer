# 25 / 09 / 2023
# Day - 21
# Scope & LEGB
# Python adalah procedural programming language atau membaca secara terurut dari atas sampai bawah

# Urutan Eksekusi Python
# L (Local) = variable ini bersifat lokal, yang biasanya berada di dalam fungsi (def/lambda) tertentu.
# E (Enclosing function local) = variable ini berada di dalam fungsi (def/lambda) mulai dari lingkup terdalam hingga keluar.
# G (Global) = variable ini didefinisikan di luar, biasa nya tahap awal.
# B (Built-in variable) = variable ini bawaan Python, seperti list, str, upper, dll
# a = 1000


# def jumlah():
#     a = 79
#     return a


# print(a)
# print(jumlah())

kalimat = "saya adalah GLOBAL"


def cetak():
    # kalimat = "saya adalah LOCAL"

    def ekeskusi():
        kalimat = "saya itu LOCAL DALAM"
        print(f"hasilnya adalah {kalimat}")

    ekeskusi()


cetak()

# materi yang lebih advanced
angka = 99


def tulis(angka):
    # print(f"angka = {angka}")
    # print("angka = {}".format(angka))

    # mendefinisikan ulang sebuah variable di fungsi
    angka = 300
    print(f"Angkanya sekarang saya rubah menjadi: {angka}")
    return angka


tulis(angka)

# variable global tidak akan bisa dipengaruhi oleh sebuah fungsi
print(angka)


def menulis():
    global angka
    # print(f"Number = {angka}")

    angka = "Ganti Lo"
    print(f"Number sekarang saya ubah menjadi: {angka}")


menulis()
print(angka)
