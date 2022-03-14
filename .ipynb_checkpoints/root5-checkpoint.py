from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root5'
log_init(NAME)
# add starting points
start_time = timer()

begin()

# find perps for square
bisector(pts[0], pts[1])
bisector(pts[0], pts[3])
bisector(pts[1], pts[2])

square = unit_square(pts[0])
add_points(square.vertices)
plot_polygon(square, color='#3C03')


# root5 diagonal
# add_element(line(pts[18], pts[31]))
add_element(circle(pts[6], pts[0]))
c = add_element(circle(pts[6], pts[18]))

# outer goldens
el = add_element(circle(pts[0], pts[38]))
el = add_element(circle(pts[1], pts[37]))

# inner goldens
el = add_element(circle(pts[0], pts[37]))
el = add_element(circle(pts[1], pts[38]))

# star diagonals
# el = add_element(line(pts[0], pts[61]))
# el = add_element(line(pts[1], pts[77]))
pentagon = polygon_ids([0, 1, 47, 49, 63])
plot_polygon(pentagon, color='#3C03')

# pentagon = polygon_ids([0, 1, 60, 62, 78])
# plot_polygon(pentagon, color='#3C03')

square = unit_square(pts[0])
add_points(square.vertices)
plot_polygon(square, color='#3C03')

square = unit_square(pts[31])
add_points(square.vertices)
plot_polygon(square, color='#3C03', )

print(f'Build: {elapsed(start_time)}')
print()
print(f'elements: {len(elements)}')
print(f'  points: {len(pts)}')

# plot *******************
fig, ax = plt.subplots()
ax.set_aspect('equal')
limx, limy = (-2, 2), (-1.5, 1.5)
bounds = set_bounds(limx, limy)

title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

ax.axis(False)
plt.tight_layout()

plot_sequence(NAME, ax, history, bounds)

sg_pts = [pts[i] for i in [18, 0, 1, 19]]
p = polygon_ids([18, 0, 1, 19])

sgs = [segment(sg_pts[i], sg_pts[i+1]) for i in range(len(sg_pts)-1)]

#  for sg in sgs:
    #  plot_segment2(sg)

plt.show()
