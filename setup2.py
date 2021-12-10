''' general startup for GEOMETOR '''
import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg
from sympy.abc import x, y
import matplotlib as mp
import matplotlib.pyplot as mpp
from sympy.plotting.plot import List2DSeries
from collections import OrderedDict, defaultdict

sp.init_printing()

pts = []
elements = []

def mpp_init(limx, limy):
    '''configure the MatPlotLib stateful plot engine'''
    mp.style.use('dark_background')
    mpp.figure(num=1, figsize=(6, 4), dpi=120)
    mpp.gca().set_aspect('equal')
    # TODO: pass in limits
    x1, x2 = limx
    mpp.gca().set_xlim(x1, x2)
    y1, y2 = limy
    mpp.gca().set_ylim(y1, y2)
    mpp.gca().set_title('G E O M E T O R', fontdict={'color': '#960'})
    mpp.axis(False)
    mpp.tight_layout()

# create independent elements
def circle(pt_c, pt_r):
    '''make sympy.geometry.Circle from two points'''
    el = spg.Circle(pt_c, pt_c.distance(pt_r))
#     el.parents = [pt_c, pt_r] 
    return el

def line(pt_a, pt_b):
    '''make sympy.geometry.Line'''
    el = spg.Line(pt_a, pt_b)
#     el.parents = [pt_a, pt_b]
    return el

def point(pt_x, pt_y):
    '''make sympy.geometry.Point'''
    pt = spg.Point(pt_x, pt_y)
#     pt.parents = []
    return pt

# plot elements to mpp
def plot_circle(circle):
    '''takes a sympy circle and plots with the matplotlib Circle patch'''
    center = (circle.center.x.evalf(), circle.center.y.evalf())
    radius = circle.radius
    el = mpp.Circle(center, radius, color='#c09', linestyle=':', fill=False)
    ax = mpp.gca()
    ax.add_patch(el)
    
def plot_line(el, bounds):
    ends = bounds.intersection(el)
    xs = [pt.x.evalf() for pt in ends]
    ys = [pt.y.evalf() for pt in ends]

    mpp.plot(xs, ys, color='#999', linestyle=':', linewidth=1)    
    
def plot_points():
    '''plot all the points in pts'''
    # collect x, y values into separate arrays
    xs = [pt.x.evalf() for pt in pts]
    ys = [pt.y.evalf() for pt in pts]

    mpp.plot(xs, ys, 'ko')
    mpp.plot(xs, ys, 'w.')

def add_point(pt):
    if not pts.count(pt):
        pts.append(pt)
#     else:
#         print(f'point: {pt} found at index: {pts.index(pt)}')

def add_intersection_points(el):
    for prev in elements:
        for pt in el.intersection(prev):
#             pt.parents.extend([prev, el])
            add_point(pt)

def add_element(el):
    add_intersection_points(el)
    if not elements.count(el):
        elements.append(el)
    else:
        print(f'element: {el} found at index: {elements.index(el)}')


