from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'star-2'
log_init(NAME)
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

lines = [el for el in elements if isinstance(el, spg.Line2D)]
sections = analyze_golden_lines(lines)

plot_sections(NAME, ax, history, sections, bounds)
      
plt.show()
