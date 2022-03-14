'''
The Model module provides a set of tools for constructing geometric models.
It relies heavily on sympy for providing the algebraic infrastructure
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

from itertools import permutations, combinations

from multiprocessing import Pool, cpu_count

# constants
num_workers = cpu_count()

Φ = sp.GoldenRatio
phi = sp.Rational(1, 2) + (sp.sqrt(5) / 2)

# globals
history = []
pts = []
elements = []
polygons = []


def get_limits_from_points(pts, margin=1):
    '''find x, y limits from a set of points'''
    limx = [0, 0]
    limy = [0, 0]

    for pt in pts:
        ptx = float(pt.x.evalf())
        pty = float(pt.y.evalf())
        # print(x, y)
        limx[0] = ptx if limx[0] > ptx else limx[0]
        limx[1] = ptx if limx[1] < ptx else limx[1]
        limy[0] = pty if limy[0] > pty else limy[0]
        limy[1] = pty if limy[1] < pty else limy[1]

    limx[0] -= margin
    limx[1] += margin
    limy[0] -= margin
    limy[1] += margin
    
    return [limx, limy]
    


def set_bounds(limx, limy):
    return sp.Polygon(
        point(limx[0], limy[1]),
        point(limx[0], limy[0]),
        point(limx[1], limy[0]),
        point(limx[1], limy[1])
        )

# structural elements
def point(x_val, y_val, parents=set(), classes=[], style={}):
    '''make sympy.geometry.Point'''
    pt = spg.Point(sp.simplify(x_val), sp.simplify(y_val))
    pt.elements = parents
    pt.classes = classes
    pt.style = style
    return pt


def line(pt_a, pt_b, classes=[], style={}):
    '''make sympy.geometry.Line'''
    el = spg.Line(pt_a, pt_b)
    el.pts = {pt_a, pt_b}
    el.classes = classes
    el.style = style
    return el


def circle(pt_c, pt_r, classes=[], style={}):
    '''make sympy.geometry.Circle from two points'''
    el = spg.Circle(pt_c, pt_c.distance(pt_r))
    el.radius_pt = pt_r
    el.pts = {pt_r}
    el.classes = classes
    el.style = style
    return el


# graphical elements
def segment(pt_a, pt_b, classes=[], style={}):
    '''make sympy.geometry.Segment'''
    el = spg.Segment(pt_a, pt_b)
    el.classes = classes
    el.style = style
    return el


def polygon(poly_pts, classes=[], style={}):
    '''- takes array of points - make sympy.geometry.Polygon, Triangle or Segment'''
    el = spg.Polygon(*poly_pts)
    el.classes = classes
    el.style = style
    return el


def polygon_ids(ids, classes=[], style={}):
    '''create polygon from list of point ids'''
    return polygon([pts[i] for i in ids], classes=classes, style=style)


def unit_square(pt, classes=[], style={}):
    '''creates a unit square from the reference point
    adds points and returns polygon'''
    poly_pts = []
    poly_pts.append(pt)
    poly_pts.append(point(pt.x + 1, pt.y))
    poly_pts.append(point(pt.x + 1, pt.y + 1))
    poly_pts.append(point(pt.x, pt.y + 1))
    return polygon(poly_pts, classes=classes, style=style)



# model ******************************

def add_point(pt):
    '''add point to pts list - check if exists first'''
    logging.info(f'* add_point: {pt}')
    if isinstance(pt, spg.Point2D):
        if not pts.count(pt):
            pts.append(pt)
            history.append(pt)
            logging.info(f'  + {pt}')
            return pt
        else:
            i = pts.index(pt)
            logging.info(f'  ! {pt} found at index: {i}')
            return pts[i]
    else:
        logging.info('    not a point')


def add_points(pt_array):
    '''add an array of points to pts list'''
    for pt in pt_array:
        add_point(pt)


def add_intersection_points(el):
    logging.info(f'* add_intersection_points: {el}')
    for prev in elements:
        for pt in el.intersection(prev):
            pt.classes = []
            pt.elements = {el, elements[index]}
            add_point(pt)

            
def add_intersection_points_mp(el):
    logging.info(f'* add_intersection_points: {el}')
    with Pool(num_workers) as pool:
        results = pool.map(el.intersection, elements)
        for index, result in enumerate(results):
            for pt in result:
                pt.classes = []
                pt.elements = set()
                pt = add_point(pt)
                pt.elements.update({el, elements[index]})
                el.pts.add(pt)
                elements[index].pts.add(pt)


def add_element(el):
    logging.info(f'* add_element: {el}')
    # check if el is in the element list
    if not elements.count(el):
        # if not found by count, test each element anyway
        for prev in elements:

            #TODO: refine test of elements
            diff = (prev.equation().simplify() - el.equation().simplify()).simplify()
            #  logging.info(f'    > diff: {diff}')
            if not diff:
                logging.info(f'''
            ! COINCIDENT
                {el}
                {prev}
                ''')
                return prev
        else:
            history.append(el)
            add_intersection_points_mp(el)
            elements.append(el)
            logging.info(f'  + {el}')
            return el
    else:
        i = elements.index(el)
        logging.info(f'  ! {el} found at index: {i}')
        return elements[i]

def add_polygon(poly):
    polygons.append(poly)
    history.append(poly)
    return poly
    
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

    
def get_pts_by_class(classname):
    '''find all points with specifdied classname'''
    pts_by_class = []
    for pt in pts:
        if pt.classes.count(classname):
            pts_by_class.append(pt)
    return pts_by_class

def get_elements_by_class(classname):
    '''find all elements with specifdied classname'''
    elements_by_class = []
    for el in elements:
        if el.classes.count(classname):
            elements_by_class.append(el)
    return elements_by_class


def line_get_y(l1, x):
    '''return y value for specific x'''
    a, b, c = l1.coefficients
    return (-a * x - c) / b


def spread(l1, l2):
    '''calculate the spread of two lines'''
    a1, a2, a3 = l1.coefficients
    b1, b2, b3 = l2.coefficients

    spread = ((a1*b2 - a2*b1) ** 2) / ( (a1 ** 2 + b1 ** 2) * (a2 ** 2 + b2 ** 2) )
    return spread


def compare_points(pt1, pt2):
    if pt1.x.evalf() > pt2.x.evalf():
        return 1
    elif pt1.x.evalf() < pt2.x.evalf():
        return -1
    else:
        if pt1.y.evalf() > pt2.y.evalf():
            return 1
        elif pt1.y.evalf() < pt2.y.evalf():
            return -1
        else:
            return 0

def point_value(pt):
    #  return pt.x.evalf()
    return (pt.x.evalf(), pt.y.evalf())

def check_range(r):
    pass

def analyze_line(line):
    line_pts = sorted(list(line.pts), key=point_value)
    for pt in line_pts:
        print(pt.x, pt.x.evalf(), pt.y, pt.y.evalf())
    ranges = list(combinations(line_pts, 4))
    for r in ranges:
        print(r)
    
