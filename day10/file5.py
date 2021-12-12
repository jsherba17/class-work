import os
import random


path = "/home/jsherba/Desktop/problem5"
os.mkdir(path)

lst =  ['first.py','second.py','third.py','forth.py','fifth.py']

#for i in range(5):
name = random.choice(lst)
print(name)
lst.remove(name)

file = open(path+'/first.py' , "w")
file = open(path+'/second.py' , 'w')
file = open(path+'/third.py' , 'w')
file = open(path+'/forth.py' , 'w')
file = open(path+'/fifth.py' , 'w')
file.write("hello world!")
file.close()
