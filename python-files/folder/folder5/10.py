# for i in range(1,10):
#     if i==5:
#         print("hii")
#         break
#     print("hello")


# i=1
# while(i<=10):
#     if i==5:
#         print("hi")
#         break
#     print("hello")
#     i=i+1

# for i in range(1,11):
#   if i==5:
#     continue
#   print(i)

# for i in range(10):
#     print("Hello")
#                                 #4 times hello
#     if i == 6:                  #4 times hi      
#         break                   #

#     elif i == 4:
#         print("Hellozz")
#         i=i+2
#         continue

#     print("hi")

# print("happy",i)

# num = int(input("enter number"))
# l = [1,3,5,7,8,12,24,56,78,89,34,67]
# for i in l:
#     if i==num:
#         break
#     print(i)

# a = [12,23,15,34,45,56,76,60,78,75,89,90,150]
# count=0
# for i in a:
#     print(i)
#     if i%5==0:
#         count=count+1
#     if count==3:
#         break

# for i in "balmeet":
#     print(i)
#     continue
#     print("balmeet")
# print(i)


# for i in "balmeet":
#      break
# print(i)



end = int(input("enter number"))
for i in range(1,end+1):
    if i%5 == 0:
        continue
    print(i)
   
  # WAP to display all the numbers from 1 to number entered by user except those numbers
   #which is divisible by 5 in this range.
   