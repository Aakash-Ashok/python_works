class p1:
    def m1(self):
        print("class p1 m1 method")

class p2:
    def m1(self):
        print("class p2 m2 method")


class c1(p2,p1):
    pass

c=c1()
c.m1()