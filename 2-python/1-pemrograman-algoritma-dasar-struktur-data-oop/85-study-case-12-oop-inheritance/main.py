# 26 / 09 / 2023
# Day - 22
# Study Case 12 - OOP Inheritance
from hero import HeroIntelligent, HeroStrength

lina = HeroIntelligent("lina")
slardar = HeroStrength("slardar")

lina.showInfo()
slardar.showInfo()

lina.gainExp = 200
slardar.gainExp = 250

lina.showInfo()
slardar.showInfo()
