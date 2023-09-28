f1=open("C:/Users/akash/Desktop/pys/attendence/data.txt","r")
f2=open("C:/Users/akash/Desktop/pys/attendence/present.txt","r")
student=set()
present=set()

for line in f1:
    student.add(line.rstrip("\n"))
print(student)

for linee in f2:
    present.add(linee.rstrip("\n"))
print(present)

abs=student-present
print(abs)