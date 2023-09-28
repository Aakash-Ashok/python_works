text="ABBAACD"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)

print(max(wc,key=lambda key:wc.get(key)))
print(min(wc,key=lambda key:wc.get(key)))