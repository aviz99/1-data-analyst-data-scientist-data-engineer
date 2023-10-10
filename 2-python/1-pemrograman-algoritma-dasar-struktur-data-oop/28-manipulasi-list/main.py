# 11 / 09 / 2023
# Day - 8
# Manipulasi List

# index berawal dari 0
data = ["C++","Java","Python"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) : {data_0}")
data_terakhir = data[2]
print(f"data terakhir (index 2) : {data_terakhir}")

# mengetahui info jumlah data pada list
panjang_data = len(data)
print(f"Jumlah seluruh data : {panjang_data}")

## manipulasi data pada sebuah list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah :\n{data}")
    # data.insert(posisi,item)
data.insert(1,"Javascript")
print(f"data sesudah ditambah :\n{data}")

# menambahkan item diakhir list
    # data.append(item)
data.append("SQL")
print(f"data ditambah ke akhir index :\n{data}")

# menggabung list dengan list
data_baru = ["PHP","MongoDB","Haskell"]
    # data.extend(data)
data.extend(data_baru)
print(f"data + data_baru :\n{data}")

# merubah data
# ubah data ke-2 menjadi ruby
    # data[index] = new_item
data[2] = "Ruby"
print(f"data setelah diupdate :\n{data}")

# menghapus / remove / delete sebuah data
# huruf besar dan kecil berpengaruh
    # data.remove(item)
data.remove("MongoDB")
print(f"data setelah diremove :\n{data}")

# menghapus data paling belakang
data.pop()
print(f"data akhir setelah diremove :\n{data}")
