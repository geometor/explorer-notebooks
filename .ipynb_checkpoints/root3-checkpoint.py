# add starting points
begin()

# add baseline
add_element(line(pts[0], pts[1]))

# add unit circles
add_element(circle(pts[0], pts[1]))
add_element(circle(pts[1], pts[0]))
 
add_element(line(pts[0], pts[4]))
add_element(line(pts[0], pts[5]))
add_element(line(pts[1], pts[5]))
add_element(line(pts[1], pts[4]))

limx, limy = (-2, 2), (-1.5, 1.5)
bounds = set_bounds(limx, limy)

plt_init(limx, limy)

# plot_elements(elements,  bounds)
# plot_points(pts)

plot_polygon(polygon_ids([0, 1, 5]))
plot_polygon(polygon_ids([4, 6, 9]))

add_element(line(pts[4], pts[5]))
add_element(line(pts[0], pts[9]))
add_element(line(pts[1], pts[6]))

plot_elements(elements, bounds)
# plot_points(pts)

c = add_element(circle(pts[14], pts[4]))
plot_circle(c, linestyle='-', color='#fc0')
# plot_points(pts)

sg_pts = [pts[i] for i in [18, 0, 1, 19]]
p = polygon_ids([18, 0, 1, 19])

sgs = [segment(sg_pts[i], sg_pts[i+1]) for i in range(len(sg_pts)-1)]

for sg in sgs:
    plot_segment2(sg)
    
plot_points(pts)