'''
the Model module provides a set of tools for constructing geometric models
relies heavily on sympy for providing the algebraic infrastructure
the functions here are for creating the abstract model, not the rendering
see the Render module for plotting with matplotlib
'''
import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg
from sympy.abc import x, y

import math as math
import numpy as np
from collections import defaultdict
import logging


from multiprocessing import Pool, cpu_count

# constants
num_workers = cpu_count()

Φ = sp.GoldenRatio
phi = sp.Rational(1, 2) + (sp.sqrt(5) / 2)


def set_bounds(limx, limy):
    return sp.Polygon(
        point(limx[0], limy[1]),
        point(limx[0], limy[0]),
        point(limx[1], limy[0]),
        point(limx[1], limy[1])
        )

# structural elements
def point(x_val, y_val):
    '''make sympy.geometry.Point'''
    pt = spg.Point(sp.simplify(x_val), sp.simplify(y_val))
    return pt


def line(pt_a, pt_b):
    '''make sympy.geometry.Line'''
    el = spg.Line(pt_a, pt_b)
    return el


def circle(pt_c, pt_r):
    '''make sympy.geometry.Circle from two points'''
    el = spg.Circle(pt_c, pt_c.distance(pt_r))
    el.radius_pt = pt_r
    return el


# geaphical elements
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


# model ******************************
class Relations:
    parents = []
    descendents = []

points = defaultdict(Relations)
# points = defaultdict({'parents': [], 'desc': []})

pts = []
elements = []


def add_point(pt):
    logging.info(f'* add_point: {pt}')
    if isinstance(pt, spg.Point2D):
        if not pts.count(pt):
            pts.append(pt)
            logging.info(f'  + {pt}')
            return pt
        else:
            i = pts.index(pt)
            logging.info(f'  ! {pt} found at index: {i}')
            return pts[i]


def add_intersection_points(el):
    logging.info(f'* add_intersection_points: {el}')
    for prev in elements:
        for pt in el.intersection(prev):
            add_point(pt)

            
def add_intersection_points_mp(el):
    logging.info(f'* add_intersection_points: {el}')
    with Pool(num_workers) as pool:
        results = pool.map(el.intersection, elements)
        for result in results:
            for pt in result:
                add_point(pt)


def add_element(el):
    logging.info(f'* add_element: {el}')
    add_intersection_points_mp(el)
    if not elements.count(el):
        for prev in elements:
            diff = (prev.equation().simplify() - el.equation().simplify()).simplify()
            logging.info(f'    > diff: {diff}')
            if diff:
                elements.append(el)
                logging.info(f'  + {el}')
                return el
            else:
                logging.info(f'''
            ! COINCIDENT
                {el}
                {prev}
                ''')
                return prev
        else:
            elements.append(el)
            logging.info(f'  + {el}')
            return el
    else:
        logging.info(f'  ! {el} found at index: {elements.index(el)}')
        return el

    
# helpers ******************************
def begin():
    '''create inital two points -
    establishing the unit for the field'''
    pt = point(sp.Rational(-1, 2), 0)
    add_point(pt)
    pt = point(sp.Rational(1, 2), 0)
    add_point(pt)

def begin_zero():
    '''create inital two points -
    establishing the unit for the field'''
    pt = point(0, 0)
    add_point(pt)
    pt = point(1, 0)
    add_point(pt)

    
def bisector(pt1, pt2):
    '''perform fundamental operations for two points
    and add perpendicular bisector'''

    # baseline
    add_element(line(pt1, pt2))

    # vesica
    c1 = add_element(circle(pt1, pt2))
    c2 = add_element(circle(pt2, pt1))

    # bisector
    # last two points should be from the last two circles intersection
    el = line(pts[-1], pts[-2])
    add_element(el)
