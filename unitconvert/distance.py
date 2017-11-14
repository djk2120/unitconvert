"""
A python module for converting distances
"""
def miles_to_kilometers(d_in_miles):
    """Convert distance from miles to kilometers

    PARAMETERS
    ----------
    d_in_miles : float
        A distance in miles

    RETURNS
    -------
    d_in_kms : float
        A distance in kilometers
    """
    d_in_kms = 1.60934*d_in_miles
    return d_in_kms

def kilometers_to_miles(d_in_kms):
    """Convert distance from kilometers to miles

    PARAMETERS
    ----------
    d_in_kms : float
        A distance in kilometers

    RETURNS
    -------
    d_in_miles : float
        A distance in miles
    """
    d_in_miles = d_in_kms/1.60934
    return d_in_miles
