# 07/09/2023
# Day - 4
# String Width & Alignment

# Data
data_nama = "Erik"
data_umur = 20
data_tinggi = 170.1
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (\n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplet)
data_string = f"""
nama = {data_nama},
umur = {data_umur},
tinggi = {data_tinggi},
nomor sepatu = {data_nomor_sepatu}
"""
print(data_string)

# Mengatur lebar
data_string = f"""
nama            = {data_nama:>5},
umur            = {data_umur:>5},
tinggi          = {data_tinggi:>5},
nomor sepatu    = {data_nomor_sepatu:>5}
"""
print(data_string)