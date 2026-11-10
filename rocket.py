import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Draw rocket with translation (tx, ty)
def rocket(tx, ty):

    # Rocket body
    ax.fill([4+tx, 4+tx, 6+tx, 8+tx, 8+tx],
            [2+ty, 8+ty, 11+ty, 8+ty, 2+ty],
            color="darkgray")

    # Left fin
    ax.fill([4+tx, 2+tx, 4+tx],
            [2+ty, 0+ty, 1+ty],
            color="red")

    # Right fin
    ax.fill([8+tx, 10+tx, 8+tx],
            [2+ty, 0+ty, 1+ty],
            color="red")

    # Window
    ax.fill([5+tx, 7+tx, 7+tx, 5+tx],
            [6+ty, 6+ty, 7+ty, 7+ty],
            color="blue")

    # Flame
    ax.fill([4+tx, 6+tx, 8+tx],
            [1+ty, -2+ty, 1+ty],
            color="orange")


# Animation function
def update(frame):

    ax.clear()

    # Sky background
    fig.patch.set_facecolor("skyblue")
    ax.set_facecolor("skyblue")

    # Dust left behind
    for i in range(frame):
        ax.scatter(6, i-2, color="gray", alpha=0.3)

    # Move rocket upward
    rocket(0, frame)

    # Set display limits
    ax.set_xlim(0, 12)
    ax.set_ylim(-3, 25)
    ax.set_aspect("equal")
    ax.axis("off")


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=20, interval=200
)

plt.show()

