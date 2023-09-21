# Comment just 1 line

"""
Comment multi-line
Hi

"""

# An example from PEP257 of a multi-line docstring.
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex
    

# An example on a user-defined function.
def number_to_the_power_of(number_one, number_two):
    """Raise a number to an arbitrary power.

    :param number_one: int the base number.
    :param number_two: int the power to raise the base number to.
    :return: int - number raised to power of second number

    Takes number_one and raises it to the power of number_two, returning the result.
    """

    return number_one ** number_two

print(number_to_the_power_of(5,2))      # put print to show the result

print(number_to_the_power_of.__doc__)    # show the comment lines

print(complex.__doc__)