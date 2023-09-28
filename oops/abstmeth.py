from abc import ABC,abstractmethod

class ide(ABC):
    @abstractmethod
    def debug(self):
        pass

class pycharm (ide):
    def debug(self):
        print("pycharm debug method")

class eclipse (ide):
    def debug(self):
        print("eclipse debug method")





class shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class rectange(shape):
    def draw(self):
        print(" draw rectangle")

class triangle(shape):
    def draw(self):
        print(" draw triangle")

ob=rectange()
ob.draw()