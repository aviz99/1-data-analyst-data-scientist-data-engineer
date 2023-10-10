# 11 / 09 / 2023
# Day - 8
# Stacks & Queues

print(5 * "=" + "STACKS / TUMPUKAN" + 5 * "=")
# Stacks / Tumpukan
stack_tumpukan = [1, 2, 3, 4, 5, 6]
print(f"Data tumpukan sebelumnya: {stack_tumpukan}")

# memasukkan data baru
stack_tumpukan.append(7)
print(f"Data tumpukan masuk: {stack_tumpukan}")
print(f"Data tumpukan sekarang: {stack_tumpukan}")
stack_tumpukan.append(8)
print(f"Data tumpukan masuk: {stack_tumpukan}")
print(f"Data tumpukan sekarang: {stack_tumpukan}")
stack_tumpukan.append(9)
print(f"Data tumpukan masuk: {stack_tumpukan}")
print(f"Data tumpukan sekarang: {stack_tumpukan}")

# Mengeluarkan data yang paling akhir
keluar_akhir = stack_tumpukan.pop()
print(f"Data keluar: {keluar_akhir}")
print(f"Data tumpukan sekarang: {stack_tumpukan}")

# Queues / Antrian
from collections import deque

print("\n" + 5 * "=" + "QUEUES / ANTRIAN" + 5 * "=")

# deque = Menambah dan mengurangi didepan

queue_antrian = deque([1, 2, 3, 4, 5])
print(f"Data antrian sebelumnya: {queue_antrian}")

# Menambahkan data
queue_antrian.append(6)
print(f"Data antrian masuk: {queue_antrian}")
print(f"Data antrian sekarang: {queue_antrian}")
queue_antrian.append(7)
print(f"Data antrian masuk: {queue_antrian}")
print(f"Data antrian sekarang: {queue_antrian}")
queue_antrian.append(8)
print(f"Data antrian masuk: {queue_antrian}")
print(f"Data antrian sekarang: {queue_antrian}")

# Mengurangi antrian / queue
keluar_awal = queue_antrian.popleft()
print(f"Data keluar: {keluar_awal}")
print(f"Data antrian sekarang: {queue_antrian}")

keluar_setelah_nya = queue_antrian.popleft()
print(f"Data keluar: {keluar_setelah_nya}")
print(f"Data antrian sekarang: {queue_antrian}")

keluar_selanjut_nya = queue_antrian.popleft()
print(f"Data keluar: {keluar_selanjut_nya}")
print(f"Data antrian sekarang: {queue_antrian}")
