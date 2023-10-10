# 21 / 09 / 2023
# Day - 19
# OOP Pendahuluan
class Hero:  # template
    pass


hero1 = Hero()  # object / instance (instanciate)
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "invoker"
hero3.health = 300

print(hero1)
print(hero1.__dict__)
print(hero1.name)
