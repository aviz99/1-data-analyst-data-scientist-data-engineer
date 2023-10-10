# 15 / 09 / 2023
# Day - 12
# Type Hints Function

import string


# penggunaan type hints
# def namaFungsi(argument/parameter: tipeData) -> expression/tipeData:
#       aksi / body
#       return nilai
def fungsi_hints(argument: int) -> int:
    """FUNGSI DENGAN HINTS"""
    output = 10**argument
    return output


hasil = fungsi_hints(2)
print(hasil)


def display(argument: string):
    print(argument)


display("Asep")

# import os

# hasil = os.system("clear")
# print(hasil)
