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
# False jika ingin mengetahui seluruh jumlah nilai yang nan atau null (nilai yang tidak ada)
print(age.sum())
print(age.std())

# mengambil data series tanpa missing values
age_bersih = age.dropna()
print(age_bersih)