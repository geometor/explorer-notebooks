'''
The Render Module 
provides functions for plotting elements from the geoemtric model to
matplotlib.
'''

import matplotlib as mp
import matplotlib.pyplot as plt
import mplcursors

import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg

import logging
import math as math

fig, ax = plt.subplots()

style_radius = {'color': '#c099', 'marker': ''}

classes = {}
classes['blue'] = {'color':'b', 'linestyle':':'}
classes['red'] = {'color':'r', 'linestyle':':'}
classes['green'] = {'color':'g', 'linestyle':':'}

classes['circle'] = {'under_color':'#0FF', 'under_markersize':7, 'under_marker':'o'}
classes['square'] = {'under_color':'#FF0', 'under_markersize':7, 'under_marker':'s'}
classes['diamond'] = {'under_color':'#F0F', 'under_markersize':7, 'under_marker':'D'}



def plt_init(limx='', limy=''):
    '''configure the MatPlotLib stateful plot engine'''
    mp.style.use('dark_background')
    plt.figure(num=1, figsize=(7, 5), dpi=120)
    plt.gca().set_aspect('equal')

    if limx:
        plt.gca().set_xlim(limx[0], limx[1])
    if limy:
        plt.gca().set_ylim(limy[0], limy[1])
    plt.gca().set_title('G E O M E T O R', fontdict={'color': '#960', 'size':'small'})
    plt.axis(False)
    plt.tight_layout()
    
def plt_init_polar():
    '''configure the MatPlotLib stateful plot engine'''
    mp.style.use('dark_background')
    # plt.figure(num=1, figsize=(6.4, 3.6), dpi=120)
    # fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    
    # plt.gca().set_aspect('equal')
    
#     ax.set_title('G E O M E T O R', fontdict={'color': '#960', 'size':'small'})
#     ax.set_axis_off()
    
    # plt.axis(False)
    # plt.tight_layout()


# plot elements to plt
def plot_circle(circle, color='#c09', linestyle=':', fill=False):
    '''takes a sympy circle and plots with the matplotlib Circle patch'''
    center = (circle.center.x.evalf(), circle.center.y.evalf())
    radius = circle.radius
    el = plt.Circle(center, radius, color=color, linestyle=linestyle, fill=fill)
    plt.gca().add_patch(el)


def plot_line(el, bounds, color='#999', linestyle=':', linewidth=1):
    ends = bounds.intersection(el)
    xs = [pt.x.evalf() for pt in ends]
    ys = [pt.y.evalf() for pt in ends]
    
    #  style = {}
    #  for cl in el.classes:
        #  cl_style = classes[cl]
        #  style.update(cl_style)
        

    plt.plot(xs, ys, color=color, linestyle=linestyle, linewidth=linewidth)

    
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


def plot_points(pts, 
               under_color='k',
               under_linestyle='',
               under_marker='.',
               under_markersize=10,
               over_color='w',
               over_linestyle='',
               over_marker='.',
               over_markersize=5,
               add_to_cursors=True, 
               ):
    '''plot all the points in pts'''
    # collect x, y values into separate arrays
    xs = [pt.x.evalf() for pt in pts]
    ys = [pt.y.evalf() for pt in pts]

    def on_add(sel):
        i = sel.index
        sel.annotation.set_text(f'{i}:\nx: {pts[i].x}\ny: {pts[i].y}')
        xval = str(pts[i].x).replace('GoldenRatio', 'Φ')
        yval = str(pts[i].y).replace('GoldenRatio', 'Φ')
        sel.annotation.set_text(f'{i}:\nx: {xval}\ny: {yval}')
        sel.annotation.arrow_patch.set(arrowstyle="simple", ec="k", fc='w')
    
    #under marker
    plt.plot(xs, ys, 
            color=under_color, 
            linestyle=under_linestyle,
            marker=under_marker,
            markersize=under_markersize
            )
    
    #over marker
    # use output for mpl cursors
    point_plot = plt.plot(xs, ys, 
            color=over_color, 
            linestyle=over_linestyle,
            marker=over_marker,
            markersize=over_markersize
            )
    
    if add_to_cursors:
        cursor = mplcursors.cursor(point_plot)
        cursor.connect("add", on_add)

def plot_segment(pt1, pt2, color='#fc09', linestyle='-', linewidth=3, marker='.', markersize=16):
    x1 = pt1.x.evalf()
    x2 = pt2.x.evalf()
    y1 = pt1.y.evalf()
    y2 = pt2.y.evalf()
    plt.plot(
            [x1, x2], [y1, y2], 
            color=color, 
            linestyle=linestyle, 
            linewidth=linewidth, 
            marker=marker,
            markersize=markersize)
    return pt1.distance(pt2)

def plot_segment2(seg, color='#fc09', linestyle='-', linewidth=3, marker='.', markersize=16):
    x1 = seg.points[0].x.evalf()
    x2 = seg.points[1].x.evalf()
    y1 = seg.points[0].y.evalf()
    y2 = seg.points[1].y.evalf()
    plt.plot(
            [x1, x2], [y1, y2], 
            color=color, 
            linestyle=linestyle, 
            linewidth=linewidth, 
            marker=marker,
            markersize=markersize)
    return seg.length


def plot_polygon(poly, color='#36c3', linestyle='-', linewidth=3):
    '''takes a sympy Polygon and plots with the matplotlib Polygon patch'''
    xy = [(pt.x.evalf(), pt.y.evalf()) for pt in poly.vertices]
    # print(xy)
    patch = plt.Polygon(xy, color=color, linestyle=linestyle, fill=True)
    plt.gca().add_patch(patch)
    

def plot_polygons(poly_array):
    for poly in poly_array:
        plot_polygon(poly)
    

def plot_wedge(ctr_pt, rad_pt, sweep_pt, color='#0f03', linestyle='', linewidth=6, fill=True):
    '''takes a sympy circle and plots with the matplotlib Circle patch'''
    center = (float(ctr_pt.x.evalf()), float(ctr_pt.y.evalf()))
    rad_val = float(ctr_pt.distance(rad_pt).evalf())
    print(center, rad_val)
    radius_line = spg.Line(ctr_pt, rad_pt)
    sweep_line = spg.Line(ctr_pt, sweep_pt)
    base_line = spg.Line(spg.Point(0,0), spg.Point(1,0))
    
    # t = polygon
    a1 = math.degrees(base_line.angle_between(radius_line).evalf())
    a2 = math.degrees(base_line.angle_between(sweep_line).evalf())
    cy = float(ctr_pt.y.evalf())
    ry = float(rad_pt.y.evalf())
    if cy > ry:
        a1 = -a1
    print(a1, a2)
    el = mp.patches.Wedge(center, rad_val, a1, a2, 
                          color=color, 
                          linestyle=linestyle, 
                          linewidth=linewidth, 
                          fill=fill ) 
    plt.gca().add_patch(el)

def plot_wedge_2(ctr_pt, rad_val, a1, a2, fc='#0ff1', ec='#0002', linestyle='', linewidth=6, fill=True):
    '''light wrapper for Wegde patch'''
    center = (float(ctr_pt.x.evalf()), float(ctr_pt.y.evalf()))
    el = mp.patches.Wedge(center, rad_val, a1, a2, 
                          fc=fc, 
                          ec=ec, 
                          linestyle=linestyle, 
                          linewidth=linewidth, 
                          fill=fill ) 
    plt.gca().add_patch(el)


# images**********************
def snapshot(filename):
    plt.savefig(filename)
                
def display(filename):
    from IPython import display
    display.Image(filename)

