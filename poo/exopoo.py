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

        return AB == AC + BC or AC == AB + BC or BC == AC + AB


    def est_isocele(self) -> bool:
        AB = self.premier.calculerdistance(self.deuxieme)
        AC = self.premier.calculerdistance(self.troisieme)
        BC = self.deuxieme.calculerdistance(self.troisieme)

        return AB == AC  or AB == BC or BC == AC

    @staticmethod
    def calculermilieu(p:Point, p1:Point) -> float:
        p = Point((p.absc + p1.absc)/2, (p.order + p1.order)/2)
        return p

    @staticmethod
    def calculerdistance(p:Point, p1:Point) -> float:
        return sqrt(pow(p.absc - p1.absc, 2) + pow(p.order - p1.order,2))


tp = TroisPoint(Point(8, 2), Point(5, 4), Point(2,2))

print(TroisPoint.calculerdistance(tp.premier, tp.deuxieme))