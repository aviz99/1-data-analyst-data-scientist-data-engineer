# 27 / 10 / 2023
# Day - 36
# Membalik Urutan Baris & Kolom Pada DataFrame 
import pandas as pd
import numpy as np

n_rows = 5
n_cols = 5
cols = tuple("ABCDE")
df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                  columns=cols)
print(df)

# Membalik urutan kolom
# print(df.loc[baris, kolom])
print(df.loc[:, ::-1])

# Membalik urutan baris
# print(df.loc[baris])
print(df.loc[::-1])

# Membalik urutan baris dan melakukan penyesuaian ulang index
print(df.loc[::-1].reset_index(drop=True))

# 27 / 10 / 2023
# Day - 36
# Mengganti Nama Kolom Pada DataFrame

# Mengganti nama (label) untuk salah satu kolom pada dataframe
print(df.rename(columns={"C":"Hobi"}))

# Mengganti nama (label) untuk banyak kolom pada dataframe
print(df.rename(columns={"A":"Nama", "B":"Alamat", "D":"Kota"}))










