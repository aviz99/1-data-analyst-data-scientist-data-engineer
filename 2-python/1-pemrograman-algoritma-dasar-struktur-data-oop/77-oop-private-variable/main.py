# 25 / 09 / 2023
# Day - 21
# OOP Private Variable


class Hero:
    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "private"
        # variable instance protected
        self._protected = "protected"


lina = Hero("lina", 100)
# print(lina.__dict__)
# lina.private = "testing" # assignment variable diluar dari class
# lina.__private = "testing"  # assignment variable diluar dari class
# print(lina.__dict__)
# print(lina.__private)
# print(lina.private)
print(lina.__dict__)
# print(lina._protected)
# lina._protected = "testing"
# print(lina.__dict__)
# print(lina._protected)
print(Hero.__dict__)
print(Hero.__privateJumlah)
