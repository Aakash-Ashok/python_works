class Mobile(object):
    name:str
    price:int
    display:str


    def __init__(self,**kwargs) -> None:
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")


    def __str__(self):
        return self.name

    @property 
    def get_dis_price(self):
        return self.price-1


obj=Mobile(name="oneplus",price=30000,display="amoled")
print(obj)

print(obj.get_dis_price)