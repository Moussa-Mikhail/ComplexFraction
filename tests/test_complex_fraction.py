# pylint: disable=redefined-outer-name, missing-docstring
from fractions import Fraction

import pytest
from ..complex_fraction import ComplexFraction


@pytest.fixture
def real_num() -> ComplexFraction:

    return ComplexFraction("2.5", "0")


@pytest.fixture
def imag_num() -> ComplexFraction:

    return ComplexFraction("0", "-1/2")


@pytest.fixture
def complex_num() -> ComplexFraction:

    return ComplexFraction("1/3", "-1/4")


def test_init(complex_num):

    assert complex_num.real == Fraction("1/3")

    assert complex_num.imag == Fraction("-1/4")


def test_repr_real(real_num):

    assert real_num.__repr__() == "ComplexFraction('5/2', '0')"


def test_repr_imag(imag_num):

    assert imag_num.__repr__() == "ComplexFraction('0', '-1/2')"


def test_repr(complex_num):

    assert complex_num.__repr__() == "ComplexFraction('1/3', '-1/4')"


def test_str_real(real_num):

    assert real_num.__str__() == "5/2"


def test_str_imag(imag_num):

    assert imag_num.__str__() == "-1/2j"


def test_str(complex_num):

    assert complex_num.__str__() == "1/3-1/4j"


def test_eq(complex_num):

    assert complex_num == ComplexFraction("1/3", "-1/4")


def test_neg(complex_num):

    assert -complex_num == ComplexFraction("-1/3", "1/4")


def test_add(real_num, imag_num):

    assert real_num + imag_num == ComplexFraction("5/2", "-1/2")


def test_add_str(complex_num):
    # sourcery skip: use-fstring-for-concatenation

    assert complex_num + "1/3+1/4j" == ComplexFraction("2/3", "0")


def test_radd(complex_num):

    assert (1 + 1j) + complex_num == ComplexFraction("4/3", "3/4")


def test_radd_str(complex_num):
    # sourcery skip: use-fstring-for-concatenation

    assert "1/3+1/4j" + complex_num == ComplexFraction("2/3", "0")


def test_sub(complex_num, real_num):

    assert complex_num - real_num == ComplexFraction("1/3", "-1/4") - ComplexFraction(
        "5/2", "0"
    )


def test_sub_str(complex_num):

    assert complex_num - "1/6" == ComplexFraction("1/6", "-1/4")


def test_rsub(complex_num):

    assert 1 / 2 - complex_num == ComplexFraction("1/6", "1/4")


def test_rsub_str(complex_num):

    assert "1/6" - complex_num == ComplexFraction("-1/6", "1/4")


def test_mul(complex_num):

    assert complex_num * (1 / 2 + 1j) == ComplexFraction("10/24", "5/24")


def test_mul_str(complex_num):

    assert complex_num * "1/2+1j" == ComplexFraction("10/24", "5/24")


def test_rmul(complex_num):

    assert (1 / 2 + 1j) * complex_num == ComplexFraction("10/24", "5/24")


def test_rmul_str(complex_num):

    assert "1/2+1j" * complex_num == ComplexFraction("10/24", "5/24")


def test_truediv(complex_num):

    assert complex_num / (1 + 1j) == ComplexFraction("1/24", "-7/24")


def test_truediv_str(complex_num):

    assert complex_num / "1+1j" == ComplexFraction("1/24", "-7/24")


def test_rtruediv(complex_num):

    assert (1 + 1j) / complex_num == ComplexFraction("12/25", "84/25")


def test_rtruediv_str(complex_num):

    assert "1+1j" / complex_num == ComplexFraction("12/25", "84/25")


def test_conjugate(complex_num):

    assert complex_num.conjugate() == ComplexFraction("1/3", "1/4")


def test_mag_sq(complex_num):

    assert complex_num.magnitude_squared() == Fraction("1/9") + Fraction("1/16")


def test_reciprocal(complex_num):

    assert complex_num.reciprocal() == ComplexFraction("1/3", "1/4") / (
        Fraction("1/9") + Fraction("1/16")
    )


def test_pow_pos_int(complex_num):

    assert complex_num**2 == complex_num * complex_num


def test_pow_neg_int(complex_num):

    assert complex_num**-2 == 1 / (complex_num * complex_num)


#  split_complex_str tests  #


def test_real_str_1():

    assert ComplexFraction.split_complex_str("1.1") == ("1.1", "0")


def test_real_str_2():

    assert ComplexFraction.split_complex_str("-1/3") == ("-1/3", "0")


def test_imag_str_1():

    assert ComplexFraction.split_complex_str("1.1j") == ("0", "1.1")


def test_imag_str_2():

    assert ComplexFraction.split_complex_str("-11/10j") == ("0", "-11/10")


def test_complex_str_1():

    assert ComplexFraction.split_complex_str("1+1j") == ("1", "1")


def test_complex_str_2():

    assert ComplexFraction.split_complex_str("1/3+1j") == ("1/3", "1")


def test_complex_str_3():

    assert ComplexFraction.split_complex_str("-1/3+1j") == ("-1/3", "1")


def test_complex_str_4():

    assert ComplexFraction.split_complex_str("-1.1-2.1j") == ("-1.1", "-2.1")


def test_complex_str_5():

    assert ComplexFraction.split_complex_str("-1.1j-2.1") == ("-2.1", "-1.1")


def test_complex_str_6():

    assert ComplexFraction.split_complex_str("-11/10j+2.1") == ("2.1", "-11/10")


#  end split_complex_str tests  #
