from connection import *
p="animal"
db=connectdb(p)

cursor=db.cursor()
query="""select * from pets"""
cursor.execute(query)

records=cursor.fetchall()

for rec in records:
    print(rec)



