basic=float(input("ENETR SALARY"))


if (basic<10000):
    DA= (70*basic)/100
    HRA=(65*basic)/100
elif (basic>10000):
     DA= (75*basic)/100
     HRA=(73*basic)/100
elif (basic>20000):
     DA= (80*basic)/100
     HRA=(76*basic)/100
     
gross_salary=basic+HRA+DA
print(gross_salary)
  
