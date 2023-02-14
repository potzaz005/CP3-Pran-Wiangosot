username = (input("username"))
password = (input("password"))
if username =="potae" and password =="1234":
    print("Welcome")
    print("1.Apple 10 THB")
    print("2.Banana 5 THB")
    UserSelected = int(input("What do you want"))
    if UserSelected ==1:
        Apple = int(input("unit"))
        price = 10
        result = Apple * price
        print(result)
    elif UserSelected ==2:
        Banana = int(input("unit"))
        price = 5
        result = Banana * price
        print(result)

