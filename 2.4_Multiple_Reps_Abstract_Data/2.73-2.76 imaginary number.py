from orderedPair import *
from dataOriented import *
from math import sin, cos, atan


# rectangular imaginary number system
def real_part(z):
    return car(z)


def imag_part(z):
    return cdr(z)


def make_from_real_imag(x, y):
    return cons(x, y)


def magnitude(z):
    return ((real_part(z)**2) + (imag_part(z)**2)) ** 0.5


def angle(z):
    return atan(imag_part(z)/real_part(z))


def make_from_mag_ang(r, a):
    return cons(r*cos(a), r*sin(a))


def tag(x):
    return attach_tag('rectangular', x)

put('real_part', 'rectangular', real_part)
put('imag_part', 'rectangular', imag_part)
put('magnitude', 'rectangular', magnitude)
put('angle', 'rectangular', angle)
put('make_from_real_imag', 'rectangular',
    lambda x, y: tag(make_from_real_imag(x, y)))
put('make_from_mag_ang', 'rectangular',
    lambda r, a: tag(make_from_mag_ang(r, a)))


# polar imaginary number system
def magnitude(z):
    return car(z)


def angle(z):
    return cdr(z)


def make_from_mag_ang(r, a):
    return cons(r, a)


def real_part(z):
    return magnitude(z) * cos(angle(z))


def imag_part(z):
    return magnitude(z) * sin(angle(z))


def make_from_real_imag(x, y):
    return cons((x**2 + y**2)**0.5, atan(y/x))


def tag(x):
    return attach_tag('polar', x)

put('real_part', 'polar', real_part)
put('imag_part', 'polar', imag_part)
put('magnitude', 'polar', magnitude)
put('angle', 'polar', angle)
put('make_from_real_imag', 'polar',
    lambda x, y: tag(make_from_real_imag(x, y)))
put('make_from_mag_ang', 'polar',
    lambda r, a: tag(make_from_mag_ang(r, a)))


# generic imaginary number system
def real_part(z):
    return appaly_generic('real_part', z)


def imag_part(z):
    return appaly_generic('imag_part', z)


def magnitude(z):
    return appaly_generic('magnitude', z)


def angle(z):
    return appaly_generic('angle', z)


def make_from_real_imag(x, y):
    return get('make_from_real_imag', 'rectangular')(x, y)


def make_from_mag_ang(r, a):
    return get('make_from_mag_ang', 'polar')(r, a)


if __name__ == '__main__':
    print(op_type_table)

