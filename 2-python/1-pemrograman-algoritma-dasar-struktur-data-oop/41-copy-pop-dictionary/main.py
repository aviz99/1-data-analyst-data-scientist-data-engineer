# 13 / 09 / 2023
# Day - 10
# Copy & Pop Dictionary

data_dosen = {
    'nama'      :'Faqihza Mukhlis, SE',
    'nid'       : 2311001,
    'email'     : 'faqihza@gmail.com',
    'jurusan'   : 'Akuntansi',
    'no.telp'   : '082376540987',
    'alamat'    : 'Bandung'
}

dosen = data_dosen.copy()

# print(f"data dosen :\n{data_dosen}\n")
# print(f"dosen :\n{dosen}\n")

# data_dosen['nama'] = 'Sandhika Galih'
# print(f"data dosen :\n{data_dosen}\n")
# print(f"dosen :\n{dosen}\n")

# cara mengambil data dan langsung keluar
# pop dictionary => mentransfer data / mengambil data berdasrkan key
# data.pop('key')
data_jurusan = dosen.pop('jurusan')
print(f'data jurusan : {data_jurusan}\n')
print(f'data dosen : {dosen}\n')

# popitem dictionary => mengambil data / mentransfer data yang terakhir
# data.popitem()
data_terakhir = dosen.popitem() # menghasilkan tuples
print(f'data terakhir : {data_terakhir}\n')
print(f'data dosen : {dosen}\n')