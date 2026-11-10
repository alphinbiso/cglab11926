
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()

def update(frame):
    ax.clear()


    # Grass across the entire bottom
    ax.axhspan(0, 2, xmin=0, xmax=1, color="green")

    # Sun rises and sets
    x = frame * 0.1
    y = 2 + 4 * math.sin(math.pi * frame / 100)

    # Sun
    sun = plt.Circle((x, y), 0.7, color="orange", zorder=-10)
    ax.add_patch(sun)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

ani = animation.FuncAnimation(
    fig, update, frames=100, interval=100
)

plt.show()

