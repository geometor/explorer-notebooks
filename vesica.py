from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'vesica'
log_init(NAME)

begin()
add_element(line(pts[0], pts[1]))
add_element(line(pts[1], pts[0]))

add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))

bl = add_element(line(pts[4], pts[5]))

add_element(circle(pts[0], pts[3]))
add_element(circle(pts[1], pts[2]))

plt.rcParams['figure.figsize'] = [16, 9]

plt.style.use('dark_background')
#  fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
fig, ax = plt.subplots()
ax.set_aspect('equal')

# set up plot
limx, limy = (-3.5, 3.5), (-2.5, 2.5)
bounds = set_bounds(limx, limy)

#  if limx:
    #  ax.set_xlim(limx[0], limx[1])
#  if limy:
    #  ax.set_ylim(limy[0], limy[1])
title = f'G E O M E T O R'
#  ax.set_title(title, fontdict={'color': '#960', 'size':'small'})
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

ax.axis(False)
plt.tight_layout()

plot_elements(elements, bounds)
plot_points(pts)

#  snapshot('vesica/01.png')

print('points: ', len(pts))
for pt in pts:
    print(f'{str(pt.x): >8} {str(pt.y): >8} {pt.classes} {[el.equation() for el in pt.elements]}')
print('elements: ', len(elements))
for el in elements:
    print(f'    {el.equation()} {el.classes} ')
print('history')
for i, step in enumerate(history):
    print(f'    {i} • {step}')
    
print()
print(bl.pts)
print(elements[0].pts)
print(pts[4].elements)

sgs = []
sgs.append(plot_segment(pts[9], pts[5]))
sgs.append(plot_segment(pts[5], pts[4]))
sgs.append(plot_segment(pts[4], pts[8]))

# plot_elements(elements, bounds)
plot_points(pts)
#  snapshot('vesica/02.png')

ratios = []
ratios.append((sgs[0] / sgs[1]).simplify())
ratios.append((sgs[1] / sgs[2]).simplify())
print([ratio - phi for ratio in ratios])

for i in range(1, len(history)+1):
    ax.clear()
    ax.axis(False)
    plot_sequence(history[0:i], bounds)
    snapshot(f'vesica/{str(i).zfill(3)}.png')


plt.show()

