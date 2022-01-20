# WAP to check a given number is prime number are not.
n=int(input("Enter Number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count<=2:
    print("its a prime number")
else:
    print("NOT prime number")