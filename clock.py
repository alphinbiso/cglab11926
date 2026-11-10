import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()

# Draw clock
def clock(frame):

    # Clock face
    circle = plt.Circle((6, 6), 4, color="lightyellow")
    ax.add_patch(circle)

    # Clock border
    circle = plt.Circle((6, 6), 4, fill=False,
                        color="black", linewidth=3)
    ax.add_patch(circle)

    # Clock numbers
    for i in range(1, 13):
        angle = math.radians(i * 30)
        x = 6 + 3.3 * math.sin(angle)
        y = 6 + 3.3 * math.cos(angle)
        ax.text(x, y, str(i), ha="center",
                va="center", fontsize=12)

    # Second hand - fast
    angle1 = math.radians(frame * 6)
    x1 = 6 + 3.2 * math.sin(angle1)
    y1 = 6 + 3.2 * math.cos(angle1)
    ax.plot([6, x1], [6, y1], color="red", linewidth=1)

    # Minute hand - slow
    angle2 = math.radians(frame * 0.1)
    x2 = 6 + 2.7 * math.sin(angle2)
    y2 = 6 + 2.7 * math.cos(angle2)
    ax.plot([6, x2], [6, y2], color="blue", linewidth=3)

    # Hour hand - very slow
    angle3 = math.radians(frame * 0.008)
    x3 = 6 + 1.8 * math.sin(angle3)
    y3 = 6 + 1.8 * math.cos(angle3)
    ax.plot([6, x3], [6, y3], color="black", linewidth=5)

    # Clock center
    ax.scatter(6, 6, color="black", s=30)


# Animation function
def update(frame):

    ax.clear()

    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    clock(frame)

    ax.set_xlim(1, 11)
    ax.set_ylim(1, 11)
    ax.set_aspect("equal")
    ax.axis("off")


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=360, interval=100
)

plt.show()


