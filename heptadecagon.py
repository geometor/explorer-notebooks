'''
this construction is inspried by:
    https://mathpages.com/home/kmath487.htm
'''
from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

BUILD = True
ANALYZE = True

NAME = 'heptadecagon-'
NAME += input(f'\nsession name: {NAME}')
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')

A, B = begin_zero()
AB = add_element(line(A, B))

add_element(circle(A, B))

def bisect_pts(pt1, pt2):
    seg = segment(pt1, pt2)
    ln = seg.perpendicular_bisector()
    ln.classes = ['bisector']
    ln.parents = {pt1, pt2}
    ln.pts = set()
    return ln

def bisect_pts2(pt1, pt2):
    '''use circles but don't add to model'''
    c1 = circle(pt1, pt2)
    c2 = circle(pt2, pt1)
    ints = c1.intersection(c2)
    ln = line(ints[0], ints[1])
    ln.classes = ['bisector']
    ln.parents = {pt1, pt2, ints[0], ints[1]}
    ln.pts = set()
    return ln

def bisect_lines(ln1, ln2):
    lns = ln1.bisectors(ln2)
    for ln in lns:
        ln.classes = ['bisector']
        ln.parents = {ln1.p1, ln1.p2, ln2.p1, ln2.p2}
        ln.pts = set()
    return lns

add_element(bisect_pts2(B, pts[2]))
Pn = pts[-1]
Ps = pts[-2]

add_element(bisect_pts2(B, A))
M = pts[-3]

add_element(bisect_pts2(A, M))
C = pts[-3]
C.classes = ['set1']

CPn = add_element(line(C, Pn))
c1 = add_element(circle(C, A))

add_element(bisect_pts2(A, pts[15]))
add_element(bisect_pts2(A, pts[21]))


#  q = add_element(lns[0])
#  print('\nq:')
#  print(q.equation())
#  print(sp.sqrtdenest(q.equation()))

D = pts[25]
D.classes = ['set1']

l1 = add_element(line(C, D))
l2 = l1.perpendicular_line(C)
l2.classes = ['bisector']
l2.parents = {C, D}
l2.pts = set()
add_element(l2)

add_element(bisect_pts2(pts[27], pts[34]))
add_element(bisect_pts2(Pn, pts[37]))
#  print('\nD:')
#  print(D)
#  print(f'    x: {D.x.simplify()}')
#  print(f'    y: {D.y.simplify()}')
#  print(f'    y: {sp.sqrtdenest(D.y)}')

#  r = q.perpendicular_line(D)
#  r.classes = ['bisector']
#  r.parents = {C, D}
#  r.pts = set()

#  print('\nr:')
#  print(r.equation())
#  print('-')
#  print(sp.sqrtdenest(r.equation()))
#  print('-')
#  print(sp.factor(r.equation()))
#  print('-')
#  print(sp.sqrt(r.equation() ** 2))

#  add_element(r)
#  lns = bisect_lines(q, r)
#  for ln in lns:
    #  print()
    #  print(ln.equation())
    #  print('-')
    #  print(ln.equation().simplify())

#  add_element(lns[0])

model_summary(NAME, start_time)

# ANALYZE ***************************
if ANALYZE:
    print_log(f'\nANALYZE: {NAME}')
    goldens, groups = analyze_model()

    analyze_summary(NAME, start_time, goldens, groups)

# PLOT *********************************
print_log(f'\nPLOT: {NAME}')
limx, limy = get_limits_from_points(pts, margin=.25)
limx, limy = adjust_lims(limx, limy, r=4/3)
bounds = set_bounds(limx, limy)
print_log()
print_log(f'limx: {limx}')
print_log(f'limy: {limy}')

#  plt.ion()
fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
ax_btm.axis('off')
ax.axis('off')
ax.set_aspect('equal')
plt.tight_layout()

title = f'G E O M E T O R'
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

print_log('\nPlot Summary')
xlabel = f'elements: {len(elements)} | points: {len(pts)}'
ax_prep(ax, ax_btm, bounds, xlabel)
plot_sequence(ax, history, bounds)
snapshot(NAME, '00000.png')

if BUILD:
    print_log('\nPlot Build')
    build_sequence(NAME, ax, ax_btm, history, bounds)

if ANALYZE:
    print_log('\nPlot Goldens')
    plot_sections(NAME, ax, ax_btm, history, goldens, bounds)

    print_log('\nPlot Golden Groups')
    plot_all_groups(NAME, ax, ax_btm, history, groups, bounds)

    plot_all_sections(NAME, ax, ax_btm, history, goldens, bounds)

    complete_summary(NAME, start_time, goldens, groups)

else:
    model_summary(NAME, start_time)



plt.show()

