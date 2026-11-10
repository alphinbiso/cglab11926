import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
import math

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.set_facecolor("lightblue")
    fig.patch.set_facecolor("lightblue")

    x = frame * 0.1
    y = 5

    flap = math.sin(frame * 0.2)

    # Bird body
    body = Ellipse((x, y), 1.5, 0.7, color="brown")
    ax.add_patch(body)

    # Bird head
    head = Ellipse((x+0.7, y+0.3), 0.6, 0.6, color="brown")
    ax.add_patch(head)

    # Eye
    ax.scatter(x+0.85, y+0.4, color="black", s=15)

    # Beak
    ax.fill([x+1, x+1.4, x+1],
            [y+0.3, y+0.2, y+0.1], color="orange")

    # Tail
    ax.fill([x-0.7, x-1.2, x-0.7],
            [y, y+0.3, y-0.2], color="brown")

    # Wings flapping
    ax.fill([x-0.2, x+0.3, x+0.5],
            [y+0.2, y+1+flap, y+0.2],
            color="saddlebrown")

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")

ani = animation.FuncAnimation(
    fig, update, frames=100, interval=100
)

plt.show()

