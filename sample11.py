amount=int(input("WITHDRAW AMOUNT"))
if amount>=500:
    a=amount//500
    amount=amount-(500*a)
    print("500 rupee Notes",a)
if amount>=200:
    b=amount//200
    amount=amount-(200*b)
    print("200 rupee Notes",b)
if amount>=100:
    c=amount//100
    print("100 rupee Notes",c)