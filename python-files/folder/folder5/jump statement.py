# for i in range(1,5):
#     print(i)
#     if i==3:
#         print("hi")
#         break
#     print("hlo")
# print("hello")


for i in range (1,5):
    print("hlo")
    if i==4:
        #print(i)
        continue
        print("hi")
    print("helozz")
        
#! wap to dispplay all numbers in the list unitl u get the third number which is divisible by 5
a = [12,23,15,34,45,56,76,60,78,75,89,90,150]
count=0
for i in a:
    print(i)
    if i%5==0:
        count=count+1
    if count==3:
        break