import pytest
from isleapyear import *


def test_isLeapYear_Når_det_er_delelig_med_4_men_ikke_100():
    assert isLeapYear(2004) == True
    assert isLeapYear(1996) == True
    assert isLeapYear(4) == True
    assert isLeapYear(1200) == True
    assert isLeapYear(2096) == True

def test_isLeapYear_er_ikke_delielig_med_4():
    assert isLeapYear(1955) == False
    assert isLeapYear(2055) == False
    assert isLeapYear(1733) == False
    assert isLeapYear(1945) == False
    assert isLeapYear(2) == False

def test_isLeapYear_når_det_er_400():
    assert isLeapYear(2000) == True
    assert isLeapYear(400) == True
    assert isLeapYear(800) == True
    assert isLeapYear(1200) == True
    assert isLeapYear(1600) == True

def test_isLeapYear_delelig_med_100men_ikke_4():
    assert isLeapYear(1900) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1700) == False
    assert isLeapYear(6900) == False
    assert isLeapYear(1500) == False