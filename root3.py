from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root3-3'
log_init(NAME)
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

# plot *******************
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis(False)
#  plt.tight_layout()

#  limx, limy = (-2, 2), (-1.5, 1.5)
limx, limy = get_limits_from_points(pts, margin=.25)
bounds = set_bounds(limx, limy)

title = f'G E O M E T O R'
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})


build_sequence(NAME, ax, history, bounds)

#  plot_sequence(ax, history, bounds)

lines = [el for el in elements if isinstance(el, spg.Line2D)]
sections = analyze_golden_lines(lines)

plot_sections(NAME, ax, history, sections, bounds)
      
plt.show()
