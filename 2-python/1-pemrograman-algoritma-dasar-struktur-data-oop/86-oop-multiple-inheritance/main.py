# 27 / 09 / 2023
# Day - 23
# OOP Multiple Inheritance


class A:
    def method_A(self):
        print("ini adalah method A")


class B:
    def method_B(self):
        print("ini adalah method B")


class Subclass(A, B):  # mengambil super class secara bersamaan (multiple inheritance)
    pass


objek = Subclass()

objek.method_A()
objek.method_B()
