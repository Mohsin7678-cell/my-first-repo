# ## wap to sum of all numbers from 1 to given number
# num = int(input("enter num"))
# add = 0
# for i in range(1,num+1):
#     add=add+i
# print("sum of all is",add)


# for i in range(1,11):
#     # a = i*i
#     print(i,"square",i*i )
#     # print(i*i)


# i=105
# while(i>=7):
#     print(i)
#     i=i-7



# for i in range (105,5,-7):
#     print(i ,end=" ")


# ## 1,4,9,16,25,....

# i=0

# # for i in range(1,100,)
# while(i<=0):
#     print(i)
#     i=i
#     i<=0

# for i in range(2000,3201,):
#     if i%7==0:
#         if i%5!=0:
#           print(i,end=",") 

# num = int(input("enter number"))
# for i in num:
#     if i in ["2","3","4","5","6","7","8","9"]:
#         print("entered number is not binary")
#         break
#     else:
#         if num%5==0:
#             print(num,"is divisible by 5")                   


for num in range(1000,3001):
    count=0
    num=str(num)
    for i in num:
        if i%2==0:
            count = count +1
    if count == 4:
      print(num)                                                          
        
          
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


    