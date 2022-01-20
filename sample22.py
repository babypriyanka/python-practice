# WAP to check a perfect number or not
n=int(input("Enter Number: "))
x=0
for i in range(1,n):
    if n%i==0:
        x=x+i
if x==n:
    print("it is a perfect number")
else:
    print("It is not a perfect number")
        
    
    
