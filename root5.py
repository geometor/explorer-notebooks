from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root5-3'
log_init(NAME)
# add starting points
start_time = timer()

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

print(f'Build: {elapsed(start_time)}')
logging.info(f'Build: {elapsed(start_time)}')
print()
print(f'elements: {len(elements)}')
logging.info(f'elements: {len(elements)}')
print(f'  points: {len(pts)}')
logging.info(f'  points: {len(pts)}')

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
sections = []
sections = analyze_golden_lines(lines)

print()
print('Golden Sections found:', len(sections))

plot_sections(NAME, ax, history, sections, bounds)

plt.show()
