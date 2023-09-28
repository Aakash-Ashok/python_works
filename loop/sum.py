limit=25
start=1
even_sum=0
odd_sum=0
for i in range(start,limit):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print("even sum =",even_sum)
print("odd sum =",odd_sum)