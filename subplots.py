from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'vesica'
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')

begin()
add_element(line(pts[0], pts[1]))
add_element(line(pts[1], pts[0]))

add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))

bl = add_element(line(pts[4], pts[5], classes=['bisector']))

add_element(circle(pts[0], pts[3]))
add_element(circle(pts[1], pts[2]))

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
      
print_log('\nPlot Golden Groups')
print_log('\nPlot Golden Groups')
print_log('\nPlot Golden Groups')
print_log('\nPlot Golden Groups')
print_log('\nPlot Golden Groups')
print_log('\nPlot Golden Groups')
sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

plt.show()
