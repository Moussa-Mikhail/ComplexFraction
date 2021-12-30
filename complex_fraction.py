from __future__ import annotations

from fractions import Fraction
from numbers import Complex, Number, Real


class ComplexFraction(Number):

    def __init__(self, *args):
        
        if (len(args) == 1):

            z: Complex = args[0]

            self.real: Fraction = Fraction(z.real)

            self.imag: Fraction = Fraction(z.imag)
        
        elif (len(args) == 2):

            real: Real = args[0]

            imag: Real = args[1]

            self.real: Fraction = Fraction(real)

            self.imag: Fraction = Fraction(imag)

    def __repr__(self) -> str:

            return f"ComplexFraction('{self.real}', '{self.imag}')"
    
    def __str__(self) -> str:

        printable_num = self.limit_denominator()

        if (printable_num == 0):

            return '0'
        
        elif (printable_num.real == 0):

            return f"{printable_num.imag}*1j"
        
        elif (printable_num.imag == 0):

            return f"{printable_num.real}"
        
        else:

            if (printable_num.imag > 0):

                return f"{printable_num.real}+{printable_num.imag}*1j"
            
            else:

                return f"{printable_num.real}-{-printable_num.imag}*1j"
            
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

        res_imag = self.real*rhs.imag + self.imag*rhs.real

        return ComplexFraction(res_real, res_imag)
    
    def __rmul__(self, lhs: Number) -> ComplexFraction:

        if not isinstance(lhs, ComplexFraction):

            lhs = ComplexFraction(lhs)

        res_real = self.real*lhs.real - self.imag*lhs.imag

        res_imag = self.real*lhs.imag + self.imag*lhs.real

        return ComplexFraction(res_real, res_imag)

    def conjugate(self: ComplexFraction) -> ComplexFraction:

        res_real = self.real

        res_imag = -self.imag

        return ComplexFraction(res_real, res_imag)
    
    def magnitude_squared(self: ComplexFraction) -> Fraction:

        return self.real**2 + self.imag**2
    
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