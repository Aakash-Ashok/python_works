from connection import *
class mobileview:
    def connect(self):
        db=connectdb("mobiledb")
        return db
    def get(self):
        db=self.connect()
        cursor=db.cursor()
        query="select * from mobile"
        cursor.execute(query)
        q=cursor.fetchall()
        for i in q:
            print(i)
mb=mobileview()
print(mb.get())