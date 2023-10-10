# 26 / 09 / 2023
# Day - 22
# OOP Staticmethod & Classmethod


class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk object tetapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) = akan nempel ke object dan class nya
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    # class method = akan nempel ke class nya aja
    @classmethod
    def getJumlah3(item):  # polymorphism = dianggap class bisa dianggap object bisa
        return item.__jumlah


sniper = Hero("sniper")
print(Hero.getJumlah2())
rikimaru = Hero("rikimaru")
print(sniper.getJumlah2())
ursa = Hero("ursa")
print(Hero.getJumlah3())
print(ursa.getJumlah3())
