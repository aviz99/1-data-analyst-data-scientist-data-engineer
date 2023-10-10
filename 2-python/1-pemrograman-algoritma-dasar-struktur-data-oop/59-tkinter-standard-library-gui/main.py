# 05 / 10 / 2023
# Day - 25
# Tkinter Standard Library Python GUI

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
# menginstance tkinter
window = tk.Tk()

# merubah sesuatu
window.configure(bg="white")

# merubah ukuran
window.geometry("300x200")

# menentukan ukuran yang tidak bisa diubah ubah
# window.resizable(sumbuX, sumbuY)
window.resizable(False, False)

# memberikan judul
window.title("Sopo Jenengan!")

# membuat frame
# frame input
input_frame = ttk.Frame(window)
# penempatan grid, pack, place
# penempatan pack
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen - komponen
# variable & function
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


def tombol_click():
    # print(NAMA_BELAKANG.get())
    """fungsi ini akan dipanggil oleh tombol"""
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, anjayyyyy!"
    showinfo(title="Whazzup!", message=pesan)


# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. Entry untuk nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. Entry untuk nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)


# 5. Tombol
tombol_sopo = ttk.Button(input_frame, text="Sopo!", command=tombol_click)
tombol_sopo.pack(fill="x", expand=True, padx=10, pady=10)

# menampilkan GUI atau main loop window
window.mainloop()
