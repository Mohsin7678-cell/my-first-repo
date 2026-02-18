distance = int(input("enter distance : "))
if distance > 500:                   
    print("i will go via flight")     
    flight =(input("enter flight : "))
    if flight == ("indigo"):          
        print("i will carry food")   
    elif flight == ("vistara"):       
        print("food is given")       
    elif flight == ("air india"):     
        print("carry only snacks")    
elif distance < 500 and distance > 400:
        print("i will go via train")
        
elif distance < 400 and distance > 300:
    print("i will go via car")
    wheather = (input("enter wheather : "))
    if wheather == ("sunny"):
        print("will go directly")
    elif wheather == ("rainy"):           #isme else nhi aa ya elif aya hai kuki agar else aa jata
        print("take a break and then go") #to uska matlab hota sunny k alva baki saare season pr isme
elif distance < 300 and distance > 200:   #elif aaya hai jiska matlba hua hai sunny k alava bs koi ek
    print("i will go via walk")           #aur season that is rainy only
    road = (input("enter road : "))
    if road == ("dry"):
        print("walk on the same road")
    elif road == ("wet"):
        print("walk on another road")
elif distance < 200 and distance > 100:
    print("i will stay at home")