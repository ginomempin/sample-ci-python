
import numpy


def generate_integers(start, stop, step):
    return numpy.arange(start, stop, step, dtype=int)


# This is for checking that code coverage will be <100%.
def generate_something():
    return True
