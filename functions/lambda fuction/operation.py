# add=lambda n1,n2:n1+n2
# sub=lambda n1,n2:n1-n2
# multiplication=lambda n1,n2:n1*n2
# div=lambda n1,n2:n1/n2

# print(add(10,20))
# print(sub(20,10))
# print(multiplication(10,20))
# print(div(20,10))



# smartsub=lambda n1,n2: n1-n2 if n1>n2 else n2-n1
# print(smartsub(10,20))

# emp={"id":100,"name":"vijay","department":"hr","salary":250000}

# getname=lambda emp : emp.get("name")
# print(getname(emp))

# getsalary=lambda emp:emp.get("salary")
# print(getsalary(emp))



words=["hello","good","aabbcccdef","morning"]
out=sorted(words,reverse=True,key=lambda w:len(w))
print(out)