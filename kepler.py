from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'kepler'
log_init(NAME)
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

# plot *******************
fig, ax = plt.subplots()
ax.set_aspect('equal')
#  limx, limy = (-2, 2), (-1.5, 1.5)
limx, limy = get_limits_from_points(pts, margin=.25)
bounds = set_bounds(limx, limy)

title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

#  ax.axis(False)
#  plt.tight_layout()


#  plot_sequence(ax, history, bounds)
#  plt.show()
build_sequence(NAME, ax, history, bounds)

lines = [el for el in elements if isinstance(el, spg.Line2D)]
sections = analyze_golden_lines(lines)

plot_all_sections(NAME, ax, history, sections, bounds)
plot_sections(NAME, ax, history, sections, bounds)
      
plt.show()
