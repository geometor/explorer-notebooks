from geometor.utils import *
from geometor.model import *
from geometor.render import *

sp.init_printing()
from geometor.pappus import *
from itertools import permutations

NAME = 'vesica'
log_init(NAME)

begin()
add_element(line(pts[0], pts[1]))
add_element(line(pts[1], pts[0]))

add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))

add_element(line(pts[4], pts[5]))

add_element(circle(pts[0], pts[3]))
add_element(circle(pts[1], pts[2]))


plt.style.use('dark_background')
#  fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
fig, ax = plt.subplots()
ax.set_aspect('equal')

# set up plot
limx, limy = (-3.5, 3.5), (-2.5, 2.5)
bounds = set_bounds(limx, limy)

if limx:
    ax.set_xlim(limx[0], limx[1])
if limy:
    ax.set_ylim(limy[0], limy[1])
title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

# plt.axis(False)
ax.axis(False)
plt.tight_layout()

plot_elements(elements, bounds)
plot_points(pts)

snapshot('vesica.py.png')

print('points: ', len(pts))
for pt in pts:
    print(f'{str(pt.x): >8} {str(pt.y): >8} {pt.classes} {[el.equation() for el in pt.parents]}')
print('elements: ', len(elements))
for el in elements:
    print(f'    {el.equation()} {el.classes} ')


plt.show()

