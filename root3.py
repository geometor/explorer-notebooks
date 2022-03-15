from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'root3'
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
limx, limy = (-2, 2), (-1.5, 1.5)
bounds = set_bounds(limx, limy)

title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

ax.axis(False)
plt.tight_layout()

#  build_sequence(NAME, ax, history, bounds)

#  plot_sequence(ax, history, bounds)

lines = [el for el in elements if isinstance(el, spg.Line2D)]
sections = []
for el in lines:
   sections.extend(analyze_golden(el))

for i, section in enumerate(sections):
    print(i, section)
    num = str(i).zfill(3)
    ax.clear()
    ax.axis(False)
    plt.tight_layout()
    section_pts = set()
    for seg in section:
        for pt in seg.points:
            #  pt.classes = ['goldpt']
            section_pts.add(pt)
    gold_points(ax, section_pts)
    plot_sequence(ax, history, bounds)
    plot_segments(ax, section)
    snapshot(f'{NAME}/sections', f'{num}.png')
      
#  plt.show()
