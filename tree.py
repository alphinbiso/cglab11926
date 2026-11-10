import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.set_facecolor("lightblue")

    # Ground
    ax.fill([0, 10, 10, 0], [0, 0, 2, 2], color="green")

    # Trunk grows and stops at fixed height
    growth = min(frame / 30, 1)
    top = 2 + 4 * growth

    ax.plot([5, 5], [2, top],
            color="brown", linewidth=8)

    # Branches appear after trunk stops growing
    if frame > 30:
        ax.plot([5, 3.5], [4, 5],
                color="brown", linewidth=4)
        ax.plot([5, 6.5], [4, 5],
                color="brown", linewidth=4)

        ax.plot([5, 4], [5, 5.8],
                color="brown", linewidth=3)
        ax.plot([5, 6], [5, 5.8],
                color="brown", linewidth=3)

    # Leaves appear gradually
    if frame > 40:
        leaves = [
            (5, 6.5), (4.5, 6.5), (5.5, 6.5),
            (4, 6.2), (6, 6.2),
            (3.5, 5.2), (6.5, 5.2)
        ]

        for x, y in leaves:
            ax.add_patch(Ellipse(
                (x, y), 1.2, 0.9, color="forestgreen"
            ))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

ani = animation.FuncAnimation(
    fig, update, frames=60, interval=100
)

plt.show()

