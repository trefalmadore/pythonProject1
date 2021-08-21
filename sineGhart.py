import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0, 5, 0.1)
line, = ax.plot(x, np.sin(x))


def animate(frame):
    line.set_ydata(np.sin(x+ frame / 50))
    return line,


anim = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.grid(True, axis='both')
plt.axhline(y=0, color='k')
plt.show()

def run():
    animate(0)

run()