# WAP to print list of Prime numbers between 1 to n
num=int(input("Enter Number: "))
for num in range(1,num+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
    