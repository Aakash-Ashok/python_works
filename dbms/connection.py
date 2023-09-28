from mysql.connector import *

def connectdb(p):
    db=connect(
        host="localhost",
        user="root",
        password="",
        database=p
        )
    return db
