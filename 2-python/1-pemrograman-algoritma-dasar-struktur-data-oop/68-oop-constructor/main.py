# 21 / 09 / 2023
# Day - 19
# OOP Constructor


# self pada class = untuk mengakses ke atribut dan method pada setiap objek yang dibuat
class Hero:
    def __init__(
        self, inputName, inputHealth, inputPower, inputArmor
    ):  # __init__ mengeksekusi pertama kali si object itu dibuat
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper", 100, 80, 45)
hero2 = Hero("mirana", 100, 75, 40)
hero3 = Hero("invoker", 100, 65, 68)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
