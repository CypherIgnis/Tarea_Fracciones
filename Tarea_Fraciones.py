# Tarea_Fracciones
import math
class Fraction():
    #atributos#
    numerator=0
    denominator=1
    #fin seccion atributos#

    def __init__(self,numerator,denominator):
        print("Comenzando programa")
        self.numerator=numerator
        self.denominator=denominator

    def printt(self):
        print(self.numerator,"/",self.denominator)

    
    def mcm (self,x,y):
        z= max(x,y)

        while True:
            if (z % x == 0) and (z % y == 0):
                return z
            
            z+=1  

    def plus(self,a,b):
        numerator = float(self.numerator)+float(a.numerator)+float(b.numerator)
        denominator = float(self.mcm)
        p=Fraction(numerator,denominator)
        p.printt()

    def minus(self,a,b):
        numerator = float(self.numerator)-float(a.numerator)-float(b.numerator)
        denominator = float(self.mcm)
        m=Fraction(numerator,denominator)
        m.printt()

    def multiplication(self,a1,b1,a2,b2):
        numerator = float(self.numerator)*float(a1.numerator)*float(b1.numerator)
        denominator = float(self.numerator)*float(a2.denominator)*float(b2.denominator)
        x=Fraction(numerator,denominator)
        x.printt()


    def division(self,a1,b1,a2,b2):
        numerator = float(self.numerator)*float(a1.numerator)*float(b2.denominator)
        denominator = float(self.numerator)*float(a2.numerator)*float(b1.denominator)
        d=Fraction(numerator,denominator)
        d.printt()


o=Fraction(3,4)
print(o.numerator)
print(o.denominator)
a=Fraction(float(input("ingrese la fraccion a1=")),float(input("ingrese la fraccion a2=")))
b=Fraction(float(input("ingrese la fraccion b1=")),float(input("ingrese la fraccion b2=")))
print(a.mcm(a.denominator,b.denominator)) 
a.printt()
b.printt()
p=a.plus(a.numerator,b.numerator)
print(p)
m=b.minus(a.numerator,b.numerator)
print(m)
x=a.multiplication(a.numerator,b.numerator,a.denominator,b.denominator)
print(x)
d=b.division(a.numerator,b.denominator,b.numerator,a.denominator)
print(d)

