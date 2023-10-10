# 13 / 09 / 2023
# Day - 10
# Multi Keys & Nesting Dictionary

import datetime

data_mhs1 = {
    'nama':'Florencia Abigail',
    'nrp':'202331010',
    'sks':130,
    'beasiswa':False,
    'tanggal lahir':datetime.datetime(2006,10,18)
}

data_mhs2 = {
    'nama':'Jacquelyn Chandra',
    'nrp':'202331011',
    'sks':140,
    'beasiswa':True,
    'tanggal lahir':datetime.datetime(2007,9,12)
}

data_mhs3 = {
    'nama':'Cindy Gulla',
    'nrp':'202331012',
    'sks':100,
    'beasiswa':False,
    'tanggal lahir':datetime.datetime(2005,8,14)
}

# dictionary didalam dictionary
data_mahasiswa = {
    'MH001':data_mhs1,
    'MH002':data_mhs2,
    'MH003':data_mhs3
}

# < : rata kiri, ^ : tengah, > : rata kanan
print(f"{'KEY':<5} {'nama':<17} {'sks':<3} {'beasiswa':<9} {'tanggal lahir':<10}")
print("-"*52)

# mengambil keys dan values data mahasiswa
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nrp']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    TANGGALLAHIR = data_mahasiswa[KEY]['tanggal lahir'].strftime("%x")
    # print(TANGGALLAHIR)
    print(f"{KEY:<5} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {TANGGALLAHIR:<10}")