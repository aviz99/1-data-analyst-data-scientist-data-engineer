# 21 / 09 / 2023
# Day - 19
# OOP Class Instance Variable
class Hero:
    # static variable
    # kegunaan dari static variable adalah memeriksa sebuah nilai
    # contoh variable static dibawah ini
    # class variable
    jumlah = 0

    # ini instance of variable
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance of variable = variable didalam object
        # contoh instance of variable dibawah ini
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print(f"membuat object dengan nama {inputName}")


hero1 = Hero("sniper", 100, 85, 45)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 70, 40)
print(Hero.jumlah)
hero3 = Hero("invoker", 100, 75, 50)
print(Hero.jumlah)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
# print(Hero.__dict__)
