
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.set_facecolor("white")

    cx, cy = 5, 5

    # Fan outer grill
    ax.add_patch(plt.Circle((cx, cy), 3, fill=False, color="gray", linewidth=3))

    # Rotating blades
    for i in range(3):
        angle = math.radians(frame * 5 + i * 120)

        x1 = cx + 0.3 * math.cos(angle)
        y1 = cy + 0.3 * math.sin(angle)

        x2 = cx + 2.5 * math.cos(angle + 0.3)
        y2 = cy + 2.5 * math.sin(angle + 0.3)

        x3 = cx + 2.5 * math.cos(angle - 0.3)
        y3 = cy + 2.5 * math.sin(angle - 0.3)

        ax.fill([cx, x2, x3], [cy, y2, y3], color="lightblue")

    # Center cap
    ax.add_patch(plt.Circle((cx, cy), 0.4, color="black"))

    # Fan stand
    ax.plot([5, 5], [2, 0.5], color="gray", linewidth=8)
    ax.plot([4, 6], [0.5, 0.5], color="black", linewidth=6)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

ani = animation.FuncAnimation(
    fig, update, frames=360, interval=50
)

plt.show()
