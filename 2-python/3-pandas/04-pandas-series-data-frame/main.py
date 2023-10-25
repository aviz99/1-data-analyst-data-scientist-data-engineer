# 25 / 10 / 2023
# Day - 34
# Data Frame & Data Series
import numpy as np
import pandas as pd

label = ['satu','dua','tiga']
angka = [10, 20, 30]
np_array = np.array(angka)
data_dictionary = {'satu':10, 'dua':20, 'tiga':30}
print(np_array)

# membuat pandas Series
# print(pd.Series(data=list/dataframe))
print(pd.Series(data=angka))

# menentukan index dipandas sesuai keinginan kita
# print(pd.Series(data=list/dataframe, index=angka/data))
dataku = pd.Series(data=angka, index=label)
print(dataku['satu'])
print(np_array[0])

# membuat pandas Series secara cepat
print(pd.Series(data_dictionary))
print(pd.Series(np_array))

# merubah data Series menjadi Data Frame
mydata = dataku.to_frame()
print(mydata)

data_dictionary2 = {'satu':10, 'dua':20, 'tiga':30, 'empat':40, 'lima':50}
mydata2 = pd.Series(data_dictionary)
mydata3 = pd.Series(data_dictionary2)
print(mydata2)
print(mydata3)

# menjumlahkan data Series
# jika ada index yang sama pada antara mydata2 dan mydata3 maka akan menjumlahkan yang index nya sama
# jika index nya tidak sama maka akan menjadi NaN
print(mydata2 + mydata3)

# DataFrame
# Dua Dimensi punya baris dan kolom
# dataku2 = pd.DataFrame(data=Data, index=Index, columns=kolomnya)
print(np.random.seed(100))
dataku2 = pd.DataFrame(np.random.randn(3,5), ['A', 'B', 'C'], ['satu', 'dua', 'tiga', 'empat', 'lima'])
print(dataku2)
print(dataku2['dua'])

# menambahkan kolom baru
dataku2['baru'] = dataku2['empat'] + dataku2['lima']
print(dataku2)

# menghapus sebuah kolom
# dataku2.drop(namaKolom, axis=baris:0/kolom:1)
# print(dataku2.drop('tiga', axis=1))
dataku2 = dataku2.drop('tiga', axis=1)
print(dataku2)

# cara lain untuk menghapus kolom tanpa melakukan re-assignment
dataku2.drop('baru', axis=1, inplace=True)
print(dataku2)

# menghapus sebuah baris
# dataku2.drop(namaKolom, axis=baris:0/kolom:1)
dataku2.drop('B', axis=0, inplace=True)
print(dataku2)

# mengetahui dimensi data frame
print(dataku2.shape)

# melakukan komparasi
dataku2_bool = dataku2 < 0
print(dataku2_bool)
print(dataku2[dataku2_bool])

dataku2 = pd.DataFrame(np.random.randn(3,5), ['A', 'B', 'C'], ['satu', 'dua', 'tiga', 'empat', 'lima'])
print(dataku2)

print(dataku2[dataku2['tiga'] > 0])

hasil = dataku2[dataku2['lima'] > 0]
print(hasil)