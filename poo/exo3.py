from math import sqrt, pow

class Point:
    def __init__(self, absc:float, ordered:float):
        self.__absc = absc
        self.__ordered = ordered

    @property
    def get_absc(self):
        return self.__absc

    
    @set_absc.setter
    def set_absc(self, absc):
        self.__absc = absc

    @property
    def get_ordered(self):
        return self.__ordered

    @set_ordered.setter
    def set_ordered(self, ordered):
        self.__ordered = ordered

    def __str__(self):
        return f'({self.__absc}, {self.__ordered})'

    def calucler(self, p:Point) -> float:
        """Calculates distance between two points"""
        return sqrt(
            pow(self.__absc - p.__absc, 2) + pow(self.__ordered - p.__ordered, 2)
            )

    def calculer_milieu(self, p:Point) -> Point:
        """Calculates two points segment's middle"""
        p = Point(absc=(self.__absc + p.__absc)/2, ordered=(self.__ordered + p.__ordered)/2)
        return p


class TroisPoint:
    def __init__(self, p1:Point, p2:Point, p3:Point):
        