# 25 / 09 / 2023
# Day - 21
# Study Case 10 - OOP Tkinter

# tkinter / Tk() = adalah object
# tkinter adalah sebuah package dari python
# tkinter adalah OOP
# val.Button = Class
# val.pack = Methods

import tkinter

main_window = tkinter.Tk()
print(main_window.__dict__)

label1 = tkinter.Label(main_window, text="label1")
label2 = tkinter.Label(main_window, text="label2")

tombol1 = tkinter.Button(main_window, text="tombol1")
tombol2 = tkinter.Button(main_window, text="tombol2")

# membuat positioning
# method positioning
# pack() tidak mempunyai return dan argument
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method untuk menampilkan layar nya / GUI
main_window.mainloop()
