from json import load
with open ("C:/Users/akash/Desktop/pys/JSONPROGRAM/data.json","r") as f:
    data=load(f)

# print(data)


names=[u.get("name") for u in data]
print(names)

maxx=max(data,key=lambda g:g.get("total"))
print(maxx)


print(len(data))