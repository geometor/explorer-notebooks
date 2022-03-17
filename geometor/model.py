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
        for prev_pt in pts:
            if pt.equals(prev_pt):
                i = pts.index(prev_pt)
                logging.info(f'  ! {pt} found at index: {i}')
                # merge parents of points
                if hasattr(pt, 'elements'):
                    if hasattr(prev_pt, 'elements'):
                        prev_pt.elements.update(pt.elements)
                return prev_pt
        else:
            pts.append(pt)
            history.append(pt)
            logging.info(f'  + {pt}')
            return pt
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
    pt = point(sp.Rational(-1, 2), 0, classes=['start'])
    add_point(pt)
    pt = point(sp.Rational(1, 2), 0, classes=['start'])
    add_point(pt)

def begin_zero():
    '''create inital two points -
    establishing the unit for the field'''
    pt = point(0, 0, classes=['start'])
    add_point(pt)
    pt = point(1, 0, classes=['start'])
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



def check_golden(section):
    '''check range of three points for golden section'''
    ab = segment(section[0], section[1]).length.simplify()
    bc = segment(section[1], section[2]).length.simplify()
    print('            ', ab)
    print('            ', bc)
    #  ratio = ab ** 2 / bc ** 2
    ratio = ab / bc 
    #  ratio = sp.simplify(ratio)
    print('            ', ratio)
    chk1 = (ratio / phi).evalf()
    print('            ', chk1)
    chk2 = (ratio / (1 / phi)).evalf()
    print('            ', chk2)
    #  if ratio == (1 / phi) or ratio == (phi):
    if chk1 == 1 or chk2 == 1:
        return True
    else:
        return False
    

def analyze_golden_lines(lines):
    sections = []

    print('\nGolden Sections')
    print('lines:', len(lines))
    print()

    for i, el in enumerate(lines):
        print(i, el.coefficients)
        sections.extend(analyze_golden(el))
    
    return sections


    
def analyze_golden(line):
    '''gecj all the points on a line for Golden Sections'''
    goldens = []
    line_pts = sorted(list(line.pts), key=point_value)
    sections = list(combinations(line_pts, 3))
    print('    points: ', len(line_pts))
    print('    sections: ', len(sections))
    #  for i, r in enumerate(sections):
        #  print(f'        {i} {r}')
        #  ab = segment(r[0], r[1])
        #  bc = segment(r[1], r[2])
        #  chk = check_golden(r)
        #  if chk:
            #  print(f'            GOLDEN!')
            #  goldens.append([ab, bc])
    with Pool(num_workers) as pool:
        results = pool.map(check_golden, sections)
        for index, result in enumerate(results):
            if result:
                section = sections[index]
                #  print(f'            GOLDEN!')
                ab = segment(section[0], section[1])
                bc = segment(section[1], section[2])
                goldens.append([ab, bc])
            
    print('    goldens: ', len(goldens))
    return goldens
    

def check_range(r):
    ad = segment(r[0], r[3]).length
    db = segment(r[3], r[1]).length
    ac = segment(r[0], r[2]).length
    cb = segment(r[2], r[1]).length
    return sp.simplify((ad / db) / (ac / cb))
    

def analyze_line(line):
    line_pts = sorted(list(line.pts), key=point_value)
    #  for pt in line_pts:
        #  print(pt.x, pt.x.evalf(), pt.y, pt.y.evalf())
    ranges = list(combinations(line_pts, 4))
    for r in ranges:
        chk = check_range(r)
        #  if chk == 1 or chk == -1:
        if True:
            print(r)
            print(chk)
    
