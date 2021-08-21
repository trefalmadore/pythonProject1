import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

fig = plt.figure()

plt.grid()
ax = fig.add_subplot(111)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
patch = patches.Rectangle(0,0),0,0)

def init():
    ax.add_patch(patch)
    return patch

def animate(frame):
    patch.set_wight(1)
    patch.set_height(1)
    patch.set_xy(10, 10)
    return patch

def run ():
    pass


anim= animation(fig, animate, frames = 3 , interval=1000)