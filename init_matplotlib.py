'''setup for matplot lib'''
import matplotlib as mp
import matplotlib.pyplot as mpp


def mpp_init(limx, limy):
    '''configure the MatPlotLib stateful plot engine'''
    mp.style.use('dark_background')
    mpp.figure(num=1, figsize=(6, 4), dpi=120)
    mpp.gca().set_aspect('equal')
    # TODO: pass in limits
    x1, x2 = limx
    mpp.gca().set_xlim(x1, x2)
    y1, y2 = limy
    mpp.gca().set_ylim(y1, y2)
    mpp.gca().set_title('G E O M E T O R', fontdict={'color': '#960'})
    mpp.axis(False)
    mpp.tight_layout()
