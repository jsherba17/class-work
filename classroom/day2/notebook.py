brand ="Lenovo"
model = "Ideapad"
series = "s145"
ram = "8Gb"
ssd = "256Gb "
hdd = "1Tb "
vc = "Nvidia GeForce 1050Ti "
price = "500$"
fnb = [brand,model,series,ram,ssd,hdd,vc,price]
print(", ".join(fnb))
user =  (int(input("Would you like buy it? Answer: 1 or 0 ")))
if user == 1:
    print('Thank you for your purchase!')
elif user == 0:
    print('Thank you for visit!')
else:
    print('Bye!')
