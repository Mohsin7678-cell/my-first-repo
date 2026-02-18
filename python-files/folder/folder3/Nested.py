distance = int(input("enter distance : "))
if distance > 500:                    #jb distance flight k liye aa jae tb input aaega 
    print("i will go via flight")     #ki kon si flight hai uske baad condition aaegi ki  
    flight =(input("enter flight : "))#kon si flight hai iske liye if and elif likhenge
    if flight == ("indigo"):          #but ye wala if and elif first wale if k andar aaega
        print("i will carry food")    #and jb flight k distance wali condition khatm 
    elif flight == ("vistara"):       #ho jaei to train ,car ets wali condition that is   
        print("food is given")        #elif ,first wale if k exact neeche aaega
    elif flight == ("air india"):     # 
        print("carry only snacks")    #
elif distance < 500 and distance > 400:
        print("i will go via train")
elif distance < 400 and distance > 300:
    print("i will go via car")
elif distance < 300 and distance > 200:
    print("i will go via walk")
elif distance < 200 and distance > 100:
    print("i will stay at home")
    