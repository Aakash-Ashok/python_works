num1=int(input("enter a number"))
num2=int(input("enter a number"))
# li=[]
hcf=1
for i in range(2,num1+1):
    if(num1%i==0 and num2%i==0):
        hcf=i
#         li.append(i)
# print(max(li))
print(hcf,"is hcf")

lcm=(num1*num2)/hcf
print(lcm)