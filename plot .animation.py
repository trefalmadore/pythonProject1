import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = [0,2,4,6,8,10]
y = [20,16,15,0,8,100]

fig, ax = plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
def animate(frame):
    ax.step(x, y, "x")
    plt.show()

def run():
    #global fig,
    animate(0)

anim = animation.FuncAnimation(fig,animate , frames = 10 , interval = 1000)

run()