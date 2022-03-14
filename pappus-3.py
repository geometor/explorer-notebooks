from geometor.utils import *
from geometor.model import *
from geometor.render import *

sp.init_printing()
from geometor.pappus import *
from itertools import permutations

#  %matplotlib widget
plt.rcParams['figure.figsize'] = [16, 9]
plt.style.use('dark_background')

#  fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
fig, ax = plt.subplots()
ax.set_aspect('equal')

NAME = 'pappus'

for perm_id in range(6):
    print('PERMUTATION: ', perm_id)
    print()
    pts.clear()
    elements.clear()

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

    #  plt.cla()
    #  fig, ax = plt.subplots()


    # if limx:
    #     plt.gca().set_xlim(limx[0], limx[1])
    # if limy:
    #     plt.gca().set_ylim(limy[0], limy[1])

    ax.clear()
    title = f'G E O M E T O R • pappus • perm: {perm_id}'
    ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
    ax.axis(False)
    plt.tight_layout()

    plot_elements(elements, bounds)

    plot_points(get_pts_by_class('circle'), **classes['circle'], add_to_cursors=False)
    plot_points(get_pts_by_class('square'), **classes['square'], add_to_cursors=False)
    plot_points(get_pts_by_class('diamond'), **classes['diamond'], add_to_cursors=False)
    plot_points(pts)

    filename = f'line-{perm_id}.png'
    snapshot(NAME, filename)


    triangle_sq = polygon(get_pts_by_class('square'))
    if isinstance(triangle_sq, spg.Triangle):
        plot_polygon(triangle_sq, color='#FF03')
        print(f'squares area: {triangle_sq.area}')
    else:
        plot_segment2(triangle_sq, color='#FF09', marker='')

    triangle_cir = polygon(get_pts_by_class('circle'))
    if isinstance(triangle_cir, spg.Triangle):
        plot_polygon(triangle_cir, color='#0FF3')
        print(f'circles area: {triangle_cir.area}')
    else:
        plot_segment2(triangle_cir, color='#0FF9', marker='')

    triangle_dia = polygon(get_pts_by_class('diamond'))
    if isinstance(triangle_dia, spg.Triangle):
        plot_polygon(triangle_dia, color='#F0F3')
        print(f'diamonds area: {triangle_dia.area}')
    else:
        plot_segment2(triangle_dia, color='#F0F9', marker='')

    filename = f'line-{perm_id}-tri.png'
    snapshot(NAME, filename)


    print('points: ', len(pts))
    for pt in pts:
        print(f'{str(pt.x): >8} {str(pt.y): >8} {pt.classes} {[el.coefficients for el in pt.elements]}')
    print('elements: ', len(elements))
    for el in elements:
        print(f'{el.coefficients} {el.classes} ')


plt.show()
