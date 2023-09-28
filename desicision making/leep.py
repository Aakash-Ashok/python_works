# A year is a leap year if the following conditions are satisfied: 

# The year is multiple of 400.
# The year is multiple of 4 and not multiple of 100.


year=int(input("enter the year"))
if year%4==0 and year%100!=0 or year%400==0:
    print("this year is leap")
else:
    print("not")