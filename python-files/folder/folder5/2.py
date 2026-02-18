print("welcome to our restaurent\nwe have many food items of your choice\n1. pizza\n2. burger\n3. hotdog")
pizza_price = 200
burger_price = 120
hotdog_price = 100

paneer_price = 40
mushroom_price = 30
capsicum_price = 25

single_cheese_price = 30
double_cheese_price = 50
soft_drinks = 40
choice = input("enter your choice ::")
if choice == "1":
    print("available topings are\na. paneer\nb. mushroom\nc. capsicum")
elif choice == "2" or choice == "3":
    print("available filings are\na. single layer cheese\nb. double layer cheese")


