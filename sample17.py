#Factors of agiven number:
    
n=int(input("Find Factors for: "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        
        