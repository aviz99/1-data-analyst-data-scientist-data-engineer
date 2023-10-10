# 22 / 09 / 2023
# Day - 20
# OOP Methods
class Hero:
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance of variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # void function / method tanpa return dan tanpa argument
    def sayHi(self):
        print(f"namaku adalah {self.name}")

    # method dengan argument tanpa return
    def healthIncrease(self, up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("mars", 100, 82, 68)
hero2 = Hero("sven", 100, 80, 60)
hero3 = Hero("sladar", 100, 90, 70)
hero4 = Hero("grimmstroke", 100, 75, 73)

hero1.sayHi()
hero1.healthIncrease(50)
# print(hero1.health)
print(hero1.getHealth())
