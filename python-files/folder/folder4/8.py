a = float(input("enter side 1 :: "))
b = float(input("enter side 2 :: "))
c = float(input("enter side 2 :: "))
if a+b>c and a+c>b and b+c>a:
    print("it is a triangle")
else:
    print("it is not a triangle")