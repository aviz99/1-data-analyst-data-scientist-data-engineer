# 26 / 09 / 2023
# Day - 22
# OOP Encapsulation

# Encapsulation / Enkapsulasi pada oop
# Menyembunyikan sebagian detail yang dimiliki oleh sebuah object terhadap object lainnya.
# Atau sama hal nya dengan membuat semua variable pada class menjadi private
# cara mengakses nya menggunakan getter dan setter
# getter mengambil dan mengendalikan sebuah variable
# setter mengatur atau men-setting sebuah variable


from typing import Any


class Hero:
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    # method mengambil __name Hero
    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def underAttack(self, damageAttack):
        self.__health -= damageAttack

    def setAttack(self, attackPower):
        self.__attack = attackPower


# awal dari game
juggernaut = Hero("juggernaut", 50, 5)

# print(juggernaut.__dict__)

# game berjalan
# print(juggernaut.__name) # ini tidak bisa diakses maupun diambil
print(juggernaut.getName())
# juggernaut.setAttack(10)
juggernaut.underAttack(5)
print(juggernaut.getHealth())
