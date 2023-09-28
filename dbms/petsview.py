from connection import *

class PetsView:

    def connect(self):
        db=connectdb("animal")
        return db



    def get(self,args,*kwargs):
        db=self.connect()
        cursor=db.cursor()
        query="select * from pets"
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    
    def retrive(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"select * from pets where id={id} "
        cursor.execute(query)
        rec=cursor.fetchone()
        return rec
    

    def post(self,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        query="insert into pets (age,gender,breed,location,price) values (%s,%s,%s,%s,%s)"
        data=tuple(v for v in kwargs.values())
        cursor.execute(query,data)
        db.commit()
        return kwargs
    
    def destory(self,id):
        db=self.connect()
        cursor=db.cursor()
        query=f"delete from pets where id={id}"
        cursor.execute(query)
        db.commit()

    def update(self,id,*args,**kwargs):
        db=self.connect()
        cursor=db.cursor()
        age=kwargs.get("age")
        query="update from pets set age={age} where id={id}"

    
pv=PetsView()
# print(pv.get())
# print(pv.retrive(2))
# print(pv.post(age=26,gender="male",breed="breed4",location="kottayam",price="40000"))
print(pv.destory(2))