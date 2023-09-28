li=[2,3,4,5,6]
sum=8
# # lii=[]
# # for i in li:
# #     for j in li:
# #         if(i!=j and i<j):
# #             cur_sum=i+j
# #             if(cur_sum==sum):
# #                 print(i,j)

low=0
upp=len(li)-1
while(low<upp):
    cur_sum=li[low]+li[upp]
    if cur_sum==sum:
        print("pair : ",li[low],li[upp])
        low+=1
    elif cur_sum<sum:
        low+=1
    elif cur_sum>sum:
        upp-=1

