import numpy

def perpendicular(vector, direction="+"):
    if direction == "+":
        return [-vector[1], vector[0]]
    else:
        return [vector[1], -vector[0]]

def norm(vector):
    mod = modulo(vector)
    return [vector[0] / mod, vector[1] / mod]

def modulo(vector):
    from math import sqrt
    return sqrt(vector[0]**2 + vector[1]**2)

def norm_perpen(vector, direction):
    return norm(perpendicular(vector, direction))

def dot(v1, v2):
    a = numpy.array(v1)
    b = numpy.array(v2)
    
    return numpy.dot(a,b)

def cross(v1, v2):
    a = numpy.array(v1)
    b = numpy.array(v2)
    
    return numpy.cross(a,b)