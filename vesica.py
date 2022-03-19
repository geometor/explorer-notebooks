from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'vesica'
log_init(NAME)
start_time = timer()

begin()
add_element(line(pts[0], pts[1]))
add_element(line(pts[1], pts[0]))

add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))

bl = add_element(line(pts[4], pts[5], classes=['bisector']))

add_element(circle(pts[0], pts[3]))
add_element(circle(pts[1], pts[2]))

print_log(f'Model: {elapsed(start_time)}')
print_log()
print_log(f'    elements: {len(elements)}')
print_log(f'    points: {len(pts)}')

# analysis  *******************************
#  limx, limy = (-2, 2), (-1.5, 1.5)
limx, limy = get_limits_from_points(pts, margin=.25)
bounds = set_bounds(limx, limy)

print_log()
print_log(f'limx: {limx}')
print_log(f'limy: {limy}')

lines = [el for el in elements if isinstance(el, spg.Line2D)]
print_log()
print_log(f'lines: {len(lines)}')

sections = analyze_golden_lines(lines)
print_log()
print_log(f'goldens: {len(sections)}')

groups = group_sections(sections)
print_log()
print_log(f'groups: {len(groups)}')

sorted_groups_keys = sorted(groups.keys(), key=lambda key: float(key.evalf()), reverse=True)

print_log()
print_log(f'Analysis: {elapsed(start_time)}')

# plot *******************
#  plt.ion()
fig, ax = plt.subplots()
ax.set_aspect('equal')
#  limx, limy = (-2, 2), (-1.5, 1.5)
limx, limy = get_limits_from_points(pts, margin=.25)
bounds = set_bounds(limx, limy)

title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

xlabel = f'elements: {len(elements)} | points: {len(pts)}'
ax_prep(ax, bounds, xlabel)
plot_sequence(ax, history, bounds)
snapshot(NAME, 'summary.png')
#  plt.show()

build_sequence(NAME, ax, history, bounds)

plot_sections(NAME, ax, history, sections, bounds)
for i, group in enumerate(sorted_groups_keys):
    i = str(i).zfill(3)
    
    title=f'${sp.latex(group)} \\approx {float(group.evalf())}$'
    plot_group_sections(NAME, ax, history, groups[group], bounds, filename=i, title=title)

plot_all_sections(NAME, ax, history, sections, bounds)

print_log()
print_log(f'Complete: {elapsed(start_time)}')
print_log(f'    elements: {len(elements)}')
print_log(f'    points:   {len(pts)}')
print_log(f'    goldens:  {len(sections)}')
      
plt.show()
