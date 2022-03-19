from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'star-4'
log_init(NAME)
start_time = timer()

# add starting points
begin()
bisector(pts[0], pts[1])

add_element(circle(pts[4], pts[0]))
add_element(circle(pts[5], pts[0]))

add_element(circle(pts[0], pts[6]))
add_element(circle(pts[1], pts[6]))

add_element(line(pts[11], pts[23], classes=['green']))

add_element(circle(pts[3], pts[0]))
add_element(circle(pts[2], pts[1]))

add_element(line(pts[4], pts[39], classes=['blue']))

add_element(line(pts[4], pts[50], classes=['blue']))

add_element(line(pts[5], pts[38], classes=['blue']))
add_element(line(pts[5], pts[49], classes=['blue']))

add_element(line(pts[16], pts[12], classes=['green']))
add_element(line(pts[7], pts[24], classes=['green']))
add_element(line(pts[8], pts[17], classes=['green']))

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
fig, ax = plt.subplots()
ax.set_aspect('equal')
#  limx, limy = (-2, 2), (-1.5, 1.5)
limx, limy = get_limits_from_points(pts, margin=.25)
bounds = set_bounds(limx, limy)

title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

ax.axis(False)
#  plt.tight_layout()

#  plot_sequence(ax, history, bounds)
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
