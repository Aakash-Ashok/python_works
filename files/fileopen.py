f=open("C:/Users/akash\Desktop\pys/files/data.txt","r")
words=[]
for line in f:
    line=line.rstrip("\n")
    text=line.split(" ")
    for w in text:
        words.append(w)
print(set(words))