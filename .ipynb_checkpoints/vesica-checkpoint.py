from geometor.utils import *
from geometor.model import *
from geometor.render import *

sp.init_printing()
from geometor.pappus import *
from itertools import permutations

%run run.py
%matplotlib widget
log_init('vesica')

begin()
add_element(line(pts[0], pts[1]))
add_element(line(pts[1], pts[0]))

add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))

add_element(line(pts[4], pts[5]))

add_element(circle(pts[0], pts[3]))
add_element(circle(pts[1], pts[2]))

# set up plot
limx, limy = (-3.5, 3.5), (-2.5, 2.5)
bounds = set_bounds(limx, limy)

plt_init(limx, limy)

# title = f'G E O M E T O R • pappus • perm: {perm_id}'
# plt.gca().set_title(title, fontdict={'color': '#960', 'size':'small'})
# plt.axis(False)
# plt.tight_layout()

plot_elements(elements, bounds)
plot_points(pts)

snapshot('vesica-01.png')



plt.show()

print('points: ', len(pts))
for pt in pts:
    print(f'{str(pt.x): >8} {str(pt.y): >8} {pt.classes} {[el.coefficients for el in pt.parents]}')
print('elements: ', len(elements))
for el in elements:
    print(f'{el.coefficients} {el.classes} ')
