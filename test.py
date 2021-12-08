"""
test
"""

#  from sympy import solve, solveset, Rational
#  from sympy import GoldenRatio
#  import matplotlib.pyplot as plt
import sympy as sp
import sympy.geometry as spg
import sympy.plotting as spp

from sympy.abc import x, y

Φ = sp.GoldenRatio
φ = 1 / Φ
print(Φ.expand(func=True))
print(type(Φ))
print(φ.expand(func=True))
print(type(φ))

c = sp.Rational(1, 2)
eq1 = x + y + c
eq2 = x - y + 1
c1 = x**2 + y**2 - x - sp.Rational(3, 4)
c2 = x**2 + (y + sp.Rational(1, 4))**2 + x - sp.Rational(3, 4)
#  PHI = (5**.5 - 1) / 2
#  print(pi/PHI)
#  print(pi.value()/PHI)
#  print(360/PHI)
#  print(eq1 - eq2)
#  root = solveset([c1, c2], (x, y))
root = sp.solve([c1, c2])
print(root)
print(f"root 1 x: {root[0][x]}")
print(f"root 1 y: {root[0][y]}")
#  root = solveset([c1, c2], (x, y))
#  print(root)
#  print(root[0][x])
#  print(root[0][y])
#  print(type(root[0][y]))

a = spg.Point(0, 0)
b = spg.Point(1, 0)
print(a.distance(b))


def circle(pt_c, pt_r):
    '''make sympy.circle from two points'''
    return sp.Circle(pt_c, pt_c.distance(pt_r))


c1 = circle(a, b)
c2 = circle(b, a)

intpoints = c1.intersection(c2)
print(intpoints)
#  intpoints = solve

#  print(dir(c1))
plot1 = spp.plot_implicit(
        c1.equation(),
        #  (y, -2, 2),
        aspect_ratio=(1, 1),
        autoscale=False,
        title='TEST',
        legend=True,
        axis=False,
        #  size=(4, 2),
        label=str(c1.equation()),
        xlabel='',
        ylabel='',
        xlim=(-2, 3),
        #  ylim=(-2, 2),
        line_color='r',
        show=False,
        )
plot2 = spp.plot_implicit(
        c2.equation(),
        legend=True,
        label=str(c2.equation()),
        show=False,
        )
plot1.extend(plot2)

#  dir(plot1)
#  spp.plot_implicit(spg.Point(1, 1), spg.Point(2, 2))
#  spp.plot(intpoints)
#  spp.plot_implicit({ 'x': 1, 'y': 1 })


#  plot2 = plt.scatter([1], [1])
#  plot1.extend(plot2)
plot1.show()
