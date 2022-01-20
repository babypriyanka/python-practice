units = float(input("Enter UNITS"))
if(units<50):
    charges=0.75*units
elif(units<=150):
    charges=(50*0.75)+(units-50)*2.10
elif(units<=250):
    charges=(50*0.75)+(100*2.10)+(units-150)*2.50
else:
    charges=(50*0.75)+(100*2.10)+(100*2.50)+(units-250)*2.80
print("Bill",charges)

gst = (charges*10)/100
bill = charges+gst
print("GST", gst)
print("Final Bill",bill)