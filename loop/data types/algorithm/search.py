li=[1,2,3,4]
ele=2
flag=0
for i in range(0,len(li)-1):
    if li[i]==ele:
        flag=1
        break
if flag==1:
    print("element found")
else:
    print("not found")




