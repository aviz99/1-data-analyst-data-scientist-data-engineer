# 25 / 09 / 2023
# Day - 21
# Study Case 9 - OOP Sederhana
# Game Sederhana Saling Serang
# kita memiliki 2 hero / karakter
# setiap hero dia punya:
# - nama
# - health
# - attack
# - defense
# kita akan membuat method
# method nya adalah membuat kedua hero tersebut menyerang satu sama lain
# jika hero 1 menyerang, hero 2 akan diserang
# jika hero 2 diserang akan bertahan
# sebalik nya jika hero 2 menyerang maka hero 1 diserang lalu dia akan bertahan
# kita harus menyampaikan bahwa hero 1 'sniper' menyerang ke hero 2 'rikimaru' begitu juga sebaliknya.
# self = object
# sekarang kita akan mengambil si power power nya itu (health, attack, defense)


class Hero:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attacking(self, opponent):
        print(self.name + " menyerang " + opponent.name)
        opponent.underAttack(self, self.attack)

    def underAttack(self, opponent, attack_op):
        print(self.name + " diserang " + opponent.name)
        attack_diterima = attack_op / self.defense
        print(f"serangan terasa : {str(attack_diterima)}")
        self.health -= attack_diterima
        print(f"darah {self.name} tersisa {str(self.health)}")


sniper = Hero("sniper", 100, 10, 5)
rikimaru = Hero("rikimaru", 100, 20, 10)

sniper.attacking(rikimaru)
print("\n")
rikimaru.attacking(sniper)
