def dic(dict1,dict2):
    dict1.update(dict2)
    return dict1
print(dic({'key':1},{'hi':2}))
