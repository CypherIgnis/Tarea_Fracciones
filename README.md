# Tarea_Fracciones
class Fraction:
#atributos#
    numerator=0
    denominator=1
#fin seccion atributos#

def __init__(self,numerator,denominator):
    self.numerator=numerator
    self.denominator=denominator

def print(self):
    print(self.numerator,"/",self.denominator)

def plus(self,b):
    numerator = self.numerator+b.numerator
    denominator = self.denominator+b.denominator
    p=Fraction(numerator,denominator)
    p.print()
    
def minus(self,b):
    numerator = self.numerator-b.numerator
    denominator = self.denominator-b.denominator
    m=Fraction(numerator,denominator)
    m.print()
    
def multiplication(self,b):
    numerator = self.numerator*b.numerator
    denominator = self.denominator*b.denominator
    x=Fraction(numerator,denominator)
    x.print()
    
    
def division(self,b):
    numerator = self.numerator*b.denominator
    denominator = self.denominator*b.numerator
    d=Fraction(numerator,denominator)
    d.print()

print(o.numerator)
print(o.denominator)
a=Fraction(3,2)
b=Fraction(6,5)
a.print()
b.print()
p=a.multiplication(b)
p.print()
m=a.multiplication(b)
m.print()
x=a.multiplication(b)
x.print()
d=a.multiplication(b)
d.print()
