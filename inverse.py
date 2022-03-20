from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'inverse'
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')

# the number to invert
n = sp.Rational(5,1)

center = point(0, 0, classes=['start'])
add_point(center)

A = point(1, 0, classes=['start'])
add_point(A)

B = point(0, 1, classes=['start'])
add_point(B)

baseline = line(center, A)
add_element(baseline)

unitcircle = circle(center, A)
add_element(unitcircle)

#add vertical
add_element(line(center, B))

N = point(n, 0, classes=['set1pt'])
add_point(N)

L1 = line(B, N, classes=['set1'])
add_element(L1)

add_element(circle(pts[3], pts[6], classes=['green']))
pts[6].classes = ['set2pt']
pts[9].classes = ['set2pt']

num_pts = len(pts)
L2 = line(B, pts[9], classes=['set1'])
add_element(L2)
pts[num_pts].classes = ['set1pt']

chord = line(pts[6], pts[9], classes=['set2'])
add_element(chord)

add_element(circle(B, A, classes=['blue']))

print_log('\nMODEL Summary:')
print_log(f'    elements: {len(elements)}')
print_log(f'    points: {len(pts)}')
print_log(f'\nelapsed: {elapsed(start_time)}')


# # ANALYZE ***************************
# print_log(f'\nANALYZE: {NAME}')
# goldens, groups = analyze_model()
# print_log('\nANALYZE Summary:')
# print_log(f'    goldens: {len(goldens)}')
# print_log(f'    groups: {len(groups)}')
# print_log(f'\nelapsed: {elapsed(start_time)}')


# PLOT *********************************
print_log(f'\nPLOT: {NAME}')
limx, limy = get_limits_from_points(pts, margin=.5)
bounds = set_bounds(limx, limy)
print_log()
print_log(f'limx: {limx}')
print_log(f'limy: {limy}')

#  plt.ion()
fig, ax = plt.subplots()
ax.set_aspect('equal')
#  limx, limy = (-2, 2), (-1.5, 1.5)

title = f'G E O M E T O R'
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

print_log('\nPlot Summary')
xlabel = f'elements: {len(elements)} | points: {len(pts)}'
ax_prep(ax, bounds, xlabel)
plot_sequence(ax, history, bounds)
snapshot(NAME, '00000.png')
#  plt.show()

print_log('\nPlot Build')
build_sequence(NAME, ax, history, bounds)

# print_log('\nPlot Goldens')
# plot_sections(NAME, ax, history, goldens, bounds)

# print_log('\nPlot Golden Groups')
# sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
# for i, group in enumerate(sorted_groups_keys):
#     i = str(i).zfill(3)
    
#     title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
#     plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

# plot_all_sections(NAME, ax, history, goldens, bounds)

print_log(f'\nCOMPLETE: {NAME}')
print_log(f'    elements: {len(elements)}')
print_log(f'    points:   {len(pts)}')
# print_log(f'    goldens:  {len(goldens)}')
print_log(f'\nelapsed: {elapsed(start_time)}')
      
plt.show()
