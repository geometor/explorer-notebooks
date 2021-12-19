'''setup for matplot lib'''

import matplotlib as mp
import matplotlib.pyplot as plt
import mplcursors

import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg

import logging
import math as math

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
    

def plot_wedge(ctr_pt, rad_pt, sweep_pt, color='#0f03', linestyle='', linewidth=6, fill=True):
    '''takes a sympy circle and plots with the matplotlib Circle patch'''
    center = (float(ctr_pt.x.evalf()), float(ctr_pt.y.evalf()))
    rad_val = float(ctr_pt.distance(rad_pt).evalf())
    print(center, rad_val)
    radius_line = spg.Line(ctr_pt, rad_pt)
    sweep_line = spg.Line(ctr_pt, sweep_pt)
    a1 = math.degrees(elements[0].angle_between(radius_line).evalf())
    a2 = math.degrees(elements[0].angle_between(sweep_line).evalf())
    cy = float(ctr_pt.y.evalf())
    ry = float(rad_pt.y.evalf())
    if cy > ry:
        a1 = -a1
    print(a1, a2)
    el = mp.patches.Wedge(center, rad_val, -a1, a2, 
                          color=color, 
                          linestyle=linestyle, 
                          linewidth=linewidth, 
                          fill=fill ) 
    plt.gca().add_patch(el)


