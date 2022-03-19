from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root5-9'
log_init(NAME)
start_time = timer()

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

# outer goldens
el = add_element(circle(pts[0], pts[54], classes=['gold']))
el = add_element(circle(pts[1], pts[53], classes=['gold']))

pentagon = polygon_ids([0, 1, 62, 64, 81])
add_polygon(pentagon)
pentagon = polygon_ids([0, 1, 63, 65, 82])
add_polygon(pentagon)

# inner goldens
add_element(circle(pts[0], pts[53], classes=['gold']))
add_element(circle(pts[1], pts[54], classes=['gold']))

# diagonals
add_element(line(pts[18], pts[31]))
add_element(line(pts[17], pts[32]))

add_element(circle(pts[6], pts[0]))

add_element(line(pts[157], pts[156]))
add_element(line(pts[104], pts[109]))
add_element(line(pts[53], pts[18]))

add_element(circle(pts[32], pts[157], classes=['gold']))
add_element(circle(pts[32], pts[158], classes=['gold']))

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


plt.show()
