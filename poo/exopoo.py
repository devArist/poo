from math import sqrt

class Point:
    def __init__(self,absc,order):
        self.__absc = absc
        self.__order = order

    @property
    def absc(self):
        return self.__absc 

    @absc.setter
    def absc(self,X):
        self.__absc = X

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self,Y):
        self.__order = Y


    def __str__(self):
        return f"({self.__absc},{self.__order})"

    def calculerdistance(self, p):
        return sqrt(pow(self.__absc - p.__absc, 2) + pow(self.__order - p.__order,2))


    def calculermilieu(self,p):
        p = Point((self.__absc + p.__absc)/2, (self.__order + p.__order)/2)
        return p


p =Point(5,9)
p1 =Point(3,7)
print(p.calculermilieu(p1))




class TroisPoint:
    def __init__(self,premier:Point, deuxieme:Point, troisieme:Point) -> bool:
        self.__premier = premier
        self.__deuxieme = deuxieme
        self.__troisieme = troisieme

    @property
    def premier(self):
        return self.__premier

    @premier.setter
    def premier(self,X):
        self.__premier = X 
    
    @property
    def deuxieme(self):
        return self.__deuxieme

    @deuxieme.setter
    def deuxieme(self,Y):
        self.__deuxieme = Y
    @property
    def troisieme(self):
        return self.__troisieme

    @deuxieme.setter
    def deuxieme(self,Z):
        self.__troisieme = Z

    def sont_alignes(self):
        AB = self.premier.calculerdistance(self.deuxieme)
        AC = self.premier.calculerdistance(self.troisieme)
        BC = self.deuxieme.calculerdistance(self.troisieme)

        if AB == AC + BC:
            return True
        else:
            return False



t = TroisPoint(Point(4, 5), Point(3, 4), Point(6, 3))

print(t.sont_alignes())