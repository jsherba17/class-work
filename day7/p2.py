lista  = [100, 1.92, 'eat', True, {'key':'non'}]
for i in lista:
    if type(i) not in [bool, int, float]:
            print(i, 'ACCEPT')
    else:
        print(i, 'NOT ACCEPT')
