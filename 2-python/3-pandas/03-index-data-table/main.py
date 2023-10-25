# 25 / 10 / 2023
# Day - 34
# Index Data Table

import pandas as pd

# tipe data "Data Frame"
dataku = pd.read_csv('kapal_titanic.csv')
print(dataku)
print(type(dataku))

# memilih salah satu kolom
# tipe data "Series"
data_umur = dataku['age']
print(data_umur)
print(type(data_umur))

# memilih lebih dari 1 kolom
# tipe data "Data Frame"
data_slicing = dataku[['age', 'fare']]
print(data_slicing)
print(type(data_slicing))
print(dataku[['age']])

# DOT Notation
# memilih salah satu kolom secara dot / method
print(dataku.age)

# melakukan komparasi atau perbandingan
# print(dataku.age.equals('dataYangInginDikomparasi'))
print(dataku.age.equals(dataku['age']))

# slicing menggunakan iloc
# digunakan ketika kita tahu index baris dan index kolom
# .iloc[baris,kolom]
print(dataku.head())
print(dataku.iloc[0])

# mengambil lebih dari 1 baris
print(dataku.iloc[0:11])

# melakukan pemilihan kolom
print(dataku.iloc[:,3])

print(dataku.tail(10))

# melakukan index negatif baris
print(dataku.iloc[-5:])
print(dataku.iloc[-5:-1])

# melakukan index negatif kolom
print(dataku.iloc[-5:-1,-4:])
print(dataku.iloc[-5:-1,-4:-2])

# melakukan beberapa baris yang ingin diambil
print(dataku.iloc[[0,2,4]])

# melakukan beberapa kolom yang ingin diambil
print(dataku.iloc[[0,2,4],[1,3,6]])

# loc
# # digunakan ketika kita tahu nama baris dan nama kolom
# .loc['nama baris','nama kolom']
data_baru = pd.read_csv('kapal_titanic.csv', index_col='embarked')
print(data_baru)
print(data_baru.loc['S'])

# menambahkan kolom
print(data_baru.loc['S','age'])

# slicing menggunakan loc untuk baris lebih dari 1 dan kolom lebih dari 1
print(data_baru.loc['S',['age','fare']])

# mendapatkan beberapa baris
print(data_baru.loc[['S', 'Q'] , ['age','fare']])

