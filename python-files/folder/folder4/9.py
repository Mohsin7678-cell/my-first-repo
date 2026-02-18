a = float(input("enter side 1 :: "))
b = float(input("enter side 2 :: "))
c = float(input("enter side 3 :: "))
if a==b==c:
    print("triangle is equiateral")
elif a==b or b==c or a==c:
    print("triangle is isosceles")
else:
    print("triangle is scalene")
