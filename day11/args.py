def terminal(pin, *args, **kwargs):
    allow = 1234
    if pin == allow:
        return 15000
 
    if args:
        kwargs["name"]
        return sum(args), kwargs
    else:
        return "Not correct pin"
print(terminal(124, 5000, 1000,15000, name = 'Sherboto'))
