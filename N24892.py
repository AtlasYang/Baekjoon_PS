#https://www.acmicpc.net/problem/24892
#started on 2022.04.04

from math import *

class Fraction():
    def __init__(self, p, q):
        self.num = p
        self.den = q
        self.update()
        
    def update(self):
        t = gcd(self.num, self.den)
        if t == 1:
            return
        else:
            self.num = int(self.num / t)
            self.den = int(self.den / t)
            return
    
    def __add__(self, obj):
        x = self.num * obj.den + self.den * obj.num
        y = self.den * obj.den
        return Fraction(x, y)
    
    def __sub__(self, obj):
        obj.num *= (-1)
        return self.__add__(obj)
    
    def __mul__(self, obj):
        x = self.num * obj.num
        y = self.den * obj.den
        return Fraction(x, y)


def Area(n, a, b):
    c = b - a
    temp = Fraction(0, 1)
    for i in range(1, n):
        x = Fraction(i * c, n)
        y = Fraction((i + 1) * c, n)
        temp += x * y * (y - x)
    max_area = temp * Fraction(1, 2)
    return max_area.num, max_area.den
