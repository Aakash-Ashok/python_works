li=[1,3,4,6]

for i in range (0,len(li)-1):
    if(li[0]!=1):
        print(1,"is missing")
        break
    else:
        ele1=li[i]
        ele2=li[i+1]
        if ele2-ele1!=1:
            print(ele1+1,"is missing")
            break
            