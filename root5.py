from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root5-diags2'
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

#  add_element(circle(pts[32], pts[157], classes=['gold']))
#  add_element(circle(pts[32], pts[158], classes=['gold']))

print_log('\nMODEL Summary:')
print_log(f'    elements: {len(elements)}')
print_log(f'    points: {len(pts)}')
print_log(f'\nelapsed: {elapsed(start_time)}')


# ANALYZE ***************************
print_log(f'\nANALYZE: {NAME}')
goldens, groups = analyze_model()
print_log('\nANALYZE Summary:')
print_log(f'    goldens: {len(goldens)}')
print_log(f'    groups: {len(groups)}')
print_log(f'\nelapsed: {elapsed(start_time)}')


# PLOT *********************************
print_log(f'\nPLOT: {NAME}')
limx, limy = get_limits_from_points(pts, margin=.25)
limx, limy = adjust_lims(limx, limy)
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

print_log('\nPlot Goldens')
plot_sections(NAME, ax, history, goldens, bounds)

print_log('\nPlot Golden Groups')
plot_all_groups(NAME, ax, history, groups, bounds)

plot_all_sections(NAME, ax, history, goldens, bounds)

print_log(f'\nCOMPLETE: {NAME}')
print_log(f'    elements: {len(elements)}')
print_log(f'    points:   {len(pts)}')
print_log(f'    goldens:  {len(goldens)}')
print_log(f'\nelapsed: {elapsed(start_time)}')
      
plt.show()
