# 26 / 09 / 2023
# Day - 22
# Study Case 11 - OOP Encapsulation


class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attack, armor):
        self.__name = name
        self.__healthStandard = health
        self.__attackStandard = attack
        self.__armorStandard = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandard * self.__level
        self.__attack = self.__attackStandard * self.__level
        self.__armor = self.__armorStandard * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {} : \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__healthMax,
            self.__attack,
            self.__armor,
        )

    # method untuk mengambil exp
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandard * self.__level
            self.__attack = self.__attackStandard * self.__level
            self.__armor = self.__armorStandard * self.__level

    def attacking(self, enemy):
        self.gainExp = 50


slardar = Hero("slardar", 100, 5, 10)
undying = Hero("undying", 100, 5, 10)
print(slardar.info)
slardar.attacking(undying)
slardar.attacking(undying)
slardar.attacking(undying)
print(slardar.info)
# print(slardar.__dict__)
