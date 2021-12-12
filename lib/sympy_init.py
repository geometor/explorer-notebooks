'''sympy setup'''
import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg
from sympy.abc import x, y

Φ = sp.GoldenRatio

sp.init_printing()

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


