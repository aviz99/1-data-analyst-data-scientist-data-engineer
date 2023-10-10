# 21 / 09 / 2023
# Day - 17
# Standard Library
import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now: {data_waktu}")
print(f"tahun: {data_waktu.year}")
print(f"hari: {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a", "b", "c", "d", "a", "d", "a"]

# count = 0
# for i in data:
#     if i == "a":
#         count += 1
# print(count)

# menggunakan package collections module Counter
data_count = Counter(data)
print(data_count)
print(f"jumlah a: {data_count['a']}")
print(f"jumlah d: {data_count['d']}")

# Baca text / file
import io

file = io.open("file_text.txt", "r")
print(file.read())
