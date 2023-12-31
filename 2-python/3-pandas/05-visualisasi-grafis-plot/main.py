# 25 / 10 / 2023
# Day - 34
# Visualisasi Grafis (Plotting)
import pandas as pd
import seaborn as sns
import numpy as np

# Library yang digunakan untuk Visualisasi data grafis (plotting)
# 1. Matplotlib
# 2. Seaborn
# 3. Plotly

dataku = pd.read_csv('kapal_titanic.csv')
# print(dataku.head())

# membuat visualisasi kolom 'age' atau membuat histogram
# print(dataku.age.hist())

# mengatur banyak nya batang diagram
# print(dataku.age.hist(bins=30))

# menghilangkan grid
# print(dataku.age.plot.hist(bins=30))
# print(sns.set())
# print(dataku.age.plot.hist(bins=30))

# mengatur tingkat transparansi
# print(dataku.age.plot.hist(bins=30, alpha=0.4))

print(np.random.seed)
angka = []
for i in range(0,100):
    angka.append(i)
print(angka)
baru = pd.DataFrame(np.random.rand(100,5),angka,['A','B','C','D','E'])
print(baru.head())

# membuat plot area
# print(baru.plot.area(alpha=0.4))

baru2 = pd.DataFrame(np.random.rand(4,5),[0,1,2,3],['A','B','C','D','E'])
# print(baru2.plot.bar())
# print(baru2.plot.bar(stacked=True))
# print(baru2['C'].plot.bar())

# membuat scatter plot
# baru.plot.scatter(x='sumbuX', y='sumbuY', c='warna', cmap='namaWarna')
# print(baru.plot.scatter(x='A', y='B', c='E', cmap='pink'))

# membedakan titik berdasarkan ukuran
# baru.plot.scatter(x='sumbuX', y='sumbuY', s=scalar/array_like/dataframe, c='warna', cmap='namaWarna')
# print(baru.plot.scatter(x='A', y='B', s=baru.D*100))

# membuat box plot
# print(baru.plot.box())

# membuat line plot
# print(baru.plot.line(x=sumbuX, y=sumbuY/kolomyangdiinginkan))
# print(baru.plot.line(y='B'))
# menentukan tebal tipis nya garis
# print(baru.plot.line(x=sumbuX, y=sumbuY/kolomyangdiinginkan, lw=ukuranGaris))
# print(baru.plot.line(y='B', lw=12))

# menentukan panjang lebar nya line plot
# print(baru.plot.line(x=sumbuX, y=sumbuY/kolomyangdiinginkan, figsize=(panjang, lebar)))
# print(baru.plot.line(y='B', figsize=(15,5)))

# membuat plot hexxbin
# print(baru.plot.hexxbin(x=sumbuX, y=sumbuY, gridsize=ukuran))
print(baru.plot.hexbin(x='A', y='B', gridsize=10))