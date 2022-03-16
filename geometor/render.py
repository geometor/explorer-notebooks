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

plt.rcParams['figure.figsize'] = [16, 9]
plt.style.use('dark_background')

style_radius = {'color': '#c099', 'marker': ''}

classes = {}
classes['blue'] = {'color':'#33F', 'linestyle':':'}
classes['red'] = {'color':'#F33', 'linestyle':':'}
classes['green'] = {'color':'#2F2', 'linestyle':':'}
classes['gold'] = {'color':'#C90', 'linestyle':':'}
classes['pappus'] = {'linestyle':'-'}
classes['bisector'] = {'linestyle':'-.'}

classes['goldpt'] = {'color':'#C90', 'markersize':7, 'marker':'o'}

classes['circle'] = {'color':'#0FF', 'markersize':7, 'marker':'o'}
classes['square'] = {'color':'#FF0', 'markersize':7, 'marker':'s'}
classes['diamond'] = {'color':'#F0F', 'markersize':7, 'marker':'D'}


classes['yellow'] = {'edgecolor':'#FF09', 'facecolor':'#FF03', 'linestyle':'-', 'linewidth':1}
classes['cyan'] = {'color':'#0FF3', 'linestyle':'-'}
classes['magenta'] = {'color':'#F0F3', 'linestyle':'-'}


def plt_init(limx='', limy=''):
    '''configure the MatPlotLib stateful plot engine'''
    plt.style.use('dark_background')
    #  plt.figure(num=1, figsize=(7, 5), dpi=120)
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


def plot_circle(ax, circle, color='#c09', linestyle=':', linewidth=1, fill=False):
    '''takes a sympy circle and plots with the matplotlib Circle patch'''
    center = (circle.center.x.evalf(), circle.center.y.evalf())
    radius = circle.radius
    styles = {'color':color, 'linestyle':linestyle, 'linewidth':linewidth, 'fill':fill}
    for cl in circle.classes:
        if cl in classes:
            styles.update(classes[cl])

    patch = plt.Circle(center, radius, **styles)
    ax.add_patch(patch)


def plot_line(ax, el, bounds, color='#999', linestyle=':', linewidth=1):
    ends = bounds.intersection(el)
    xs = [pt.x.evalf() for pt in ends]
    ys = [pt.y.evalf() for pt in ends]

    styles = {'color':color, 'linestyle':linestyle, 'linewidth':linewidth}
    for cl in el.classes:
        if cl in classes:
            styles.update(classes[cl])

    ax.plot(xs, ys, **styles)


def plot_elements(ax, elements, bounds):
    for el in elements:
        if type(el) == sp.Line2D:
            plot_line(ax, el, bounds)
        elif type(el) == sp.Circle:
            plot_circle(ax, el)
        else:
            print('No Match')


