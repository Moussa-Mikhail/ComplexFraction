from __future__ import annotations

from fractions import Fraction
from numbers import Complex, Number, Real


class ComplexFraction(Number):

    def __init__(self, *args):

        if (len(args) == 0):

            self.real: Fraction = Fraction(0)
            
            self.imag: Fraction = Fraction(0)
        
        elif (len(args) == 1):

            z: Complex = args[0]

            self.real: Fraction = Fraction(z.real)

            self.imag: Fraction = Fraction(z.imag)
        
        elif (len(args) == 2):

            real: Real = args[0]

            imag: Real = args[1]

            self.real: Fraction = Fraction(real)

            self.imag: Fraction = Fraction(imag)

    def __repr__(self) -> str:

        if (self.imag != 0):

            return f"ComplexFraction({self.real}, {self.imag})"

        else:
            
            return f"ComplexFraction({self.real})"
    
    def __str__(self) -> str:

        if (self == 0):

            return '0'
        
        elif (self.real == 0):

            return f"{self.imag}j"
        
        elif (self.imag == 0):

            return f"{self.real}"
        
        else:

            if (self.imag > 0):

                return f"{self.real}+{self.imag}j"
            
            else:

                return f"{self.real}-{-self.imag}j"
            
    def __eq__(self, rhs: Number) -> bool:

        return self.real == rhs.real and self.imag == rhs.imag    

    def __neg__(self) -> ComplexFraction:

        res_real = -self.real

        res_imag = -self.imag

        return ComplexFraction(res_real, res_imag)
    
    def __add__(self, rhs: Number) -> ComplexFraction:

        if not isinstance(rhs, ComplexFraction):

            rhs = ComplexFraction(rhs)

        res_real = self.real + rhs.real

        res_imag = self.imag + rhs.imag

        return ComplexFraction(res_real, res_imag)
    
    def __radd__(self, lhs: Number) -> ComplexFraction:

        if not isinstance(lhs, ComplexFraction):

            lhs = ComplexFraction(lhs)

        res_real = self.real + lhs.real

        res_imag = self.imag + lhs.imag

        return ComplexFraction(res_real, res_imag)
    
    def __sub__(self, rhs: Number) -> ComplexFraction:

        if not isinstance(rhs, ComplexFraction):

            rhs = ComplexFraction(rhs)
        
        rhs = -rhs

        res_real = self.real - rhs.real

        res_imag = self.imag - rhs.imag

        return ComplexFraction(res_real, res_imag)
    
    def __rsub__(self, lhs: Number) -> ComplexFraction:

        if not isinstance(lhs, ComplexFraction):

            lhs = ComplexFraction(lhs)

        res_real = -self.real + lhs.real

        res_imag = -self.imag + lhs.imag

        return ComplexFraction(res_real, res_imag)
    
    def __mul__(self, rhs: Number) -> ComplexFraction:

        if not isinstance(rhs, ComplexFraction):

            rhs = ComplexFraction(rhs)

        res_real = self.real*rhs.real - self.imag*rhs.imag

        res_imag = self.real*rhs.imag + self.imag*rhs.imag

        return ComplexFraction(res_real, res_imag)
    
    def __rmul__(self, lhs: Number) -> ComplexFraction:

        if not isinstance(lhs, ComplexFraction):

            lhs = ComplexFraction(lhs)

        res_real = self.real*lhs.real - self.imag*lhs.imag

        res_imag = self.real*lhs.imag + self.imag*lhs.imag

        return ComplexFraction(res_real, res_imag)

    def conjugate(self: ComplexFraction) -> ComplexFraction:

        res_real = self.real

        res_imag = -self.imag

        return ComplexFraction(res_real, res_imag)
    
    def magnitude_squared(self: ComplexFraction) -> Fraction:

        return (self*self.conjugate()).real
    
    def recip(self: ComplexFraction) -> ComplexFraction:

        return self.conjugate()/self.magnitude_squared()
    
    def __truediv__(self, rhs: Number) -> ComplexFraction:

        return self*(1/rhs)
    
    def __rtruediv__(self, lhs: Number) -> ComplexFraction:

        return lhs*self.recip()
    
    def limit_denominator(self, max_denominator=1000000) -> ComplexFraction:

        new_real: Fraction = self.real.limit_denominator(max_denominator)

        new_imag: Fraction = self.imag.limit_denominator(max_denominator)

        return ComplexFraction(new_real, new_imag)