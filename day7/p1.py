l = []
s = set()
for i in range(1,6):
    x = int(input("Введите число: "))
    l.append(x)
    s.update(l)
min_word = min(s)
print(s,min_word)
