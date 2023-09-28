li=[8,14,15,20,21]
lii=[9,10,20,21,22]

p1=0
p2=0

while(p1<len(li) and p2<len(lii)):
    if(li[p1]==lii[p2]):
        print(li[p1])
        p1+=1
    elif (li[p1]<lii[p2]):
        p1+=1
    elif (li[p1]>lii[p2]):
        p2+=1