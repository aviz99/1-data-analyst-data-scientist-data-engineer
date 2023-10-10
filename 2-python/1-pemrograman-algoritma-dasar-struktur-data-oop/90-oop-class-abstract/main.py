# 05 / 10 / 2023
# Day - 24
# OOP Class Abstract
# Abstract Class = dia akan memaksa class untuk mengimplementasikan methodnya
# abstract class tidak bisa diimplementasikan ke dalam object
# abstract class harus dibuat terlebihi dahulu class nya sehingga dia mengimplementasikan method yang ada di class abstract
# kegunaan membuat abstract class adalah kita jika misalkan punya PushButton atau tipe-tipe tombol tombol yang banyak dan kita sudah membuat design bahwa class yang berhubungan dengan button itu harus punya click
# ketika super class yang dibuat adalah abstract class maka method dari subclass akan dipaksakan menjadi method dari super class
# berguna untuk structure object oriented design
# seperti single turn, strategy pattern, observation pattern dll

# membuat class abstract
# import abc = abstract base class
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        # print("ini adalah button click")
        pass


# harus mengimplementasikan abstract method
class PushButton(Button):
    def click(self):
        print("ini adalah push button click")


tombol1 = PushButton()
tombol1.click()
help(tombol1)
# tombol2 = Button()
# tombol2.click()
