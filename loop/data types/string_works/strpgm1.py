# text="one 100 and fifty 5"
# a=text.split()

# for ch in a:
#         if ch.isdigit():
#                 print(ch)

# num=[ ch for ch in text.split() if ch.isdigit()]
# print(num)


##########################################################################2nd programe#############################################################################

# text="England promised to continue its agressive approch to Test cricket"
# a=text.casefold()
# b=a.split(" ")
# for ch in b:
#     if ch[0] in ["a","e","i","o","u"]:
#         print(ch)


# str=[ch for ch in text.split() if ch[0].casefold() in ["a","e","i","o","u"]]
# print(str)


##############################################################################3rd programe############################################################################
text="hello i am here in kakkanad"
a=text.split(" ")
print(max(a,key=lambda w:len(w)))