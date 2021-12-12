import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

for i in range(4):
    name = random.choice(names)
    print(name)
    names.remove(name)

