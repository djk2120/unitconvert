import numpy as np
import pytest

from unitconvert import temperature
from unitconvert import distance

def test_fahrenheit_to_celsius():
    should_be_10 = temperature.fahrenheit_to_celsius(50)
    np.testing.assert_allclose(should_be_10, 10, rtol=1e-5)
    negative_40  = temperature.fahrenheit_to_celsius(-40)
    np.testing.assert_allclose(negative_40,-40, rtol=1e-5)

def test_celsius_to_fahrenheit():
    should_be_50 = temperature.celsius_to_fahrenheit(10)
    np.testing.assert_allclose(should_be_50, 50, rtol=1e-5)
    negative_40  = temperature.celsius_to_fahrenheit(-40)
    np.testing.assert_allclose(negative_40,-40, rtol=1e-5)

def test_miles_to_kilometers():
    should_be_0 = distance.miles_to_kilometers(0)
    np.testing.assert_allclose(should_be_0, 0, rtol=1e-5)
    about_5k    = distance.miles_to_kilometers(3.1)
    np.testing.assert_allclose(about_5k, 5, rtol=1e-1)

def test_kilometers_to_miles():
    should_be_0 = distance.kilometers_to_miles(0)
    np.testing.assert_allclose(should_be_0, 0, rtol=1e-5)
    marathon    = distance.kilometers_to_miles(42.195)
    np.testing.assert_allclose(marathon, 26.2, rtol=1e-1)
