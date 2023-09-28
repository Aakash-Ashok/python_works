lst1=[10,11,13,15]
lst2=[9,8,11,13,14]
l1=0
l2=0
while(l1<len(lst1)and l2<len(lst2)):
    if(lst1[l1]==lst2[l2]):
        print(lst1[l1])
        l2+=1
    elif(lst1[l1]>lst2[l2]):
        l2+=1
    elif(lst1[l1]<lst2[l2]):
        l1+=1

