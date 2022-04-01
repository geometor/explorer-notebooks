from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

BUILD = True
ANALYZE = False

GREEN = True
BLUE = True

PART1 = False
PART2 = False
PART3 = True
PART4 = False
if PART1:
    print_log(f'\nPART1')
    if PART2:
        print_log('PART2')
        if PART3:
            print_log('PART3')

NAME = 'wedges-'
NAME += input(f'\nsession name: {NAME}')
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')

# add starting points
A, B = begin_zero()

add_element(circle(A, B))

sweep = 2 * sp.pi - (2 * sp.pi / phi)
print_log(f'sweep: {sweep}')

theta = math.degrees(2 * np.pi - (2 * np.pi / phi))
print_log(f'theta: {theta}')

rays = []

num_rays=144
for i in range(0, num_rays):
    ray = spg.Ray(A, angle=i*sweep)
    print(ray)
    rays.append(ray)
    rad = num_rays - i
    c = circle(A, point(0, rad))
    ints = c.intersection(ray)
    pt = ints[0]
    pt.classes = []
    pt.parents = set()
    pt.elements = set()
    add_point(pt)
    #  plot_wedge_2(ax, A, leafs-i, theta*(i), theta*(i+1), linestyle='-', ec='#000', fc='#c903', linewidth=2)
print('\nRays: ')
print(ray) 
print('\nPoints: ')
print(pts)

model_summary(NAME, start_time)

# ANALYZE ***************************
if ANALYZE:
    print_log(f'\nANALYZE: {NAME}')
    goldens, groups = analyze_model()

    analyze_summary(NAME, start_time, goldens, groups)

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
snapshot(NAME, '00000.png')

#  leafs=3
#  for i in range(0, leafs):
    #  plot_wedge_2(ax, A, leafs-i, theta*(i), theta*(i+1), linestyle='-', ec='#000', fc='#c903', linewidth=2)

if BUILD:
    print_log('\nPlot Build')
    build_sequence(NAME, ax, ax_btm, history, bounds)

if ANALYZE:
    print_log('\nPlot Goldens')

    bounds = get_bounds_from_sections(goldens)

    plot_sections(NAME, ax, ax_btm, history, goldens, bounds)

    print_log('\nPlot Golden Groups')
    plot_all_groups(NAME, ax, ax_btm, history, groups, bounds)

    plot_all_sections(NAME, ax, ax_btm, history, goldens, bounds)

    complete_summary(NAME, start_time, goldens, groups)

else:
    model_summary(NAME, start_time)



plt.show()

