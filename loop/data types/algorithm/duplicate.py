li=[2,3,4,4,5,5,6,7]
i=0
while(i<len(li)-1):
    if li[i]==li[i+1]:
        print(li[i])
        i+=1
    else:
        i+=1

# li=[2,3,4,4,5,5,6,7]
# low=0
# upp=len(li)-1
# while(low<=upp):
#     if li[low]==li[upp]:
#         li.pop(low)

#         upp-=1
#     else:
#         low-=1
# print(li)


