"""
A python module for converting temperatures
"""

def fahrenheit_to_celsius(temperature_in_f):
    """Convert temperature from fahrenheit to celsius

    PARAMETERS
    ----------
    temperature_in_f : float
        A temperature in degrees Fahrenheit

    RETURNS
    -------
    temperature_in_c : float
        A temperature in degrees Celsius
    """
    temperature_in_c = 5/9*(temperature_in_f-32)
    print(temperature_in_c)
    return temperature_in_c

def celsius_to_fahrenheit(temperature_in_c):
    """Convert temperature from celsius to fahrenheit

    PARAMETERS
    ----------
    temperature_in_c : float
        A temperature in degrees Celsius

    RETURNS
    -------
    temperature_in_f : float
        A temperature in degrees Fahrenheit
    """
    temperature_in_f = 9/5*temperature_in_c+32
    print(temperature_in_f)
    return temperature_in_f

