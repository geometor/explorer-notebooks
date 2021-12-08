''' general startup for GEOMETOR '''
import sympy as sp
import sympy.plotting as spp
import sympy.geometry as spg
from sympy.abc import x, y

def circle(pt_c, pt_r):
    '''make sympy.geometry.circle from two points'''
    return spg.Circle(pt_c, pt_c.distance(pt_r))

def line(pt_a, pt_b):
    '''make sympy.geometry.Line'''
    return spg.Line(pt_a, pt_b)

def point(x, y):
    '''make sympy.geometry.Point'''
    return spg.Point(x, y)

def plot(element, color='r', title=''):
    return spp.plot_implicit(
        element.equation(),
        aspect_ratio=(1, 1),
        # autoscale=False,
        title=title,
        # legend=True,
        axis=False,
        #  size=(4, 2),
        label=str(element.equation()),
        xlabel='',
        ylabel='',
        # xlim=(-2, 3),
        #  ylim=(-2, 2),
        line_color=color,
        show=False,
        )
