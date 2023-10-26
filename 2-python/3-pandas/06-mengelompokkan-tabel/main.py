# 26 / 10 / 2023
# Day - 35
# Mengelompokkan & Menggabungkan Tabel
import pandas as pd

satu = pd.DataFrame(
    {
        "A": ["a0", "a1", "a2", "a3", "a4", "a5"],
        "B": ["b0", "b1", "b2", "b3", "b4", "b5"],
        "C": ["c0", "c1", "c2", "c3", "c4", "c5"],
        "D": ["d0", "d1", "d2", "d3", "d4", "d5"],
    },
    index=[0, 1, 2, 3, 4, 5],
)

dua = pd.DataFrame(
    {
        "A": ["a6", "a7", "a8", "a9", "a10", "a11"],
        "B": ["b6", "b7", "b8", "b9", "b10", "b11"],
        "C": ["c6", "c7", "c8", "c9", "c10", "c11"],
        "D": ["d6", "d7", "d8", "d9", "d10", "d11"],
    },
    index=[6, 7, 8, 9, 10, 11],
)

tiga = pd.DataFrame(
    {
        "A": ["a12", "a13", "a14", "a15", "a16", "a17"],
        "B": ["b12", "b13", "b14", "b15", "b16", "b17"],
        "C": ["c12", "c13", "c14", "c15", "c16", "c17"],
        "D": ["d12", "d13", "d14", "d15", "d16", "d17"],
    },
    index=[12, 13, 14, 15, 16, 17],
)

bisnis = pd.DataFrame(
    {
        "Perusahaan": [
            "Telkom",
            "Telkom",
            "Pertamina",
            "BRI",
            "Pertamina",
            "KFC",
            "KFC",
            "Indosat"
        ],
        "Karyawan": [
            "Joko",
            "Budi",
            "Susi",
            "Iriana",
            "Bambang",
            "Burhanudin",
            "Intan",
            "Mukiman"
        ],
        "Usia": [44, 53, 67, 34, 60, 19, 20, 17]
    }
)

# Merging / Concatenation
# print(pd.concat(DataFrame))
# print(pd.concat([satu, dua, tiga]))

# Merging Data berdasarkan kesamaan
# menggunakan groupby()
# print(bisnis.groupby("Perusahaan"))
print(bisnis.groupby("Perusahaan").sum(numeric_only=True))
print(bisnis.groupby("Perusahaan").count())
print(bisnis.groupby("Perusahaan").mean(numeric_only=True))
print(bisnis.groupby("Perusahaan").min())
print(bisnis.groupby("Perusahaan").max())
print(bisnis.groupby("Perusahaan").describe())

# format dataframe
print(bisnis.groupby("Perusahaan").describe().transpose())

# bentuk dataframe yang miirip dengan dataframe SQL
data1 = pd.DataFrame(
    {
     "key": [
         "k0",
         "k1",
         "k2",
         "k3",
         "k4"
         ],
     
     "one": [ 1, 2, 3, 4, 5 ],
     "two": [ 6, 7, 8, 9, 10 ]
     }
)

data2 = pd.DataFrame(
    {
     "key": [
         "k0",
         "k1",
         "k2",
         "k3",
         "k4"
         ],
     
     "three": [ 1, 2, 3, 4, 5 ],
     "four": [ 6, 7, 8, 9, 10 ]
     }
)

print(data1)
print(data2)

# menggabungkan 2 dataframe dengan parameter "key"
# data_baru = pd.merge(left, right, how="inner", on="label/list/key")
data_baru = pd.merge(data1, data2, how="inner", on="key")
print(data_baru)


data3 = pd.DataFrame(
    {
     "key1": ["K0", "K0", "K1", "K2"],
     "key2": ["K0", "K1", "K0", "K1"],
     "A": ["A0", "A1", "A2", "A3"],
     "B": ["B0", "B1", "B2", "B3"]
     }
)

data4 = pd.DataFrame(
    {
     "key1": ["K0", "K1", "K1", "K2"],
     "key2": ["K0", "K0", "K0", "K0"],
     "C": ["C0", "C1", "C2", "C3"],
     "D": ["D0", "D1", "D2", "D3"]
     }
)

print(data3)
print(data4)

# inner join
# ketika kita memiliki 2 dataframe maka jika key nya sama dia akan
# menggabungkan key yang sama dalam dataframe tersebut

# left join
# mengambil dataframe yang pertama / awal
data_left = pd.merge(data3, data4, how="left", on=["key1", "key2"])
print(data_left)

# right join
# mengambil dataframe yang terakhir
data_right = pd.merge(data3, data4, how="right", on=["key1", "key2"])
print(data_right)

# outer join
# memasukkan inner join tetapi juga memasukkan baris yang lain yang tidak sama
data_outer = pd.merge(data3, data4, how="outer", on=["key1", "key2"])
print(data_outer)

# mengambil dataframe key berdasarkan index atau baris atau rows
bapak = pd.DataFrame(
    {
     "A": ["A0", "A1", "A2"],
     "B": ["B0", "B1", "B1"]
     }, index=["K0", "K1", "K2"]
)

ibu = pd.DataFrame(
    {
     "C": ["C0", "C1", "C2"],
     "D": ["D0", "D1", "D1"]
     }, index=["K0", "K2", "K3"]
)

print(bapak)
print(ibu)

# menggunakan join
print(bapak.join(ibu))
print(bapak.join(ibu, how="inner"))
