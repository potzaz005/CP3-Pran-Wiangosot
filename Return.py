def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
totalPrice = int(input("Your Total Price"))
print(vatCalculate(totalPrice))