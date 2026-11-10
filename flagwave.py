import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()

# Draw flag
def flag(frame):

    # Flag pole
    ax.plot([3, 3], [2, 10], color="black", linewidth=4)

    # Red triangular flag waving side to side
    tip = 8 + math.sin(frame) * 1.5

    ax.fill([3, tip, 3],
            [10, 9, 8],
            color="red")


# Animation function
def update(frame):

    ax.clear()

    # White background
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    # Green ground
    ax.fill([-5, 15, 15, -5],
            [0, 0, 2, 2],
            color="green")

    # Draw flag
    flag(frame * 0.2)

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.set_aspect("equal")
    ax.axis("off")


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=50, interval=100
)

plt.show()

