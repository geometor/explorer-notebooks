'''sympy setup'''
import numpy as np  # putting this here for now

import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg
from sympy.abc import x, y

Φ = sp.GoldenRatio
phi = sp.Rational(1, 2) + (sp.sqrt(5) / 2)

sp.init_printing()

def set_bounds(limx, limy):
    return sp.Polygon(
        point(limx[0], limy[1]),
        point(limx[0], limy[0]),
        point(limx[1], limy[0]),
        point(limx[1], limy[1])
        )

# create independent elements
def circle(pt_c, pt_r):
    '''make sympy.geometry.Circle from two points'''
    el = spg.Circle(pt_c, pt_c.distance(pt_r))
    return el


def line(pt_a, pt_b):
    '''make sympy.geometry.Line'''
    el = spg.Line(pt_a, pt_b)
    return el


def point(pt_x, pt_y):
    '''make sympy.geometry.Point'''
    pt = spg.Point(pt_x, pt_y)
    return pt


