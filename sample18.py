#number of factors of a given number

n=int(input("Find Number of factors for: "))
count=0
for i in range(1,n+1):
    if(n%i==0):
       print(i)
       count+=1
print("number of factors are: ",count)       
        