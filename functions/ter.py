# num1=12
# # print("odd" if num1%2!=0 else "even")
# num2=1
# print(num1 if num1>num2 else num2)/

def max_three(n1,n2,n3):
    return n1 if (n1>n2) and (n1>n3) else n2 if n2>n3 else n3

print(max_three(10,20,30))