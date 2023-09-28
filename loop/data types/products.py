mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
        
]

# print(len(mobiles),"mobiles available")

# mobile_names=[mob[1] for mob in mobiles]
# print(mobile_names)

# mobile_names=[ mob[1] for mob in mobiles if mob[3]=="4g"]
# print(mobile_names)

# mobile_names=[mob[1] for mob in mobiles if mob[2]<30000]
# print(mobile_names)

# mobile_names=[mob[1] for mob in mobiles if 30000<mob[2]<50000]
# print(mobile_names)

mobile_names=[mob[1] for mob in mobiles if mob[2]<25000 and mob[3]=="5g"]
print(mobile_names)

