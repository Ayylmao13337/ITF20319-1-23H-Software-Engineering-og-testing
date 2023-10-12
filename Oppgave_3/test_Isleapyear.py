from Isleapyear import *


def test_isLeapYear_when_its_divisible_with_4_but_not_100():
    assert isLeapYear(2004) == True
    assert isLeapYear(1996) == True
    assert isLeapYear(4) == True
    assert isLeapYear(1200) == True
    assert isLeapYear(2096) == True

def test_isLeapYear_is_not_divisible_with_4():
    assert isLeapYear(1955) == False
    assert isLeapYear(2055) == False
    assert isLeapYear(1733) == False
    assert isLeapYear(1945) == False
    assert isLeapYear(2) == False

def test_isLeapYear_when_its_divisible_with_400():
    assert isLeapYear(2000) == True
    assert isLeapYear(400) == True
    assert isLeapYear(800) == True
    assert isLeapYear(1200) == True
    assert isLeapYear(1600) == True

def test_isLeapYear_divisible_with_100_but_not_4():
    assert isLeapYear(1900) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1700) == False
    assert isLeapYear(6900) == False
    assert isLeapYear(1500) == False