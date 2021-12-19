# sympy setup *******************************
import math as math
import numpy as np

import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg
from sympy.abc import x, y

Φ = sp.GoldenRatio
phi = sp.Rational(1, 2) + (sp.sqrt(5) / 2)

# sp.init_printing()

def set_bounds(limx, limy):
    return sp.Polygon(
        point(limx[0], limy[1]),
        point(limx[0], limy[0]),
        point(limx[1], limy[0]),
        point(limx[1], limy[1])
        )

# create independent elements
def point(x_val, y_val):
    '''make sympy.geometry.Point'''
#     pt = spg.Point(x_val, y_val)
    pt = spg.Point(sp.simplify(x_val), sp.simplify(y_val))
    return pt


def circle(pt_c, pt_r):
    '''make sympy.geometry.Circle from two points'''
    el = spg.Circle(pt_c, pt_c.distance(pt_r))
    el.radius_pt = pt_r
    return el


def line(pt_a, pt_b):
    '''make sympy.geometry.Line'''
    el = spg.Line(pt_a, pt_b)
    return el


def segment(pt_a, pt_b):
    '''make sympy.geometry.Segment'''
    el = spg.Segment(pt_a, pt_b)
    return el


def polygon(poly_pts):
    '''- takes array of points - make sympy.geometry.Polygon, Triangle or Segment'''
    el = spg.Polygon(*poly_pts)
    return el


def polygon_ids(ids):
    '''create polygon from list of point ids'''
    return polygon([pts[i] for i in ids])


