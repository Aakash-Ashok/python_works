# num=input("enter a number : ")
# print(num)
# print(type(num))




# def add(num1,num2):
#     sum=num1+num2
#     return sum
# num1=int(input("number"))
# num2=int(input("number"))
# print(add(num1,num2))



# def multiplication(num1,num2,num3):
#     result=num1*num2*num3
#     return result

# print(multiplication(2,3,4))

def minn(num1,num2):
    # if(num1>num2):
    #     return num1
    # else:
    #     return num2
    return num2 if num1>num2 else num1
a=int(input("number"))
b=int(input("number"))
print(minn(a,b))