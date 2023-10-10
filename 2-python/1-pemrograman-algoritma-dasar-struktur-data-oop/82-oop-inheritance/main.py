# 26 / 09 / 2023
# Day - 22
# OOP Inheritance


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


# membuat inheritance
class Hero_Intelligent(Hero):
    pass


class Hero_Strength(Hero):
    pass


lina = Hero("lina", 100)
techies = Hero_Intelligent("techies", 50)
axe = Hero_Strength("axe", 200)

print(lina.name)
print(techies.name)
print(axe.name)
# print(help(axe))
# print(help(techies))
