import re 
mail=input("enter the email : ")
y=re.search("@gmail.com$",mail)
if y:
    print("vaild")
else:
    print("not vaild")