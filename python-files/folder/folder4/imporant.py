#!A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and 
#!Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys 
#!if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys,
#!a discount of 5% is given,and a discount of 10% is given on orders for electrical charging based toys
#!of value more than Rs. 500. Assume that the numeric codes 1, 2 and 3 are used for battery based toys,
#!key-based toys, and electrical charging based toys respectively. Write a program that reads the 
#!product code and the order amount and prints out the net amount that the customer is required 
#!to pay after the discount.










print("battery based toys  :: you will get a discount of 10% when you buy more than 1000Rs \nkey based toys      :: you will get a discount of 5% when you buy more than 100 Rs \nelectric based toys :: you will get a discount of 10% when you buy more than 500 Rs")

choice=input("a::battery based toys\nb::key based toys\nc::electric based toys\n enter your choice : ")

orderamount = float(input("enter orderamount : "))
if choice == "a":
    if orderamount > 1000:
        print("you will get a 10% discount\nyour final amount that you have to pay is",orderamount-orderamount*10/100)
    else:
        print("you will not get any discount\nyour final amount that you have to pay is",orderamount)
elif choice == "b":
    if orderamount > 100:
        print("you will get a 5% discount\nyour final amount that you have to pay is",orderamount-orderamount*5/100)
    else:
        print("you will not get any discount\nyour final amount that you have to pay is",orderamount)
elif choice == c:
    if orderamount > 500:
        print("you will get a 10% discount\nyour final amount that you have to pay is",orderamount-orderamount*10/100)
    else:
        print("you will not get any discount\nyour final amount that you have to pay is",orderamount)
print("thank you for shopping.....\nhave a nice day.....")