s1=int(input("Enter Project Marks: "))
s2=int(input("Enter Internal Marks: "))
s3=int(input("Enter External Marks: "))
total_score=0
if(s3<50):
     e=50-s3
     print("failed in External by the shortage of: ",e,"Marks")
if(s2<50):
     i=50-s2
     print("failed in internal by the shortage of: ",i ,"Marks")
if(s1<50):
     p=50-s1
     print("failed in Project by: ",p ,"Marks")
if(s1>=50 and s2>=50 and s3>=50):
    total_score=(70/100)*s1+(10/100)*s2+(20/100)*s3
    print("Total Score:",total_score)

if(total_score>=90):
     print("A Grade")
elif(total_score>75):
     print("B Grade")
else:
     print("C Grade")   