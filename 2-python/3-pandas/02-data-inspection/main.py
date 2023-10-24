# 24 / 10 / 2023
# Day - 33
# Data Inspection
import pandas as pd

dataku = pd.read_csv("kapal_titanic.csv")
print(dataku.head(3))
# print(dataku.tail(10))
# print(dataku)
pd.options.display.max_rows = 891
pd.options.display.min_rows = 891
print(pd.options.display.max_rows)
print(pd.options.display.min_rows)
# print(dataku)

# meringkas dataframe
print(dataku.info())

# mengetahui tipe data kapal_titanic.csv
# print(dataku.describe())

# non-numerik
print(dataku.describe(include="O"))
