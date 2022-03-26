from geometor.utils import *
from geometor.model import *
from geometor.render import *
from geometor.pappus import *
from itertools import permutations

sp.init_printing()

BUILD = True
ANALYZE = True

GREEN = True
BLUE = True

PART1 = True
PART2 = False
PART3 = True
PART4 = False
if PART1:
    print_log(f'\nPART1')
    if PART2:
        print_log('PART2')
        if PART3:
            print_log('PART3')

NAME = 'star-'
NAME += input(f'\nsession name: {NAME}')
log_init(NAME)
start_time = timer()

print_log(f'\nMODEL: {NAME}')

# add starting points
A, B = begin()
bisector(A, B)

C = pts[5]
D = pts[4]
O = pts[6]

add_element(circle(D, A))
add_element(circle(C, A))

add_element(circle(A, O))
add_element(circle(B, O))


add_element(circle(pts[3], A))
add_element(circle(pts[2], B))


if GREEN:
    add_element(line(pts[11], pts[23], classes=['green']))
if BLUE:
    add_element(line(D, pts[31], classes=['blue']))

if PART1:
    if GREEN:
        add_element(line(pts[16], pts[12], classes=['green']))
        add_element(line(pts[7], pts[24], classes=['green']))
        add_element(line(pts[8], pts[17], classes=['green']))
    if BLUE:
        add_element(line(D, pts[40], classes=['blue']))
        add_element(line(C, pts[30], classes=['blue']))
        add_element(line(C, pts[39], classes=['blue']))


model_summary(NAME, start_time)

# ANALYZE ***************************
if ANALYZE:
    print_log(f'\nANALYZE: {NAME}')
    goldens, groups = analyze_model()

    analyze_summary(NAME, start_time, goldens, groups)

# PLOT *********************************
print_log(f'\nPLOT: {NAME}')
limx, limy = get_limits_from_points(pts, margin=.25)
limx, limy = adjust_lims(limx, limy)
bounds = set_bounds(limx, limy)
print_log()
print_log(f'limx: {limx}')
print_log(f'limy: {limy}')

#  plt.ion()
fig, (ax, ax_btm) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [10, 1]})
ax_btm.axis('off')
ax.axis('off')
ax.set_aspect('equal')
plt.tight_layout()

title = f'G E O M E T O R'
fig.suptitle(title, fontdict={'color': '#960', 'size':'small'})

print_log('\nPlot Summary')
xlabel = f'elements: {len(elements)} | points: {len(pts)}'
ax_prep(ax, ax_btm, bounds, xlabel)
plot_sequence(ax, history, bounds)
snapshot(NAME, '00000.png')

if BUILD:
    print_log('\nPlot Build')
    build_sequence(NAME, ax, ax_btm, history, bounds)

if ANALYZE:
    print_log('\nPlot Goldens')

    bounds = get_bounds_from_sections(goldens)

    plot_sections(NAME, ax, ax_btm, history, goldens, bounds)

    print_log('\nPlot Golden Groups')
    plot_all_groups(NAME, ax, ax_btm, history, groups, bounds)

    plot_all_sections(NAME, ax, ax_btm, history, goldens, bounds)

    complete_summary(NAME, start_time, goldens, groups)

else:
    model_summary(NAME, start_time)



plt.show()

