class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = Fraction.reduction(numerator,denominator)

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a,b = b, a%b
        return a

    @classmethod
    def reduction(cls, newnumerator, newdenominator):
        common = cls.gcd(newnumerator,newdenominator)
        return (newnumerator//common,newdenominator//common)

    def __repr__(self):
        return "{!r} / {!r}".format(self.numerator,self.denominator)

    def __add__(self, other):
        newnumerator = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        newdenominator = self.denominator * other.denominator
        return Fraction(newnumerator,newdenominator)

    def __eq__(self, other):
        firstnumerator = self.numerator * other.denominator
        secondnumerator = self.denominator * other.numerator
        return firstnumerator == secondnumerator
        


    
f1 = Fraction(1,2)
f2 = Fraction(1,4)
print(f1 + f2)
if f1 == f2:
    print('Equal')
else:
    print('Not Equal')

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x,y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    
p1 = Polynomial(1,2,3)
p2 = Polynomial(3,4,5)

print(p1 + p2)


class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)