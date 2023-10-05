import pytest

def fizzbuzz(number):
    return str(number)


def test_one_is_one():
    assert fizzbuzz(1) == "1"

def test_two_is_two():
    assert fizzbuzz(2) == "2"

i = 0

for i in range(0,100):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
