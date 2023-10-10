# 26 / 09 / 2023
# Day - 22
# OOP Override Methods
# override / overriding methods = adalah menimpah fungsi atau methods atau class atau sub class yang ada di super class
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(self.name, self.health))


class Hero_Intellegent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)  # mengambil methods dari super class

    # menimpah sebuah methods pada super class
    # override
    def showInfo(self):
        print("showInfo di subclass Hero_Intellegent")
        print("{} \n\tTipe: intellegent, \n\tHealth: {}".format(self.name, self.health))


class Hero_Strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = Hero_Intellegent("lina")
axe = Hero_Strength("axe")

lina.showInfo()
axe.showInfo()
