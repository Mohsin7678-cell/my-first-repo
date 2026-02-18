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


#! WAP to display those numbers which are divisible by 7 only or 3 only,
#! by both 7 and 3, neither by 7 nor 3 from the range entered by user 
#! and also display the count of each of them

start = int(input("enter start : "))              
end = int(input("enter end : "))                        
for num in range(start,end+1):                     
    if num%7 == 0 and num%3 == 0:                     
      print(num,"is divisible both 7 and 3\n")          
    elif num%7  == 0:                                    
      print(num,"is divisible by 7\n")                
    elif num%3 == 0:                                 
        print(num,"is divisible by 3\n")             
    elif num%7 != 0 and num%3 != 0:                     
      print(num,"is not divisible both 7 and 3")
      
      #! Wap to find factors
num = int(input("enter num that you want its factors :: "))
count = 0
for i in range(1,num+1):                       #remember factors and factorial are different
    if num%i == 0:
        count = count+1
        print("factors of this num is",i)
print("total factors is",count)
if count == 2:                               # to find number is prime or not(composite)
    print("number is prime")
else:
    print("number is composite")
    
    
#! wap to display the sum of even mumbers present in the list 
#! and display average of odd numbers
    
    l = [1,2,3,4,5,6,7,8,9,]
add = 0
for num in l:            # 'num'tabhi exist krega jab 'for' loop start hoga isiliye agar 'if' me 
  if num%2 == 0:              #  'num'use ho rha hai to 'if' se pehle 'for' loop aaega
    add = add+num
print("addition of even num is",add)   #agar print if loop k andar hoga to code kuch aisa hoga
                                                    #addition of even num is 2
                                                    #addition of even num is 6
   #this code is incorrect ,                         #addition of even num is 12
    # sahi code niche likha ha                       #addition of even num is 20
                                                      #isiliye print starting se likho
                                                      
#! wap to display sum of even numbers and average of odd numbers
l = [1,2,3,4,5,6,7,8,9,]  
add_e= 0
add_o=0
count_e = 0
count_o = 0                           #pehle code me dekho last line print wali hai agar print aise
for num in l:                          # hi beech me aa jaega to if condition break ho jaega  
    if num%2 == 0:                      #isiliye if aur else ek saath likh kr print baad me likhenge
        add_e= add_e+num
        count_e=count_e+1                    
    else:
        add_o = add_o+num
        count_o=count_o+1
print("sum of even num is",add_e)
print("sum of odd num is",add_o)
average=add_o/count_o
print(average)
print("total even is",count_e)
print("total odd is",count_o)

#! wap to print days in all months
l = ["jan","feb","march","april","may","june","july","august","spetember","october","november","december"]
for i in l:
    if i == ("feb"):
        print(i,"has 28 days")
    elif i in ("jan","march","may","july","august","october","december"):
        print(i,"has 31 days")
    else:
        print(i,"has 30 days")
#if ,elif k andar tuple nhi aa sakta to isiliye agar likhna hai to double equal ko remove krk
# uski place pr 'in' likh do                                                 

#! wap to display sequence as: 4/2,7/2,10/2,13/2.........n(take input)
n = int(input("enter number"))
add = 1
for i in range(n):
    add = add+3
   # print(add,"/2",end=",")      #print me 'add' ki jagah pr pehle 'i' likh rha tha me pr 'i' to poori
    print(f"{add}/2",end=",")     # series hai (1,2,3,4,5,....) aur mujhe bs add hue number print 
                                  # krwane hai isiliye 'add' aaega
#jo print commented hai usme add k baad comma hai to output me space aa jaega(4 /2) aise , 
# pr 'f' use krne se ye htt jata hai


#!wap to add add inputs
n = int(input("enter number"))
add = 1
for i in range(n):
    add = add+3
   # print(add,"/2",end=",")      #print me 'add' ki jagah pr pehle 'i' likh rha tha me pr 'i' to poori
    print(f"{add}/2",end=",")     # series hai (1,2,3,4,5,....) aur mujhe bs add hue number print 
                                  # krwane hai isiliye 'add' aaega
#jo print commented hai usme add k baad comma hai to output me space aa jaega(4 /2) aise
# pr 'f' use krne se ye htt jata hai

 #! wap to take ur name from the user and display the vowel in it and also display the count as well     
name = (input("enter your name : "))
count_v= 0
count_c=0
for ch in name:
    if ch in("AEIOUaeiou"):              #("A","E","I","O","U","a","e","i","o","u"):
        print(ch,"is a vowel")         
        count_v=count_v+1                 
        count_c=count_c+1                # this program is for one word
    else:
        print(ch,"is a consonant")
print("total count_v is",count_v)
print("total count_c is",count_c)



l=["happy","angry","crying","surprised"]
count_v = 0
count_c = 0
for word in l:
    for ch in word:
        if ch in"a,e,i,o,u,A,E,I,O,U":    # this prog is for many words
            print(ch,"is a vowel")
            count_v=count_v+1
        else:
          print(ch,"is a consonant")
        count_c=count_c+1
print("total count_v is",count_v)
print("total count_c is",count_c) 
       


## wap to display factorials of the number entered by user
num = int(input("enter number : "))
mult=1
for i in range(num,0,-1):
    mult=mult*i
    print(i,end="x" if i !=1 else"")
print("=",mult)


## wap to reverse of a number entered bu user
    
num = int(input("enter three number"))
A1 = num%10
A2 = num//10%10  # // iska matlab floor division , ye decimal part ko hta deta hai
A3 = num//100
print(f"reverse of number is {A1}{A2}{A3}")    # f srting me hr variable ko ek alag
                                               # bracket me likhna padta hai
                                               
                                               
###
# for i in 'balmeet':
#     print(i)               # balmeet print hoga uske baad continue ka kaam khatm kuki  
#     continue               # for loop me itna hi tha print krwane k liye , to ab last time
#     #print('balmeet')      # jb loop chla tha tb 'i' me 't' reh gya tha , isiliye last
# print(i)                   # wale print(i) me 't' ptint hoga

 
# for i in 'balmeet':
#      continue           loop balmeet me 'b' se lekr 't' tk chlega pr sb kuch skip ho jaega
# print(i)                due to continue and last me sirf 't' print hoga


#### registration and login
username = input("enter user name : ")
password = input("enter password : ")
print("registration sucessfull")
attempt = 0
while True:
    if attempt>=3:
        print("you tried too much\ntry again later")
        break
    else:
      u = input("enter user name : ")
      p = input("enter password : ")
      if u == username and p == password:
        print("welcome",username)
        break      # agar break use nhi krenge to registration and login sucessful hone k baad
      else:             # bhi enter user name and enter pasword show hoga
        print("invalid credentials try again")
        attempt = attempt+1
        
        

### wap to diaplay the sum of the numbers given by user until explicitly say stop
add = 0
while True:
  num = int(input("enter number"))
  add = add+num
  choice = input("would you like to add more numbers\nif yes then press y and if no then press any key")
  if choice == "y":
    continue
  else:
    break
print("sum of numbers is",add)
