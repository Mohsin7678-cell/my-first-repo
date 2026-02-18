prev = int(input("Enter previous meter reading: "))
curr = int(input("Enter current meter reading: "))

units = curr - prev
print("Units consumed:", units)

if units <= 100:
    bill = units * 0.5

elif units <= 200:
    bill = 50 + (units - 100) * 1

elif units <= 300:
    bill = 150 + (units - 200) * 1.5

else:
    bill = 300 + (units - 300) * 2

print("Electricity Bill = Rs.", bill)
