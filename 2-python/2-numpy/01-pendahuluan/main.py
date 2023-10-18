# 17 / 10 / 2023
# Day - 28
# Instalasi NumPy
# cara menginstal numpy pada PIP di windows
# ketik di search engine browser kalian masing-masing PIP Python
# maka akan muncul PIP Python lalu pilih yang https://pypi.org/
# jika sudah masuk ke website nya search numpy
# lalu kita harus masuk ke terminal cmd / gitbash / powershell
# ketikan pip --version pada terminal
# kalo kita mau melihat sudah instal apa saja di komputer kita
# ketikan pip list
# kembali ke website pypi nya
# lalu ketik di search engine nya numpy
# kembali ke terminal lalu kita upgrade python -m pip install --upgrade pip
# jika sudah mengupgrade dan menginstal pip versi terbaru
# maka kembali ke terminal lalu instal numpy ketikan pip install numpy
# jika sudah terinstal kita cek kemabali untuk memastikan apakah numpy tersebut sudah terinstal ke versi terbaru dengan pip list
# menginstal numpy versi yang berbeda
# pip install numpy==versiBerapa
# jika kita ingin melihat syntax - syntax yang ada di pip
# maka ketikan pip
# jika ingin mengunisntall pip numpy
# ketikan pip uninstall numpy
# lalu pilih Yes 'y'

# package operasi matematika matriks
# kegunaan nya adalah bisa membuat matriks
import numpy as np

list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

# matriks sederhana
print(f"list_a: {list_a}")
# print(list_a**2)
print(f"vector a: {vector_a}")
print(f"vector a kuadrat 2: \n{vector_a**2}")
print(f"vector a kali 5: \n{vector_a * 5}")

# matriks 2 dimensi
matrix_b = np.array([(1, 2), (3, 4)])
print(f"matrix b: \n{matrix_b}")
print(f"matrix b kuadrat 2: \n{matrix_b**2}")

# matriks zeros / matriks kosong
zeros_c = np.zeros((2, 2))
print(f"matriks zeros c: \n{zeros_c}")

# matriks ones / satu matriks satu
ones_d = np.ones((2, 2))
print(f"matriks ones d: \n{ones_d}")

# menjumlahkan seluruh matriks / melakukan operasi matriks
jumlah = matrix_b + matrix_b**2 + ones_d
print(jumlah)
