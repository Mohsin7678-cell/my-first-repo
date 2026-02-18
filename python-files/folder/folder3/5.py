# marks = int(input("enter marks - "))
# if marks > 90:
#     print("grade-A")
# elif marks > 80:
#     print("grade-B")
# elif marks > 70:
#     print("grade-C")
# else:
#     print("grade-D")    
distance = int(input("enter the distance"))
if distance >= 400:
    print("i will go via flight")
elif distance > 300 and distance < 400:
    print("will go via train")
elif distance > 200 and distance <= 300:
    print("go via cab")
elif distance > 100 and distance <= 200:
    print("will go via personal car")
elif distance <= 100:
    print("will stay at home")