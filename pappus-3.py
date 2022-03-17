from geometor.utils import *
from geometor.model import *
from geometor.render import *

sp.init_printing()
from geometor.pappus import *
from itertools import permutations

#  fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
fig, ax = plt.subplots()
ax.set_aspect('equal')

NAME = 'pappus'

for perm_id in range(6):
    print('PERMUTATION: ', perm_id)
    print()
    pts.clear()
    elements.clear()
    history.clear()

    A = []
    A.append( add_point( point(0, 0, classes=['A', 'square']) ) )
    A.append( add_point( point(1, 0, classes=['A', 'circle']) ) )
    line_a = line(A[0], A[1], classes=['blue']) 
    add_element(line_a)
    x_val = 3
    A.append( add_point( point(x_val, 0, classes=['A', 'diamond']) ) )
    line_a.pts.add(A[-1])

    B = []
    B.append( add_point( point(0, 1, classes=['B']) ) )
    B.append( add_point( point(1, 2, classes=['B']) ) )
    line_b = line(B[0], B[1], classes=['blue']) 
    add_element(line_b)
    x_val = 3
    y_val = line_get_y(line_b, x_val)
    B.append( add_point( point(x_val, y_val, classes=['B']) ) )
    line_b.pts.add(B[-1])

    B_perms = list(permutations(B))

    B = B_perms[perm_id]
    # print(B)

    # add pt types based on new permuation order
    print('B points:')
    for i, pt in enumerate(B):
        pt.classes.append(types[i])
        print(i, pt, pt.classes)

    set_meet(0, 1, A, B)
    set_meet(1, 2, A, B)
    set_meet(2, 0, A, B)

    meets = get_pts_by_class('meet')

    if len(meets) >= 2:
        pappus_line = line(meets[0], meets[1], classes=['blue', 'pappus'])
        add_element(pappus_line)
    else:
        print('no pappus line')
    if len(meets) == 3:
        pappus_line.pts.add(meets[2])
        print('collinear: ', sp.Point.is_collinear(*meets))

    limx, limy = get_limits_from_points(pts)
    bounds = set_bounds(limx, limy)

    # if limx:
    #     plt.gca().set_xlim(limx[0], limx[1])
    # if limy:
    #     plt.gca().set_ylim(limy[0], limy[1])

    ax.clear()
    title = f'G E O M E T O R • pappus • perm: {perm_id}'
    ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
    ax.axis(False)
    #  plt.tight_layout()

    triangle_sq = add_polygon(polygon(get_pts_by_class('square'), classes=['yellow']))
    if isinstance(triangle_sq, spg.Triangle):
        print(f'squares area: {triangle_sq.area}')

    triangle_cir = add_polygon(polygon(get_pts_by_class('circle'), classes=['cyan']))
    if isinstance(triangle_cir, spg.Triangle):
        print(f'circles area: {triangle_cir.area}')

    triangle_dia = add_polygon(polygon(get_pts_by_class('diamond'), classes=['magenta']))
    if isinstance(triangle_dia, spg.Triangle):
        print(f'diamonds area: {triangle_dia.area}')


    print('points: ', len(pts))
    for pt in pts:
        print(f'{str(pt.x): >8} {str(pt.y): >8} {pt.classes} {[el.coefficients for el in pt.elements]}')
    print('elements: ', len(elements))
    for el in elements:
        print(f'{el.coefficients} {el.classes} ')

    folder = f'{NAME}/{perm_id}'
    build_sequence(folder, ax, history, bounds)

    #  plot_sequence(ax, history, bounds)
    #  filename = f'line-{perm_id}.png'
    #  snapshot(NAME, filename)

plt.show()
