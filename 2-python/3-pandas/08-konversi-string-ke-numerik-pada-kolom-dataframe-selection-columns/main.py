# 27 / 10 / 2023
# Day - 36
# Konversi Tipe Data String Ke Numerik Pada Kolom DataFrame
import pandas as pd
import numpy as np

data = {"col1":["1", "2", "3", "teks"],
        "col2":["1", "2", "3", "4"]}

df = pd.DataFrame(data)
print(df)
print(df.dtypes)

# Konversi tipe data dengan method astype() untuk 1 kolom
df_x = df.astype({"col2":"int"})
print(df_x)
print(df_x.dtypes)

# Konversi tipe data numerik dengan method to_numeric()
# errors="coerce" artinya jika andai kata dalam proses konversi tipe data
# ke numerik didapati data yang memang tidak bisa dikonversikan ke numerik,
# maka data tersebut akan digantikan dengan "NaN"
print(df.apply(pd.to_numeric, errors="coerce"))


# 27 / 10 / 2023
# Day - 36
# Selection Columns
n_rows = 5
n_cols = 2
cols = ["bil_pecahan", "bil_bulat"]

df2 = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)),
                   columns=cols)
df2["bil_pecahan"] = df2["bil_pecahan"].astype("float")
dt = pd.date_range('2023-05-10', periods=(n_rows), freq='H')
df2.index = pd.to_datetime(dt, format='%d%b%Y:%H:%M:%S.%f')
df2 = df2.reset_index()

df2["teks"] = list("ABCDE")

print(df2)
print(df2.dtypes)

# Memilih kolom bertipe data numerik
print(df2.select_dtypes(include="number"))
print(df2.select_dtypes(include="float"))
print(df2.select_dtypes(include="int"))

# Memilih kolom bertipe data string atau object
print(df2.select_dtypes(include="object"))

# Memilih kolom bertipe data datetime
print(df2.select_dtypes(include="datetime"))

# Memilih kolom dengan kombinasi tipe data yang berbeda
print(df2.select_dtypes(include=["number", "object"]))