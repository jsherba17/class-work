t = """bin   cdrom  etc   lib    lib64   lost+found  mnt  proc  run   snap  swapfile  tmp  var
hghghghghgboot  dev    home  lib32  libx32  media       opt  root  sbin  srv   sys  usr"""
my_file = open('qwerty.txt', 'w')
my_file.write(t)
my_file.close()

my_file = open("qwerty.txt", 'r')
txt = my_file.read()
print(txt)
my_file.close()


with open('qwerty.txt', 'r') as my_file:
    f = my_file.read()
    print(f)
