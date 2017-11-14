import pytest

from unitconvert import temperature
from unitconvert import distance

# for each function in unitconvert
# test known distance or temperature

def test_fahrenheit_to_celsius():
    should_be_10 = temperature.fahrenheit_to_celsius(50)
    assert round(should_be_10,4)==10
    negative_40  = temperature.fahrenheit_to_celsius(-40)
    assert round(negative_40,4)==-40

def test_celsius_to_fahrenheit():
    should_be_50 = temperature.celsius_to_fahrenheit(10)
    assert round(should_be_50,4)==50
    negative_40  = temperature.celsius_to_fahrenheit(-40)
    assert round(negative_40,4)==-40

def test_miles_to_kilometers():
    should_be_0 = distance.miles_to_kilometers(0)
    assert round(should_be_0,4)==0
    about_5k    = distance.miles_to_kilometers(3.1)
    assert round(about_5k,1)==5

def test_kilometers_to_miles():
    should_be_0 = distance.kilometers_to_miles(0)
    assert round(should_be_0,4)==0
    marathon    = distance.kilometers_to_miles(42.195)
    assert round(marathon,1)==26.2
