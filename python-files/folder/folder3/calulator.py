print("Select operator")
print("addition :(+) \nsubtraction :(-) \nmultiplication :(*) \ndivision :(/)")
operator = input("enter operator : ")
num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
if operator == ("+"):
    print("addition of num1 and num2 is =", num1+num2)
elif operator == ("-"):
    print("subtraction of num1 and num2 is =", num1-num2)
elif operator == ("*"):
    print("multiplication of num1 and num2 is =", num1*num2)
elif operator == ("/"):
    print("division of num1 and num2 is =", num1/num2)
else:
    print("invalid option")