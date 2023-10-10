# 07/09/2023
# Day - 4
# Operasi manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "Muhaimin"
nama_kedua = "Wahab"
nama_akhir = "Abdullah"

nama_lengkap = nama_pertama + " " + nama_kedua + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap) # menghasilkan int
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator string

# mengecek apakah ada komponen char atau string di string
cekHuruf1 = "d"
status = cekHuruf1 in nama_lengkap # menghasilkan boolean
print("string "+ cekHuruf1 + " ada di " + nama_lengkap + " " + str(status))

cekHuruf2 = "m"
status = cekHuruf2 not in nama_lengkap # menghasilkan boolean
print("string "+ cekHuruf2 + " ada di " + nama_lengkap + " " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-10 : " + nama_lengkap[10])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0,3] : " + nama_lengkap[0:4])
print("index ke-[4,8] : " + nama_lengkap[4:8])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ") # menghasilkan int
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah : " + chr(data))

# 4. Operator dalam bentuk method
dataOne = "Rizal Iskandar Nofariza"
jumlah = dataOne.count("a") # menghasilkan int
print("Jumlah a pada " + dataOne + "= " + str(jumlah))