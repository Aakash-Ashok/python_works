num1=1
num2=20
num3=40

largest=0
sec_largest=0
third_largest=0
if num1 > num2 and num1 > num3:
    largest=num1
    if num2 > num3:
        sec_largest=num2
        third_largest=num3
    else:
        sec_largest=num3
        third_largest=num2
elif num2 > num1 and num2 > num3:
    largest=num2
    if num1 > num3:
        sec_largest=num1
        third_largest=num3
    else:
        sec_largest=num3
        third_largest=num1
else:
    largest=num3
    if num1 > num2:
        sec_largest=num1
        third_largest=num2
    else:
        sec_largest=num2
        third_largest=num1
print(f"largest={largest}")
print(f"second largest={sec_largest}")
print(f"third largest={third_largest}")






num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}")
