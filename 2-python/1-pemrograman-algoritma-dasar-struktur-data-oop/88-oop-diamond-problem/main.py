# 30 / 09 / 2023
# Day - 24
# OOP Diamond Problem


class A:
    def show(self):
        print("ini adalah show A")


class B(A):
    print("ini adalah show B")


class C(A):
    print("ini adalah show C")


class D(B, C):
    pass


objek = D()
objek.show()
help(objek)
