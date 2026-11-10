import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
import random

fig, ax = plt.subplots()

drops = [[random.uniform(0, 10), random.uniform(2, 10)] for i in range(15)]
splashes = []

def update(frame):
    ax.clear()
    ax.set_facecolor("skyblue")

    # Ground
    ax.fill([0, 10, 10, 0], [0, 0, 1, 1], color="green")

    for drop in drops:
        x, y = drop

        if y > 1:
            rain = Ellipse((x, y), 0.1, 0.3, color="lightblue")
            ax.add_patch(rain)
            drop[1] -= 0.3

        else:
            # Create short splash
            splashes.append([x, 1, 0])
            drop[1] = random.uniform(7, 10)
            drop[0] = random.uniform(0, 10)

    # Draw splash for only 3 frames
    for splash in splashes[:]:
        x, y, age = splash

        ax.plot([x-0.2, x, x+0.2],
                [y, y+0.15, y],
                color="lightblue", linewidth=1.5)

        splash[2] += 1

        if splash[2] >= 3:
            splashes.remove(splash)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

ani = animation.FuncAnimation(
    fig, update, frames=100, interval=100
)

plt.show()

