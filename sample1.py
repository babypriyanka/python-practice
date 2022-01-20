list=[5,6,4,8,9,7,4,5,6,7]
count =0
n=int(input("Enter Number: "))
for i in list:
    if i==n:
        count=count+1
if count!=0:
    print("the number occurs in: ",+ count)
else:
    print("No")