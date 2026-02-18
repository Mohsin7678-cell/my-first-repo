print(" battery based :: a discount of 10% of the order more than 1000 Rs\nkey-based toys                                                                                                                   ::a discount of 5% is given on the order greater than 100  Rs\nelectrical charging based toys  ::  a discount of 10% on the order more tahn 500 rs    ")
choice=input("which type of toy would u like to buy  ...\n b ::  battery based\nk :: key based\n e :: electrical based ")
order_amount=float(input("enter your order amount "))
if choice=="b":
    if order_amount>1000:
        d=10*100/order_amount
        print("ur final amount u have to pay is ",round(order_amount-d,2))
    else:
        print("no discount on ur order :: so ur final amount u have to pay is ",order_amount)
elif choice=="k":
    if order_amount>100:
        d=5*100/order_amount
        print("ur final amount u have to pay is ",round(order_amount-d,2))
    else:
        print("no discount on ur order :: so ur final amount u have to pay is ",order_amount)
elif choice=="e":
    if order_amount>500:
        d=10*100/order_amount
        print("ur final amount u have to pay is ",round(order_amount-d,2))
    else:
        print("no discount on ur order :: so ur final amount u have to pay is ",order_amount)
else:
    print("sory this type of toys is not available")






