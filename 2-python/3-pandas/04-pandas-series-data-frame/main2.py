# 25 / 10 / 2023
# Day - 34
# Data Frame & Data Series
import numpy as np
import pandas as pd

dataku = pd.read_csv('kapal_titanic.csv')
age = dataku['age']
print(age)
# untuk menghasilkan statistik deskriptif
print(age.describe())
print(age.count())

# Data Cleaning / Membersihkan Data
print(age.mean())
print(age.median())
# pandas bisa mengabaikan nilai nilai null dan nan
# print(age.sum(skipna=True/False))
# True jika ingin mengetahui seluruh jumlah nilai yang ada pada data tersebut
# False jika ingin mengetahui seluruh
# jumlah nilai yang nan atau null (nilai yang tidak ada)
print(age.sum())
print(age.std())

# mengambil data series tanpa missing values
# dropna untuk data series secara default menghilangkan baris nya
age_bersih = age.dropna()
print(age_bersih)

# menggunakan dropna untuk seluruh data frame
# dataku2 = dataku.dropna(axis=0index=baris/1columns=kolom,thresh=1)
# theresh=1 artinya hanya akan hilang jika minimal ada satu nilai yang tidak na
# theresh=2 artinya minimal ada 2 nilai didalam satu baris itu yang bukan na,
# maka baris itu dipertahankan
# theresh=3 artinya minimal ada 3 data dalam satu baris itu yang bukan na,
# maka baris itu dipertahankan
# theresh digunakan untuk memastikan minimal ada sekian data dalam 1 baris yang
# tidak na maka baru data tersebut dipertahankan jika kurang dari data yang
# diharapkan maka baris tersebut akan dihilangkan
dataku2 = dataku.dropna(thresh=9)
print(dataku2)

# jika kita menemukan data na dalam suatu baris jangan dihilangkan nya
# karena ada formasi sangat penting dibaris tertentu
# dalam rangka preproccessing atau sebelum kita melakukan betul - betul
# analisis data science atau data tabel tersebut digunakan untuk machine learning
# membuat aplikasi AI Artificial Intellegent maka biasa nya data - data kosong (na)
# ini langkah paling aman nya adalah diisi dengan data rata - rata mean

# melakukan isi nilai nan pada baris data
dataku3 = dataku
# print(dataku3)
# print(dataku3.age.fillna(value=data.namaKolom.mean()))
# gunakan mean jika data tersebut numerik
dataku3.age = dataku3.age.fillna(value=dataku3.age.mean())
# merubah data series menjadi data array
# print(dataku.age.values)
# print(dataku3.age)
print(dataku3)