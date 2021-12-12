months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
months_a.update(months_b)
months_a.add('Dec')


x ={1,2,3}
y ={4,3,6}
c =x.intersection(y)
print(months_a,c)
