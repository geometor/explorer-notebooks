from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root3-full'
log_init(NAME)

start_time = timer()

print_log(f'\nMODEL: {NAME}')
# add starting points
begin()

# add baseline
baseline = add_element(line(pts[0], pts[1]))

# add unit circles
add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))
 
add_polygon(polygon_ids([0, 1, 5]))

add_element(line(pts[0], pts[4]))
add_element(line(pts[0], pts[5]))
add_element(line(pts[1], pts[5]))
add_element(line(pts[1], pts[4]))

add_polygon(polygon_ids([4, 6, 9]))

add_element(line(pts[4], pts[5], classes=['bisector']))
add_element(line(pts[0], pts[9], classes=['bisector']))
add_element(line(pts[1], pts[6], classes=['bisector']))

# circumcircle
add_element(circle(pts[14], pts[4], classes=['gold']))

add_element(circle(pts[5], pts[0]))
add_element(line(pts[6], pts[9]))

nine_ids = [4, 22, 19, 9, 21, 23, 6, 18, 20]
nine = add_polygon(polygon_ids(nine_ids, classes=['nine']))

add_element(line(pts[20], pts[22], classes=['red']))
add_element(line(pts[19], pts[21], classes=['red']))
add_element(line(pts[23], pts[18], classes=['red']))

pt_apex = pts[4]
add_element(line(pt_apex, pts[22], classes=['green']))
add_element(line(pt_apex, pts[19], classes=['set1']))
add_element(line(pt_apex, pts[21], classes=['set2']))
add_element(line(pt_apex, pts[23], classes=['set2']))
add_element(line(pt_apex, pts[18], classes=['set1']))
add_element(line(pt_apex, pts[20], classes=['green']))

pt_apex = pts[6]
add_element(line(pt_apex, pts[18], classes=['green']))
add_element(line(pt_apex, pts[20], classes=['set1']))
add_element(line(pt_apex, pts[22], classes=['set2']))
add_element(line(pt_apex, pts[19], classes=['set2']))
add_element(line(pt_apex, pts[21], classes=['set1']))
add_element(line(pt_apex, pts[23], classes=['green']))

pt_apex = pts[9]
add_element(line(pt_apex, pts[21], classes=['green']))
add_element(line(pt_apex, pts[23], classes=['set1']))
add_element(line(pt_apex, pts[18], classes=['set2']))
add_element(line(pt_apex, pts[20], classes=['set2']))
add_element(line(pt_apex, pts[22], classes=['set1']))
add_element(line(pt_apex, pts[19], classes=['green']))

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
#  limx, limy = (-2, 2), (-1.5, 1.5)
limx, limy = get_limits_from_points(pts, margin=.25)
bounds = set_bounds(limx, limy)
print_log()
print_log(f'limx: {limx}')
print_log(f'limy: {limy}')

#  plt.ion()
fig, ax = plt.subplots()
ax.set_aspect('equal')

title = f'G E O M E T O R'
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

print_log('\nPlot Summary')
xlabel = f'elements: {len(elements)} | points: {len(pts)}'
ax_prep(ax, bounds, xlabel)
plot_sequence(ax, history, bounds)
snapshot(NAME, '00000.png')
#  plt.show()

#  print_log('\nPlot Build')
#  build_sequence(NAME, ax, history, bounds)

#  print_log('\nPlot Goldens')
#  plot_sections(NAME, ax, history, goldens, bounds)

print_log('\nPlot Golden Groups')
sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

#  plot_all_sections(NAME, ax, history, goldens, bounds)

print_log(f'\nCOMPLETE: {NAME}')
print_log(f'    elements: {len(elements)}')
print_log(f'    points:   {len(pts)}')
print_log(f'    goldens:  {len(goldens)}')
print_log(f'\nelapsed: {elapsed(start_time)}')
      
plt.show()
