num=int(input("number"))
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
if is_prime==True:
    print(num,"is prime")
else:
    print(num,"is not prime")



for i in range(2,num):
    if num%i==0:
        print(num,"is not prime")
        break
else:
    print(num,"is  prime")