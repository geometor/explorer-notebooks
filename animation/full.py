from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.figure()
#  plt.style.use('dark_background')
plt.plot([1, 2], [1, 2])
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
