from py.test import raises

from rome import Roman


def test_single_digit_convertion_from_roman_to_arabic_numerals():
    assert Roman('I') == 1


def test_multiple_digit_convertion_from_roman_to_arabic_numerals():
    assert Roman('XVI') == 16


def test_passing_invalid_numeral_should_raise_value_error():
    with raises(ValueError):
        Roman('$%^')
