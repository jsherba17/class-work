print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
print('off "0"')
s = input("Знак (+,-,*,/): ")
if s == '0':
if s in ('+', '-', '*', '/'):
x = float(input("x="))y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("нельзя!")

exit(0)
sys.exit
os.abort()
