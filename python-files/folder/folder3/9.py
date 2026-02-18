num = int(input("enter number"))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
    if num % 7 == 0:
        print("number is divisible by seven")
        cube = num**3
        print("cube of this num is",cube)
    else:print("number is not divisible by seven")
   

