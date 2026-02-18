# for i in range(1,40):
#     if i%2 == 0:
#         print(i,end=",")

# start = int(input("enter start : "))
# end = int(input("enter end : "))
# count = 0
# for i in range(start,end+1):
#     if i%2 == 0:
#         count = count+1
# print("total even number is",count)



# start = int(input("enter start : "))
# end = int(input("enter end : "))
# count_e= 0
# count_o= 0
# for i in range(start,end+1):
#     if i%2 == 0:
#         count_e= count_e+1
#         count_o= count_o+1
# print("total even number is",count_e)
         
# print("total even number is",count_o)


# for i in range(1,11):
#     if i%2 == 0:
#         print(i,"is even")
#     elif i%2!=0:
#         print(i,"is odd")

 
# num = int(input("enter num that you want its factors :: "))
# count = 0
# for i in range(1,num+1):                      
#     if num%i == 0:
#         count = count+1
#         print("factors of this num is",i)
# print("total factors is",count)
# if count == 2:
#     print("number is prime")
# else:
#     print("number is composite")
      

# a = "mohsin"
# for ch in a:
#     print(ch,end="_")



# print(12,13,"hello hii")
# for i in "24":
#     print(i)
      
      
 #! wap to take ur name from the user and display the vowel in it and also display the count as well     
# name = (input("enter your name : "))
# count_v= 0
# count_c=0
# for ch in name:
#     if ch in("AEIOUaeiou"):                                         #("A","E","I","O","U","a","e","i","o","u"):
#         print(ch,"is a vowel")
#         count_v=count_v+1
#         count_c=count_c+1
#     else:
#         print(ch,"is a consonant")
# print("total count_v is",count_v)
# print("total count_c is",count_c)




# l =[1,3,5,6,7,8]
# add = 0
# for num in l:
#     add = add+num
# print("addition is",add)


# l = [1,2,3,4,5,6,7,8,9,]
# add = 0
# for num in l:
#   if num%2 == 0:
#     add = add+num
#     print("addition of even num is",add)
    
    
# l = [1,2,3,4,5,6,7,8,9,]  
# add_e= 0
# add_o=0
# count_e = 0
# count_o = 0
# for num in l:
#     if num%2 == 0:
#         add_e= add_e+num
#         count_e=count_e+1                    
#     else:
#         add_o = add_o+num
#         count_o=count_o+1
# print("sum of even num is",add_e)
# print("sum of odd num is",add_o)
# average=add_o/count_o
# print(average)
# print("total even is",count_e)
# print("total odd is",count_o) 


# start = int(input("enter start : "))
# end = int(input("enter end : "))
# for num in range(start,end+1):
#     cube = num**3
# print("cube of this num is",cube) 



# start = int(input("enter start : "))
# end = int(input("enter end : "))
# mul = 1
# for i in range(start,end+1):
#     mul = mul*i
#     print("multiple at each step is",mul)
# print("multiple of total is",mul)



         

num = int(input("enter number"))
rev = 0
while(num>0):
    d=num%10
    num=num//10
    rev=rev*10+d
#print("reverse of number is",rev)
if num == rev:
  print("number is pallindrome")
else:
    print("number is not pallindrome")