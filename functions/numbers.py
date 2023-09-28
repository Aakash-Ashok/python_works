def maxx(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        largest=num1
        if num2 > num3:
            sec_largest=num2
        else:
            sec_largest=num3
    elif num2 > num1 and num2 > num3:
        largest=num2
        if num1 > num3:
            sec_largest=num1
        else:
            sec_largest=num3
    else:
        largest=num3
    if num1 > num2:
        sec_largest=num1
    else:
        sec_largest=num2
    print(largest)

print(maxx(10,20,30))