class parent:
    def vehicles(self):
        self.context=["passionpro","swift"]
        return self.context
    

class child(parent):
    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("hunter")
        return self.context

    
c=child()
print(c.vehicles())