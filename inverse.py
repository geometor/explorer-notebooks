from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'inverse-'
NAME += input(f'\nsession name: {NAME}')
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')

# the number to invert
n = sp.Rational(3,1)

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

N = point(n, 0, classes=['start', 'set1pt'])
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


# ANALYZE ***************************
print_log(f'\nANALYZE: {NAME}')

harmonics = []
for el in get_elements_lines():
    result  = analyze_harmonics(el)
    #  print(result)
    harmonics.extend(result)
    #  print()

#  print('\n\nharmonics')
#  for i, h in enumerate(harmonics):
    #  print(i)
    #  print(h)


print_log('\nANALYZE Summary:')
print_log(f'    harmonics: {len(harmonics)}')

      
# PLOT *********************************
print_log(f'\nPLOT: {NAME}')
limx, limy = get_limits_from_points(pts, margin=.25)
limx, limy = adjust_lims(limx, limy)
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
snapshot(NAME, 'sequences/summary.png')
#  plt.show()

print_log('\nPlot Build')
build_sequence(NAME, ax, ax_btm, history, bounds)

print_log('\nPlot Harmonic Ranges')
plot_ranges(NAME, ax, ax_btm, history, harmonics, bounds)
plot_all_ranges(NAME, ax, ax_btm, history, harmonics, bounds)

complete_summary(NAME, start_time, goldens, groups)

plt.show()
