"""
This module implements complex numbers with components being Fractions.
"""
from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from math import sqrt
from numbers import Complex, Number, Rational
from typing import Union

Fractionable = Union[float, Decimal, Rational, str]


class ComplexFraction(Complex):
    """This class implements complex numbers with components being Fractions.

    In the 1 argument constructor a complex number or a string representation
    of a complex number is acceptable.

    The 2 argument constructor accepts 2 real numbers, 2 strings, or a combination.

    Note that 1/3j is interpreted by python as 1/(3j) == -0.333...j
    but for the purposes of this class "1/3j" is equivalent to (1/3)j.
    """

    __hash__ = None  # type: ignore

    def __init__(self, *args):

        if len(args) == 1:

            z = args[0]  # pylint: disable=invalid-name

            if isinstance(z, Complex):

                self._from_components(z.real, z.imag)

            elif isinstance(z, str):

                self._from_complex_str(z)

            else:
                raise TypeError(f"Expected {z} to be string or complex")

        elif len(args) == 2:

            real: Fractionable = args[0]

            imag: Fractionable = args[1]

            self._from_components(real, imag)

        else:
            raise TypeError(
                f"ComplexFraction expected at most 2 arguments, got {len(args)}"
            )

    @staticmethod
    def split_complex_str(z_str: str) -> tuple[str, str]:

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

        real_str = ""

        imag_str = ""

        if "j" in z_str:

            curr_pos = z_str.find("j")

            curr_char = z_str[curr_pos]

            imag_str = "j"

            while curr_pos > 0 and curr_char not in {"+", "-"}:

                curr_pos -= 1

                curr_char = z_str[curr_pos]

                imag_str = curr_char + imag_str

            real_str = z_str.replace(imag_str, "")

            real_str = real_str.replace("+", "")

            imag_str = imag_str.replace("*1j", "")

            imag_str = imag_str.replace("j", "")

            imag_str = imag_str.replace("+", "")

            if not real_str:

                real_str = "0"

        else:

            real_str = z_str

            real_str = real_str.replace("+", "")

            imag_str = "0"

        return real_str, imag_str

    def _from_complex_str(self, z_str: str):

        real_str, imag_str = ComplexFraction.split_complex_str(z_str)

        self._from_components(real_str, imag_str)

    def _from_components(self, real: Fractionable, imag: Fractionable):

        self._real = Fraction(real)

        self._imag = Fraction(imag)

    @property
    def real(self) -> Fraction:

        return self._real

    @property
    def imag(self) -> Fraction:

        return self._imag

    def __repr__(self) -> str:

        return f"ComplexFraction('{self.real}', '{self.imag}')"

    def __str__(self) -> str:

        printable_num: ComplexFraction = self.limit_denominator()

        if printable_num == 0:

            return "0"

        if printable_num.real == 0:

            return f"{printable_num.imag}j"

        if printable_num.imag == 0:

            return f"{printable_num.real}"

        if printable_num.imag > 0:

            return f"{printable_num.real}+{printable_num.imag}j"

        return f"{printable_num.real}-{-printable_num.imag}j"

    def __eq__(self, rhs) -> bool:

        if isinstance(rhs, ComplexFraction):

            return self.real == rhs.real and self.imag == rhs.imag

        if isinstance(rhs, (Complex, str)):

            return self == ComplexFraction(rhs)

        return NotImplemented

    def __neg__(self) -> ComplexFraction:

        return ComplexFraction(-self.real, -self.imag)

    def __pos__(self) -> ComplexFraction:

        return self

    def __add__(self, rhs: Number) -> ComplexFraction:

        try:

            rhs = ComplexFraction(rhs)

        except TypeError:

            return NotImplemented

        res_real = self.real + rhs.real

        res_imag = self.imag + rhs.imag

        return ComplexFraction(res_real, res_imag)

    def __radd__(self, lhs) -> ComplexFraction:

        return self + lhs

    def __sub__(self, rhs) -> ComplexFraction:

        try:

            rhs = ComplexFraction(rhs)

        except TypeError:

            return NotImplemented

        return self + (-rhs)

    def __rsub__(self, lhs) -> ComplexFraction:

        return -self + lhs

    def __mul__(self, rhs) -> ComplexFraction:

        try:

            rhs = ComplexFraction(rhs)

        except TypeError:

            return NotImplemented

        res_real = self.real * rhs.real - self.imag * rhs.imag

        res_imag = self.real * rhs.imag + self.imag * rhs.real

        return ComplexFraction(res_real, res_imag)

    def __rmul__(self, lhs) -> ComplexFraction:

        return self * lhs

    def conjugate(self) -> ComplexFraction:

        res_real = self.real

        res_imag = -self.imag

        return ComplexFraction(res_real, res_imag)

    def magnitude_squared(self) -> Fraction:
        """Returns the magnitude squared of the complex number."""

        return self.real**2 + self.imag**2

    def __abs__(self) -> float:  # type: ignore

        return sqrt(self.magnitude_squared())

    def reciprocal(self) -> ComplexFraction:
        """Returns the reciprocal of the complex number."""

        return self.conjugate() / self.magnitude_squared()

    def __truediv__(self, rhs) -> ComplexFraction:

        try:

            return self * (1 / rhs)

        except TypeError:

            rhs = ComplexFraction(rhs)

            return self * rhs.reciprocal()

    def __rtruediv__(self, lhs) -> ComplexFraction:

        return self.reciprocal() * lhs

    def limit_denominator(self, max_denominator=1000000) -> ComplexFraction:
        """Returns a new ComplexFraction that has had the denominators
        of it components limited to the given value."""

        new_real: Fraction = self.real.limit_denominator(max_denominator)

        new_imag: Fraction = self.imag.limit_denominator(max_denominator)

        return ComplexFraction(new_real, new_imag)

    def __complex__(self) -> complex:

        real: float = float(self.real)

        imag: float = float(self.imag)

        return complex(real, imag)

    def __pow__(self, power: Complex) -> ComplexFraction:

        if not isinstance(power, int):
            return ComplexFraction(complex(self) ** power)

        res = ComplexFraction(1, 0)

        for _ in range(abs(power)):

            res = res * self

        if power < 0:

            res = 1 / res

        return res

    def __rpow__(self, base: Complex) -> ComplexFraction:

        return ComplexFraction(base ** complex(self))
