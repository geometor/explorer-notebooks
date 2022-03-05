'''Helper functions and resources for the Pappus study'''
from geometor.model import *

A = []
B = []

types = ['square', 'circle', 'diamond']


def set_meet(u, v, A, B):
    '''join pairs of points to find the meet'''
    j1 = add_element( line(A[u], B[v], classes=['red']) )
    j2 = add_element( line(A[v], B[u], classes=['green']) )
    join_spread = spread(j1, j2)
    print(f'join {u} {v}')
    print(f'  j1: {j1.coefficients}')
    print(f'  j2: {j2.coefficients}')
    print(f'  spread: {join_spread}')
    meet = j1.intersection(j2)
    # check if parallel or conicident
    if meet and isinstance(meet[0], spg.Point2D):    
        # find meets from points list
        pt = pts[pts.index(meet[0])]
        pt.classes.append('meet')
        type = types[3 - (u + v)]
        pt.classes.append(type)
        print(f'  meet ({pt.x}, {pt.y})')