def plot_points(ax, pts,
               color='w',
               linestyle='',
               marker='.',
               markersize=5,
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

    point_plot = ax.plot(xs, ys,
            color='k',
            linestyle=linestyle,
            marker=marker,
            markersize=markersize+3
            )
    # use output for mpl cursors
    point_plot = ax.plot(xs, ys,
            color=color,
            linestyle=linestyle,
            marker=marker,
            markersize=markersize
            )

    if add_to_cursors:
        cursor = mplcursors.cursor(point_plot)
        cursor.connect("add", on_add)


def highlight_points(ax, pts,
               color='y',
               linestyle='',
               marker='o',
               markersize=7,
               ):
    '''plot all the points in pts'''
    for pt in pts:
        if len(pt.classes):
            styles = {'color':color, 'linestyle':linestyle, 'marker':marker, 'markersize':markersize}
            for cl in pt.classes:
                if cl in classes:
                    styles.update(classes[cl])
            # collect x, y values into separate arrays
            xs = [pt.x.evalf()]
            ys = [pt.y.evalf()]

            ax.plot(xs, ys, **styles)

def gold_points(ax, pts,
               color='#C90',
               linestyle='',
               marker='o',
               markersize=7,
               ):
    '''plot all the points in pts'''
    for pt in pts:
        styles = {'color':color, 'linestyle':linestyle, 'marker':marker, 'markersize':markersize}
        # collect x, y values into separate arrays
        xs = [pt.x.evalf()]
        ys = [pt.y.evalf()]
        ax.plot(xs, ys, **styles)



def plot_sequence(ax, sequence, bounds):
    seq_pts = [step for step in sequence if isinstance(step, spg.Point2D)]
    seq_polys = [step for step in sequence if isinstance(step, spg.Polygon)]
    seq_segments = [step for step in sequence if isinstance(step, spg.Segment2D)]
    seq_els = [step for step in sequence if isinstance(step, spg.Line2D) or isinstance(step, spg.Circle)]

    highlight_points(ax, seq_pts)
    plot_polygons(ax, seq_polys)
    plot_segments(ax, seq_segments)
    plot_elements(ax, seq_els, bounds)
    plot_points(ax, seq_pts)


def build_sequence(folder, ax, sequence, bounds):
    for i in range(1, len(sequence)+1):
        ax.clear()
        ax.axis(False)
        plot_sequence(ax, sequence[0:i], bounds)
        snapshot(folder, f'{str(i).zfill(3)}.png')


def plot_segment(ax, pt1, pt2, color='#fc09', linestyle='-', linewidth=3, marker='.', markersize=0):
    x1 = pt1.x.evalf()
    x2 = pt2.x.evalf()
    y1 = pt1.y.evalf()
    y2 = pt2.y.evalf()
    styles = {'color':color, 'linestyle':linestyle, 'linewidth':linewidth, 'marker':marker, 'markersize':markersize}
    ax.plot( [x1, x2], [y1, y2], **styles )


def plot_segment2(ax, seg, color='#fc09', linestyle='-', linewidth=4, marker='', markersize=0):
    x1 = seg.points[0].x.evalf()
    x2 = seg.points[1].x.evalf()
    y1 = seg.points[0].y.evalf()
    y2 = seg.points[1].y.evalf()
    styles = {'color':color, 'linestyle':linestyle, 'linewidth':linewidth, 'marker':marker, 'markersize':markersize}
    for cl in seg.classes:
        if cl in classes:
            styles.update(classes[cl])
    if 'edgecolor' in styles:
        styles['color'] = styles['edgecolor']
        styles.pop('edgecolor')
    if 'facecolor' in styles:
        styles.pop('facecolor')
    ax.plot( [x1, x2], [y1, y2], **styles )


def plot_segments(ax, segs):
    for seg in segs:
        plot_segment2(ax, seg)


def plot_polygon(ax, poly, edgecolor='#36c9', facecolor='#36c3', linestyle='-', linewidth=1, fill=True):
    '''takes a sympy Polygon and plots with the matplotlib Polygon patch'''
    if isinstance(poly, spg.Segment2D):
        plot_segment2(ax, poly)
    else:
        xy = [(pt.x.evalf(), pt.y.evalf()) for pt in poly.vertices]
        # print(xy)
        styles = {'facecolor':facecolor, 'edgecolor':edgecolor, 'linestyle':linestyle, 'linewidth':linewidth, 'fill':fill}
        for cl in poly.classes:
            if cl in classes:
                styles.update(classes[cl])
        patch = plt.Polygon(xy, **styles)
        ax.add_patch(patch)


def plot_polygons(ax, poly_array):
    for poly in poly_array:
        plot_polygon(ax, poly)


def plot_wedge(ax, ctr_pt, rad_pt, sweep_pt, color='#0f03', linestyle='', linewidth=6, fill=True):
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
    patch = mp.patches.Wedge(center, rad_val, a1, a2,
                          color=color,
                          linestyle=linestyle,
                          linewidth=linewidth,
                          fill=fill )
    ax.add_patch(patch)

def plot_wedge_2(ax, ctr_pt, rad_val, a1, a2, fc='#0ff1', ec='#0002', linestyle='', linewidth=6, fill=True):
    '''light wrapper for Wegde patch'''
    center = (float(ctr_pt.x.evalf()), float(ctr_pt.y.evalf()))
    patch = mp.patches.Wedge(center, rad_val, a1, a2,
                          fc=fc,
                          ec=ec,
                          linestyle=linestyle,
                          linewidth=linewidth,
                          fill=fill )
    ax.add_patch(patch)


# images**********************
def snapshot(folder, filename):
    import os
    sessions = os.path.expanduser('~') + '/Sessions'
    out = f'{sessions}/{folder}/'
    if not os.path.isdir(out):
        os.mkdir(out)
    plt.savefig(out + filename, dpi=120)
    print(f'snapshot: {out + filename}')


def display(filename):
    from IPython import display
    display.Image(filename)

