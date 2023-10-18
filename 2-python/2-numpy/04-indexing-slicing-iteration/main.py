# 18 / 10 / 2023
# Day - 29
# Indexing, Slicing & Iteration

import numpy as np

a_array_biasa = np.arange(10) ** 2
print(a_array_biasa)

# mengambil nilai
print(f"elemen ke-1 dari a adalah: {a_array_biasa[0]}")
print(f"elemen ke-7 dari a adalah: {a_array_biasa[6]}")
print(f"elemen terakhir dari a adalah: {a_array_biasa[-1]}")

# slicing
print(
    f"elemen dari 1 sd 6 adalah: {a_array_biasa[0:6]}"
)  # exclusive dia mengambil dari nilai awal sampai nilai sebelum akhir
print(f"elemen dari ke-4 sd terakhir: {a_array_biasa[3:]}")
print(f"elemen dari awal sd ke-5: {a_array_biasa[:5]}")

# iteration
for i in a_array_biasa:
    print(f"value: {i}")
