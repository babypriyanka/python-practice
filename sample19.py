#  WAP to accept start and stop values and print the values between them
# eg:10 to 20
# or 20 to 10 (2 if condition needed)

n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))

if(n1>n2):
    for i in range(n2,n1,-1):
       print(i)
if(n1<n2):
    for i in range(n1,n2):
        print(i)