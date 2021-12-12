import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
d = dict()
for i in range(4):
    name = random.choice(names)
    d.update(name)
    print(d)
