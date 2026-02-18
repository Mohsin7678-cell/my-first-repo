distance = int(input("enter the distance"))
if distance >= 400:
    print("i will go via flight")
elif distance >=300:
    print("will go via train")
elif distance >=200:
    print("go via cab")
elif distance >=100:
    print("will go via personal car")
elif distance < 100:
    print("will stay at home")