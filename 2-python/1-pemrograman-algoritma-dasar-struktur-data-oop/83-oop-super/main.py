# 26 / 09 / 2023
# Day - 22
# OOP Super


# Super = adalah mengambil class utama atau class parent-nya
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(self.name, self.health))


class Hero_Intellegent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        super().showInfo()


class Hero_Strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().showInfo()


lina = Hero_Intellegent("lina")
axe = Hero_Strength("axe")

# print(lina.name, " ", lina.health)
# print(axe.name, " ", axe.health)
