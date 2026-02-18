start = int(input("enter start : "))
end = int(input("enter end : "))

for num in range(start, end + 1):      # OUTER LOOP
    count = 0

    for i in range(1, num + 1):        # INNER LOOP
        if num % i == 0:                #Ab har number ke liye check karna hai:
            count = count + 1            #“Ye number kin-kin numbers se divide hota hai?”

    if count == 2:
        print(num, "is prime")


start = int(input("enter start : "))
end = int(input("enter end : "))

num = start
while num <= end:
    if num > 1:
        i = 2
        while i < num:
            if num % i == 0:
                break
            i += 1
        else:
            print(num, "is prime")
    num += 1
