# li=[]
# arr=[2,3,4]
# total=sum(arr)
# for i in range(0,len(arr)):
#     a=total-arr[i]
#     li.append(a)
# print(li)     


# numbers=[2,7,8,9,12,13]
# even=[]
# odd=[]
# for num in numbers:
#     even.append(num) if num%2==0 else odd.append(num)
# print(even)
# print(odd)

# num=[2,4,7,8]

# # print(numbers-num)

# num.insert(0,1)
# print(num)


# li=[]
# limit=int(input("enter a number of elements : "))
# for i in range(0,limit):
#     a=int(input(f"enter elemts in {i} : "))
#     li.append(a)
#     big=li[0]
#     if (li[0]<li[i]):
#         big=li[i]
#     else:
#         big=li[0]
# print(big)
# li.insert(2,big+10)
# print(li)



name=["Akash","Jishnu","Arya","Snehith","Akash"]
search=input("enter name to be searched : ")
flag=0
for i in range(0,len(name)):
    if(search==name[i]):
        name[i]="Anamika"
        flag=1
if(flag==0):
    name.insert(1,"Amal")
    print(name)
else:
    print(name)



