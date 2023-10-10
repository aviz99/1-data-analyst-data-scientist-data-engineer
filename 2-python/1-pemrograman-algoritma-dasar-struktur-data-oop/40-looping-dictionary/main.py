# 13 / 09 / 2023
# Day - 10
# Looping Dictionary

data_mhs = {
    'nama'    : 'Erik Setiawan',
    'nrp'     : 201621002,
    'email'   : 'erik@gmail.com',
    'jurusan' : 'Teknik Industri',
    'no.telp' : '089712349876'
}

# print(f"Mahasiswa 1 :\n{data_mhs}")

# looping first try
for mhs in data_mhs: # menghasilkan key
    print(mhs)

# operator untuk mengambil item / iterables (keys)
keys = data_mhs.keys()
print(keys)

for key in data_mhs.keys():
    print(data_mhs.get(key))

# operator untuk mengambil item / iterables (values)
values = data_mhs.values()
print(values)

for value in data_mhs.values():
    print(value)

# operator untuk mengambil item / iterables (items)
# items = pasangan - pasangan dari key dan value
items = data_mhs.items()
print(items)

for item in data_mhs.items(): # menghasilkan tuples
    print(item)

# mengambil item berdasarkan keys & values
for key,value in data_mhs.items():
    print(f"key:{key} value:{value}")