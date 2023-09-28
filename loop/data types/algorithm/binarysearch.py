li=[3,4,5,6,7,8,9,10]

ele=2
flag=0
low=0
up=len(li)-1

while(low<up):
    mid=(low+up)//2
    if ele==li[mid]:
        flag=1
        break
    elif ele>li[mid]:
        low=mid+1
    elif ele<li[mid]:
        up=mid-1
print("found" if flag==1 else "not found")