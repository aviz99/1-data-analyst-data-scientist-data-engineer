# contoh membuat exception
from numbers import Number


def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise f"input harus angka"
    return a + b


print(tambah(5, 6))

# menangkap berdasarkan tipe exception
angka = 0
# try:
#     hasil = 10 / angka
# except Exception as error_message:
#     print(error_message)

# ambil langsung saja / lebih detail
try:
    hasil = 10 / angka
except ZeroDivisionError as error_message:
    print(error_message)
