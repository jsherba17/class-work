film = ["horror","detective","comedy"]
t = [0,24]
a = input("What would you like?: horror, detective, comedy:   ")
if a == film[0] or a == film[1] or a == film[2]:
    time = int(input("What time would you like? 0-24:   "))
if time >= 21:
    print("500 som")
elif time < 21:
    print("300 som")
else:
    print("bye!")
