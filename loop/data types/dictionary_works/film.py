movies={"2018":5,"keralastory":3,"neymer":4,"kgf":5,"arm":4}

"""
all movie name
print top rated movie
sort movies in desc
"""
print(movies.keys())
print(max(movies,key=lambda value:movies.get(value)))
print(sorted(movies,key=lambda i:movies.get(i),reverse=True))