from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root5-'
NAME += input(f'\nsession name: {NAME}')
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')
# add starting points
begin()

# find perps for square
bisector(pts[0], pts[1])
bisector(pts[0], pts[3])
bisector(pts[1], pts[2])

# squares
add_element(line(pts[18], pts[32]))
add_element(line(pts[17], pts[31]))
add_polygon(polygon_ids([0, 1, 18, 32]))
add_polygon(polygon_ids([0, 1, 17, 31]))

# golden circle
c = add_element(circle(pts[6], pts[18], classes=['gold']))
goA = pts[53]
goB = pts[54]

# outer goldens
el = add_element(circle(pts[0], goB, classes=['gold']))
el = add_element(circle(pts[1], goA, classes=['gold']))

pentagon = polygon_ids([0, 1, 62, 64, 81])
add_polygon(pentagon)
pentagon = polygon_ids([0, 1, 63, 65, 82])
add_polygon(pentagon)

# inner goldens
add_element(circle(pts[0], goA, classes=['gold']))
add_element(circle(pts[1], goB, classes=['gold']))

# diagonals
add_element(line(pts[18], pts[31], classes=['green']))
add_element(line(pts[17], pts[32], classes=['green']))

add_element(line(pts[18], goA, classes=['set1']))
add_element(line(pts[17], goA, classes=['set1']))

add_element(line(pts[18], goB, classes=['set2']))
add_element(line(pts[17], goB, classes=['set2']))

add_element(line(pts[31], goA, classes=['set2']))
add_element(line(pts[32], goA, classes=['set2']))

add_element(line(pts[31], goB, classes=['set1']))
add_element(line(pts[32], goB, classes=['set1']))

# half unit circle
add_element(circle(pts[6], pts[0]))

# cross
add_element(line(pts[293], pts[292]))
add_element(line(pts[293], pts[291]))

add_element(line(pts[294], pts[292]))
add_element(line(pts[294], pts[291]))


model_summary(NAME, start_time)

# ANALYZE ***************************
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
#  plt.show()

print_log('\nPlot Build')
build_sequence(NAME, ax, ax_btm, history, bounds)

print_log('\nPlot Goldens')
plot_sections(NAME, ax, ax_btm, history, goldens, bounds)

print_log('\nPlot Golden Groups')
plot_all_groups(NAME, ax, ax_btm, history, groups, bounds)

plot_all_sections(NAME, ax, ax_btm, history, goldens, bounds)

complete_summary(NAME, start_time, goldens, groups)


plt.show()
