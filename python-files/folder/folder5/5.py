print("1. Pizza")
print("2. Burger")
print("3. Hotdog")

choice = input("Enter your choice: ")
total = 0

if choice == "1":
    total = 200
    print("Toppings:")
    print("1. Paneer")
    print("2. Mushroom")
    print("3. Capsicum")
    t = input("Choose topping: ")

    if t == "1":
        total = total + 40
    elif t == "2":
        total = total + 30
    elif t == "3":
        total = total + 25

elif choice == "2":
    total = 120
    print("Fillings:")
    print("1. Single cheese")
    print("2. Double cheese")
    f = input("Choose filling: ")

    if f == "1":
        total = total + 30
    elif f == "2":
        total = total + 50

elif choice == "3":
    total = 100
    print("Fillings:")
    print("1. Single")