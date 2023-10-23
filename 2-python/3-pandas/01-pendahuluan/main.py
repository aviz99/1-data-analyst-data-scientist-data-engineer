# 23 / 10 / 2023
# Day - 32
# Pendahuluan Pandas

# Apa itu Pandas ?
# Library di Python khusus untuk data analysis & manipulation data (mengolah data) sehingga nanti kita bisa mendapatkan insight dari data yang kita miliki
# Dibangun di atas Numpy
# Dengan Pandas, maka Python akan menjadi seperti R
# biasa nya digunakan untuk deep learning, machine learning, menganalisis statistik, membaca format file csv, membaca file database seperti sql,monngo db dll, html atau dari website dan cloud computing

# Install beberapa library
# Excel = openpyxl, xlrd
# HTML = lxml, html5lib, BeautifulSoup4
# SQL = Sqlalchemy
# pip install pandas
# pip install (openpyxl, xlrd, lxml, html5lib, BeautifulSoup4, Sqlalchemy)

import pandas as pd
from sqlalchemy import create_engine

# membaca file kapal_titanic.csv
data = pd.read_csv("kapal_titanic.csv")
# print(data)

# menggunakan file kapal_titanic.csv di 5 awal pertama
# print(data.head())
# menggunakan file kapal_titanic.csv di 5 file terakhir
# print(data.tail())

# cara mengexport file data ke file lain dengan format - format yang berbeda - beda
# print(data.to_csv("datakucsv.csv", index=False))
dataku = pd.read_csv("datakucsv.csv")
# print(dataku)
# print(data.to_excel("dataexcel.xlsx", index=False, sheet_name="asik"))
# print(pd.read_excel("dataexcel.xlsx"))

# membaca file html
# datahtml = pd.read_html(
#     "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
# )
# print(datahtml)

# export menjadi SQL
mesin_sql = create_engine("sqlite:///:memory:")
print(mesin_sql)
print(data.to_sql("datasql", con=mesin_sql))
print(pd.read_sql("datasql", con=mesin_sql))
