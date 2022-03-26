from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

NAME = 'subplots'
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')

begin()
add_element(line(pts[0], pts[1]))
add_element(line(pts[1], pts[0]))

add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))

bl = add_element(line(pts[4], pts[5], classes=['bisector']))

add_element(circle(pts[0], pts[3]))
add_element(circle(pts[1], pts[2]))

print_log('\nMODEL Summary:')
print_log(f'    elements: {len(elements)}')
print_log(f'    points: {len(pts)}')
print_log(f'\nelapsed: {elapsed(start_time)}')


#  ANALYZE ***************************
#  print_log(f'\nANALYZE: {NAME}')
#  goldens, groups = analyze_model()
#  print_log('\nANALYZE Summary:')
#  print_log(f'    goldens: {len(goldens)}')
#  print_log(f'    groups: {len(groups)}')
#  print_log(f'\nelapsed: {elapsed(start_time)}')


# PLOT *********************************
print_log(f'\nPLOT: {NAME}')
limx, limy = get_limits_from_points(pts, margin=.25)
limx, limy = adjust_lims(limx, limy)
bounds = set_bounds(limx, limy)
print_log()
print_log(f'limx: {limx}')
print_log(f'limy: {limy}')

fig = plt.figure(1)
#  gs = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[20, 1], left=.05, right=.95, hspace=.05, wspace=.05 )
#  gs = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[.95, .05], left=0, right=1, hspace=0, wspace=0 )
#  ax = fig.add_subplot(gs[0, :])
#  ax_btm = fig.add_subplot(gs[1, :])
gs = fig.add_gridspec(nrows=20, ncols=1, left=0, right=1, hspace=0, wspace=0 )
ax = fig.add_subplot(gs[0:18, :], label='a')
ax2 = fig.add_subplot(gs[0:18, :], label='b')
ax_btm = fig.add_subplot(gs[19, :])
ax.set_aspect('equal')

title = f'G E O M E T O R'
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

print_log('\nPlot Summary')
xlabel = f'elements: {len(elements)} | points: {len(pts)}'
ax_prep(ax, ax_btm, bounds, xlabel)
#  plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.patch.set_facecolor('#FF0')
ax.patch.set_alpha(0)
ax2.patch.set_alpha(0)
plot_sequence(ax, history, bounds)
ax2.plot([0, 10], [0,10])
fig.tight_layout()
snapshot(NAME, '00000.png')
fig.show()

#  print_log('\nPlot Build')
#  build_sequence(NAME, ax, ax_btm, history, bounds)

#  print_log('\nPlot Goldens')
#  plot_sections(NAME, ax, ax_btm, history, goldens, bounds)

#  print_log('\nPlot Golden Groups')
#  plot_all_groups(NAME, ax, ax_btm, history, groups, bounds)

#  plot_all_sections(NAME, ax, ax_btm, history, goldens, bounds)

#  complete_summary(NAME, start_time, goldens, groups)

ax.patch.set_facecolor('#FF0')
plt.show()
