# 21 / 09 / 2023
# Day - 19
# Write External File

# 1. mode write
# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya
with open("data_1.txt", mode="w", encoding="utf-8") as file:
    file.write("apa kabs ?")

with open("data_1.txt", mode="w", encoding="utf-8") as file:
    file.write("gimans kabs ?")

with open("data_1.txt", mode="w", encoding="utf-8") as file:
    file.write("overwrite")

# 2. mode append
with open("data_2.txt", mode="a", encoding="utf-8") as file:
    file.write("apa kabs ?\n")
with open("data_2.txt", mode="a", encoding="utf-8") as file:
    file.write("gimans kabs ?\n")
with open("data_2.txt", mode="a", encoding="utf-8") as file:
    file.write("ini akan menambah lagi dengan append\n")


# 3. mode r+

with open("data_3.txt", mode="w", encoding="utf-8") as file:
    file.write("data ketiga\n")

with open("data_3.txt", mode="r+", encoding="utf-8") as file:
    # data = file.read()
    # file.write("menambah dengan r+")
    # print(data)
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")
    file.write("baris ke-3\n")

with open("data_3.txt", mode="r+", encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt", mode="r+", encoding="utf-8") as file:
    file.write("otong")  # menimpa isi text sesuai dengan panjang data
