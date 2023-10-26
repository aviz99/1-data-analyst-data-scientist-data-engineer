# 26 / 10 / 2023
# Day - 35
# Menyertakan Prefix & Suffix Pada Seluruh Kolom DataFrame
import pandas as pd
import numpy as np

# persiapan Data Frame
n_rows = 5
n_cols = 5
cols = tuple("ABCDE")
df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                  columns=cols)
print(df)

# menyertakan prefix kolom
# prefix adalah string didepan suatu string tertentu
print(df.add_prefix("Kolom_"))

# menyertakan suffix kolom
# suffix adalah sekumpulan string dibagian belakang
print(df.add_suffix("_Field"))