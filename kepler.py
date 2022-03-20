from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'kepler'
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')
# add starting points
pt_a = add_point(point(0, 0))
pt_b = add_point(point(1, 0))
#this point should be constructed eventually
pt_c = add_point(point(0, sp.sqrt(phi)))

triangle = add_polygon(polygon([pt_a, pt_b, pt_c]))

bisector(pt_a, pt_b)
bisector(pt_a, pt_c)
bisector(pt_b, pt_c)

# midpoint circle
c = add_element(circle(pts[30], pt_a))

circle = add_element(circle(pt_a, pt_c))
poly_pts = []
poly_pts.append(point(-1, -1))
poly_pts.append(point(-1, 1))
poly_pts.append(point(1, 1))
poly_pts.append(point(1, -1))
square = add_polygon(polygon(poly_pts))

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
sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

plot_all_sections(NAME, ax, history, goldens, bounds)

print_log(f'\nCOMPLETE: {NAME}')
print_log(f'    elements: {len(elements)}')
print_log(f'    points:   {len(pts)}')
print_log(f'    goldens:  {len(goldens)}')
print_log(f'\nelapsed: {elapsed(start_time)}')
      
plt.show()
