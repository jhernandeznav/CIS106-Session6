# activity 2
def fun_unit_price(quantity):
    if int(quantity) > 1000:
        unit_price = 8.00
    elif int(quantity) >= 500:
        unit_price = 10.00
    else:
        unit_price = 12.00
    return unit_price


quantity = input("Enter the quantity:")

unit_price = fun_unit_price(quantity)

e_price = int(unit_price) * int(quantity)

print("Quantity ordered:", quantity)
print("Unit price: $", unit_price)
print("Extended price: $", e_price)
