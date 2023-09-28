from connection import *
p="animal"
db=connectdb(p)
cursor=db.cursor()
query="""select * from pets where id=2"""
cursor.execute(query)
rec=cursor.fetchone()
print(rec)