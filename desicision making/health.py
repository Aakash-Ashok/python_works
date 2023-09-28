tummy_size=int(input("enter tummy size in cm : "))
buttock_size=int(input("enter buttock size in cm : "))
gen=input("enter your gender M/F : ")
value=tummy_size/buttock_size
print(value)
if (value <= 0.80 and gen == "F") or (value <= 0.95 and gen == "M"):
    print("Health risk is low")
elif(value<=0.85 and gen=="F") or (value<=1.0 and gen=="M"):
    print("health risk is moderate")
elif( value>=0.85 and gen=="F") or (value>=1.0 and gen=="M"):
    print("health risk is high")