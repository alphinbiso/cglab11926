import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

fig, ax = plt.subplots()

# Draw fish with translation
def fish(tx, ty):

    # Fish tail
    ax.fill([3+tx, 2.3+tx, 2.3+tx],
            [5+ty, 5.6+ty, 4.4+ty],
            color="orange")

    # Fish body
    body = Ellipse((4+tx, 5+ty), 2, 1.2,
                   color="orange")
    ax.add_patch(body)

    # Top fin
    ax.fill([3.5+tx, 4+tx, 4.5+tx],
            [5.5+ty, 6+ty, 5.5+ty],
            color="darkorange")

    # Bottom fin
    ax.fill([3.5+tx, 4+tx, 4.5+tx],
            [4.5+ty, 4+ty, 4.5+ty],
            color="darkorange")

    # Side fin
    ax.fill([4+tx, 4.7+tx, 4.3+tx],
            [5+ty, 4.6+ty, 5.3+ty],
            color="gold")

    # Fish eye
    ax.scatter(4.7+tx, 5.2+ty, color="black", s=15)


# Animation function
def update(frame):

    ax.clear()

    # White background
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    # Light blue water
    ax.fill([0, 15, 15, 0],
            [0, 0, 10, 10],
            color="lightblue")

    # Move fish horizontally
    fish(frame * 0.1, 0)

    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=80, interval=100
)

plt.show()