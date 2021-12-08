import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
#  %matplotlib inline


x = np.linspace(0, 10)
fig, ax = plt.subplots()

for style in plt.style.available:
    print(style)
plt.style.use('seaborn-dark')

for n in range(-20, 30, 10):
    ax.plot(x, np.cos(x) + np.random.randn(50) + n)

ax.set_title("'seaborn-dark' style")

plt.show()
