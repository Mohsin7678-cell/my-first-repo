print("welcome to our restaurant")
print("we have many food items of your choice")
print("1. pizza\n2. burger\n3. hotdog")

# prices
pizza_price = 200
burger_price = 120
hotdog_price = 100

paneer_price = 40
mushroom_price = 30
capsicum_price = 25

single_cheese_price = 30
double_cheese_price = 50

softdrink_price = 20

choice = input("enter your choice :: ")

total = 0

if choice == "1":
    total = pizza_price
    print("available toppings are")
    print("a. paneer\nb. mushroom\nc. capsicum")
    top = input("choose topping :: ")

    if top == "a":
        total = total + paneer_price
    elif top == "b":
        total = total + mushroom_price
    elif top == "c":
        total = total + capsicum_price

elif choice == "2":
    total = burger_price
    print("available fillings are")
    print("a. single layer cheese\nb. double layer cheese")
    fill = input("choose filling :: ")

    if fill == "a":
        total = total + single_cheese_price
    elif fill == "b":
        total = total + double_cheese_price

elif choice == "3":
    total = hotdog_price
    print("available fillings are")
    print("a. single layer cheese\nb. double layer cheese")
    fill = input("choose filling :: ")

    if fill == "a":
        total = total + single_cheese_price
    elif fill == "b":
        total = total + double_cheese_price

side = input("do you want softdrink? (y/n) :: ")
if side == "y":
    total = total + softdrink_price

print("your total bill amount is Rs.", total)
