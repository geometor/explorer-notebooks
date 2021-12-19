''' general startup for GEOMETOR '''
from collections import defaultdict

import logging

def log_init(name):
    filename = f'logs/{name}.log'
    with open(filename, 'w'):
        pass

    logging.basicConfig(
            filename=f'logs/{name}.log', 
            filemode='w', 
            encoding='utf-8', 
            level=logging.INFO
            )
    logging.info(f'Init {name}')

# time *********************
import datetime
from timeit import default_timer as timer

def elapsed(start_time):
    secs = timer() - start_time
    return str(datetime.timedelta(seconds=secs))

# multiprocessing *************************************
from multiprocessing import Pool, cpu_count
num_workers = cpu_count()

# sympy setup *******************************
import math as math
import numpy as np

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




# matplotlib ************************************
import matplotlib as mp
import matplotlib.pyplot as plt
import mplcursors

fig, ax = plt.subplots()


def plt_init(limx, limy):
    '''configure the MatPlotLib stateful plot engine'''
    mp.style.use('dark_background')
    plt.figure(num=1, figsize=(7, 5), dpi=120)
    plt.gca().set_aspect('equal')
    # TODO: pass in limits
    x1, x2 = limx
    ax.set_xlim(x1, x2)
    y1, y2 = limy
    plt.gca().set_ylim(y1, y2)
    plt.gca().set_title('G E O M E T O R', fontdict={'color': '#960', 'size':'small'})
    plt.axis(False)
    plt.tight_layout()


# plot elements to plt
def plot_circle(circle):
    '''takes a sympy circle and plots with the matplotlib Circle patch'''
    center = (circle.center.x.evalf(), circle.center.y.evalf())
    radius = circle.radius
    el = plt.Circle(center, radius, color='#c09', linestyle=':', fill=False)
    plt.gca().add_patch(el)


def plot_line(el, bounds):
    ends = bounds.intersection(el)
    xs = [pt.x.evalf() for pt in ends]
    ys = [pt.y.evalf() for pt in ends]

    plt.plot(xs, ys, color='#999', linestyle=':', linewidth=1)

    
def plot_perp_bisector(el, bounds):
    ends = bounds.intersection(el)
    xs = [pt.x.evalf() for pt in ends]
    ys = [pt.y.evalf() for pt in ends]

    plt.plot(xs, ys, color='#393', linestyle='-.', linewidth=1)

    
def plot_elements(elements, bounds):
    for el in elements:
        if type(el) == sp.Line2D:
            plot_line(el, bounds)
        elif type(el) == sp.Circle:
            plot_circle(el)
        else:
            print('No Match')


def plot_points(pts):
    '''plot all the points in pts'''
    # collect x, y values into separate arrays
    xs = [pt.x.evalf() for pt in pts]
    ys = [pt.y.evalf() for pt in pts]

    plt.plot(xs, ys, 
            color='k', 
            linestyle='',
            marker='.',
            markersize=10
            )
    point_plot = plt.plot(xs, ys, 
            color='w', 
            linestyle='',
            marker='.',
            markersize=5
            )
    cursor = mplcursors.cursor(point_plot)

    def on_add(sel):
        i = sel.index
        sel.annotation.set_text(f'{i}:\nx: {pts[i].x}\ny: {pts[i].y}')
        xval = str(pts[i].x).replace('GoldenRatio', 'Φ')
        yval = str(pts[i].y).replace('GoldenRatio', 'Φ')
        sel.annotation.set_text(f'{i}:\nx: {xval}\ny: {yval}')
        sel.annotation.arrow_patch.set(arrowstyle="simple", ec="k", fc='w')

    cursor.connect("add", on_add)

def plot_segment(pt1, pt2):
    x1 = pt1.x.evalf()
    x2 = pt2.x.evalf()
    y1 = pt1.y.evalf()
    y2 = pt2.y.evalf()
    plt.plot(
            [x1, x2], [y1, y2], 
            color='#fc09', 
            linestyle='-', 
            linewidth=3, 
            marker='.',
            markersize=16)
    return pt1.distance(pt2)

def plot_segment2(seg):
    x1 = pt1.x.evalf()
    x2 = pt2.x.evalf()
    y1 = pt1.y.evalf()
    y2 = pt2.y.evalf()
    plt.plot(
            [x1, x2], [y1, y2], 
            color='#fc09', 
            linestyle='-', 
            linewidth=3, 
            marker='.',
            markersize=16)
    return pt1.distance(pt2)


def plot_polygon(poly, color='#36c3'):
    '''takes a sympy Polygon and plots with the matplotlib Polygon patch'''
    xy = [(pt.x.evalf(), pt.y.evalf()) for pt in poly.vertices]
    # print(xy)
    patch = plt.Polygon(xy, color=color, linestyle='-', fill=True)
    plt.gca().add_patch(patch)


    


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
