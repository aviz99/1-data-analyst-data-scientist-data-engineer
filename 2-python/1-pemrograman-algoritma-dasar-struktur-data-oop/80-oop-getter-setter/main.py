# 26 / 09 / 2023
# Day - 22
# OOP Getter & Setter


class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.name, self.__health)

    # def getHealth(self):
    #     return self.__health

    # @property,@.getter,@.setter,@staticmethod,@classmethod,@deleter = decorator
    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di hilangkan")
        self.__armor = None


sniper = Hero("sniper", 100, 10)
# print(sniper.getHealth())
print("merubah info")
print(sniper.info)
# sniper.name = "pance pondaag"
print(sniper.info)
# sniper.info = "info"

print("getter & setter untuk __armor:")
print(sniper.armor)
# print(sniper.__dict__)
# sniper.armor = 10
sniper.armor = 50
print(sniper.armor)

print("hilang armor")
del sniper.armor
print(sniper.__dict__)
