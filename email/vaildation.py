from re import fullmatch
f=open("C:/Users/akash/Desktop/pys/email/data.txt")
vaild_mail=set()
rule="[a-zA-Z0-9][a-zA-Z0-9#$]*[@]gmail[.]com"
for id in f:
    id=id.rstrip("\n")
    matcher=fullmatch(rule,id)
    if matcher!=None:
        vaild_mail.add(id)
print(vaild_mail)
    