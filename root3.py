from geometor.utils import *
from geometor.model import *
from geometor.render import *

sp.init_printing()

BUILD = True
ANALYZE = False

PART1 = True
PART2 = True
PART3 = True
PART4 = True
if PART1:
    print_log(f'\nPART1')
    if PART2:
        print_log('PART2')
        if PART3:
            print_log('PART3')
            if PART4:
                print_log('PART4')

NAME = 'root3-'
NAME += input(f'\nsession name: {NAME}')
log_init(NAME)

start_time = timer()

print_log(f'\nMODEL: {NAME}')
# add starting points
A, B = begin()

# add baseline
baseline = add_element(line(A, B))

# add unit circles
add_element(circle(A, B))
add_element(circle(B, A))
 
C = pts[5]
D = pts[4]
#  O = pts[6]

add_polygon(polygon_ids([0, 1, 5]))

add_element(line(A, D))
add_element(line(A, C))
add_element(line(B, C))
add_element(line(B, D))

add_polygon(polygon_ids([4, 6, 9]))

add_element(line(D, C, classes=['bisector']))
add_element(line(A, pts[9], classes=['bisector']))
add_element(line(B, pts[6], classes=['bisector']))
circumcenter = pts[14]

# circumcircle
add_element(circle(circumcenter, D, classes=['gold']))

add_element(circle(C, A))
add_element(line(pts[6], pts[9]))

if PART1:
    nine_ids = [4, 22, 19, 9, 21, 23, 6, 18, 20]
    nine = add_polygon(polygon_ids(nine_ids, classes=['nine']))

    add_element(line(pts[20], pts[22], classes=['red']))
    add_element(line(pts[19], pts[21], classes=['red']))
    add_element(line(pts[23], pts[18], classes=['red']))

    if PART2:
        pt_apex = D
        add_element(line(pt_apex, pts[22], classes=['green']))
        if PART3:
            add_element(line(pt_apex, pts[19], classes=['set1']))
            if PART4:
                add_element(line(pt_apex, pts[21], classes=['set2']))
                add_element(line(pt_apex, pts[23], classes=['set2']))
            add_element(line(pt_apex, pts[18], classes=['set1']))
        add_element(line(pt_apex, pts[20], classes=['green']))

        pt_apex = pts[6]
        add_element(line(pt_apex, pts[18], classes=['green']))
        if PART3:
            add_element(line(pt_apex, pts[20], classes=['set1']))
            if PART4:
                add_element(line(pt_apex, pts[22], classes=['set2']))
                add_element(line(pt_apex, pts[19], classes=['set2']))
            add_element(line(pt_apex, pts[21], classes=['set1']))
        add_element(line(pt_apex, pts[23], classes=['green']))

        pt_apex = pts[9]
        add_element(line(pt_apex, pts[21], classes=['green']))
        if PART3:
            add_element(line(pt_apex, pts[23], classes=['set1']))
            if PART4:
                add_element(line(pt_apex, pts[18], classes=['set2']))
                add_element(line(pt_apex, pts[20], classes=['set2']))
            add_element(line(pt_apex, pts[22], classes=['set1']))
        add_element(line(pt_apex, pts[19], classes=['green']))

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
snapshot(NAME, 'sequences/summary.png')

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

