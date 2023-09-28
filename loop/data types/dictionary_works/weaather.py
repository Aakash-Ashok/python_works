weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},
]

temp={}
for t in weather:
    for k,v in t.items():
        district_name=k
        current_weather=v
        if district_name in temp :
            old_temp=temp[district_name]
            if current_weather>old_temp:
                temp[district_name]=current_weather
        else:
            temp[district_name]=current_weather
print(temp)