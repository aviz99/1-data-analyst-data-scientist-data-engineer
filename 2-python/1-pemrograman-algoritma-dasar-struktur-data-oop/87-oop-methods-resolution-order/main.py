# 30 / 09 / 2023
# Day - 24
# OOP Methods Resolution Order

# multiple inheritance => methods resolution order


class A:
    def show(self):
        print("ini adalah show A")


class B:
    def show(self):
        print("ini adalah show B")


class C(B, A):
    pass


objek = C()
objek.show()
# methods resolution order
# dimana kita liat urutan eksekusinya itu kita bisa tampilkan disini
# method resolution order yang di-inherit ke sebuah class itu tergantung dari urutan sub-class nya
# help(objek)
