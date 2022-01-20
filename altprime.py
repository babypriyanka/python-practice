# WAP to print alternate prime numbers
n=int(input("Enter number: "))
list=[]
for n in range(1,n+1):
    if n>1:
        for i in range(2,n): 
            if n%i==0:
                break
        else:
            print(n,end=" ") 
            n.append(list)
            for x in range(0,list):
                if x%2 !=0:
                    print(x)
