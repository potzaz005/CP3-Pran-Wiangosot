def login():
    username = (input("username : "))
    password = (input("password : "))
    if username == "potae" and password == "1234":
        return ShowMenu()
    else:
        return login()
def ShowMenu():
    print("----- PotaeShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    UserSelected = int(input(">> : "))
    if UserSelected == "1":
        return vatCalculate()
    else:
        return priceCalculate()
def vatCalculate(totalPrice):
    vat = 7 / 100
    result = totalPrice + (totalPrice * vat)
    return result

def priceCalculate():
    price1 = int(input("First Product Prics :"))
    price2 = int(input("Second Product Prics :"))
    return vatCalculate(price1 + price2)

print(login())