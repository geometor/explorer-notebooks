from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'kepler'
log_init(NAME)
start_time = timer()

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

title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

#  ax.axis(False)
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
