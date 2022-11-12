# Tarea_Fracciones
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

    def plus(self,b):
        numerator = self.numerator+b.numerator
        denominator = self.denominator+b.denominator
        p=Fraction(numerator,denominator)
        p.printt()

    def minus(self,b):
        numerator = self.numerator-b.numerator
        denominator = self.denominator-b.denominator
        m=Fraction(numerator,denominator)
        m.printt()

    def multiplication(self,b):
        numerator = self.numerator*b.numerator
        denominator = self.denominator*b.denominator
        x=Fraction(numerator,denominator)
        x.printt()


    def division(self,b):
        numerator = self.numerator*b.denominator
        denominator = self.denominator*b.numerator
        d=Fraction(numerator,denominator)
        d.printt()


o=Fraction(3,4)
print(o.numerator)
print(o.denominator)
a=Fraction(3,2)
b=Fraction(6,5)
a.printt()
b.printt()
p=b.plus(2)
print(p)
m=a.minus(2)
print(m)
x=b.multiplication(4)
print(x)
d=a.division(3)
print(d)
