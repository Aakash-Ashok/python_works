weight=90
height_cm=190
height=height_cm/100
bmi=weight/(height**2)
if(bmi<18.5):
    print("underweight")
elif(18<bmi>24.9):
    print("normal weight")
elif(25<bmi>29.9):
    print("over weight")
elif(bmi<=34.4):
    print("ob levl 1")
elif(bmi<=39.9):
    print("ob levl 2")
else:
    print("ob lvl 3")