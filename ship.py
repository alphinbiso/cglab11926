import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Draw ship with translation
def ship(tx, ty):

    # Ship body
    ax.fill([2+tx, 8+tx, 7+tx, 3+tx],
            [5+ty, 5+ty, 2+ty, 2+ty],
            color="brown")

    # Cabin
    ax.fill([4+tx, 6+tx, 6+tx, 4+tx],
            [5+ty, 5+ty, 7+ty, 7+ty],
            color="gray")

    # Window
    ax.fill([4.5+tx, 5.5+tx, 5.5+tx, 4.5+tx],
            [5.5+ty, 5.5+ty, 6+ty, 6+ty],
            color="blue")

    # Mast
    ax.plot([5+tx, 5+tx], [7+ty, 9+ty], color="black")

    # Flag
    ax.fill([5+tx, 7+tx, 5+tx],
            [9+ty, 8+ty, 8+ty],
            color="red")


# Animation function
def update(frame):

    ax.clear()

    # White background
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    # Light blue water below ship
    ax.fill([0, 15, 15, 0],
            [0, 0, 2, 2],
            color="lightblue")

    # Move ship horizontally
    ship(frame * 0.2, 0)

    ax.set_xlim(0, 15)
    ax.set_ylim(0, 12)
    ax.set_aspect("equal")
    ax.axis("off")


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=30, interval=200
)

plt.show()

