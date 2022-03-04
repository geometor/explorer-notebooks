'''Helper functions and resources for the Pappus study'''
from geometor.model import *

A = []
B = []


def set_meet(u, v, type):
    '''join pairs of points to find the meet'''
    j1 = add_element( line(A[u], B[v], classes=['red']) )
    j2 = add_element( line(A[v], B[u], classes=['green']) )

    meet = j1.intersection(j2)
    # check if parallel or conicident
    if meet and isinstance(meet[0], spg.Point2D):    
        # find meets from points list
        pt = pts[pts.index(meet[0])]
        pt.classes.append('meet')
        pt.classes.append(type)

