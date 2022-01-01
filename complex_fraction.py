from __future__ import annotations

from fractions import Fraction
from numbers import Complex, Number, Real
from typing import Tuple, Union


class ComplexFraction(Number):
    """This class implements complex numbers with components being Fractions. 

    In the 1 argument constructor a complex number or a string of a complex number is acceptable.\n

    The 2 argument constructor accepts 2 real numbers, 2 strings, or a combination.\n

    Note that 1/3j is interpreted by python as 1/(3j) == -0.333...j\n
    but for the purposes of this class "1/3j" is equivalent to "(1/3)j."


    """

    __slots__ = ('_real', '_imag')

    def __new__(cls, *args) -> ComplexFraction:

        self = super(ComplexFraction, cls).__new__(cls)

        if (len(args) == 1):

            z = args[0]
            
            if (isinstance(z, Complex)):

                self.from_complex(z)

                return self
            
            elif (isinstance(z, str)):

                self.from_complex_str(z)

                return self
        
        elif (len(args) == 2):

            real: Union[str, Real] = args[0]

            imag: Union[str, Real] = args[1]

            self.from_components(real, imag)     

            return self   
        				

    def from_complex(self, z: Complex):

        self._real: Fraction = Fraction(z.real)

        self._imag: Fraction = Fraction(z.imag)
    
    @staticmethod
    def split_complex_str(z_str: str) -> Tuple[str, str]:

        """Takes a string representing a complex number \n
        and returns a tuple of strings which are \n
        representations of the real and imaginary parts.

        Examples
        --------

        split_complex_str("1.1") = ("1.1", "0")

        split_complex_str("1.1j") = ("0", "1.1")

        split_complex_str("1/3*1j") = ("0", "1/3")

        split_complex_str("1+1j") = ("1", "1")

        split_complex_str("1/3+1.2j") = ("1/3", "1.2")

        split_complex_str("1.2j+1/3") = ("1/3", "1.2")

        split_complex_str("1.2-1/3*1j") = ("1.2", "-1/3")

        split_complex_str("-1/3*1j+1.2") = ("1.2", "-1/3")

        """

        real_str: str = ''

        imag_str: str = ''

        if 'j' in z_str:

            curr_pos: int = z_str.find('j') 

            curr_char: str = z_str[curr_pos]

            imag_str = 'j'

            while (curr_pos > 0 and curr_char not in {'+', '-'}):

                curr_pos -= 1

                curr_char = z_str[curr_pos]

                imag_str = curr_char + imag_str
        
            real_str = z_str.replace(imag_str, '')

            real_str = real_str.replace('+', '')

            imag_str = imag_str.replace("*1j", '')

            imag_str = imag_str.replace('j', '')

            imag_str = imag_str.replace('+', '')

            if real_str == '':

                real_str = '0'
        
        else: 

            real_str = z_str

            real_str = real_str.replace('+', '')

            imag_str = '0'

        return real_str, imag_str
    
    def from_complex_str(self, z_str: str):

        real: str

        imag: str

        real, imag = ComplexFraction.split_complex_str(z_str)

        self.from_components(real, imag)
    
    def from_components(self, real: Union[str, Real], imag: Union[str, Real]):
        
        self._real: Fraction = Fraction(real)

        self._imag: Fraction = Fraction(imag)
    
    @property
    def real(z: ComplexFraction) -> Fraction:

        return z._real
    
    @property
    def imag(z: ComplexFraction) -> Fraction:

        return z._imag

    def __repr__(self) -> str:

            return f"ComplexFraction('{self.real}', '{self.imag}')"
    
    def __str__(self) -> str:

        printable_num: ComplexFraction = self.limit_denominator()

        if (printable_num == 0):

            return '0'
        
        elif (printable_num.real == 0):

            return f"{printable_num.imag}j"
        
        elif (printable_num.imag == 0):

            return f"{printable_num.real}"
        
        else:

            if (printable_num.imag > 0):

                return f"{printable_num.real}+{printable_num.imag}j"
            
            else:

                return f"{printable_num.real}-{-printable_num.imag}j"
            
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
