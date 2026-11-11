import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

fig, ax = plt.subplots()

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect("equal")
ax.set_title("Weight Lifting Animation using DDA")
ax.grid()

# Head
head = Circle((50, 80), 6, color="black")
ax.add_patch(head)

# DDA algorithm
def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return [(round(x1), round(y1))]

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1
    points = []

    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points


# Draw animated lines
line, = ax.plot([], [], "ko", markersize=4)

def update(frame):

    points = []

    # Bar moves up and down
    if frame <= 30:
        bar_y = 50 + frame
    else:
        bar_y = 80 - (frame - 30)

    # Body
    points += dda(50, 75, 50, 45)

    # Legs
    points += dda(50, 45, 38, 15)
    points += dda(50, 45, 62, 15)

    # Arms follow the barbell
    points += dda(50, 68, 40, bar_y)
    points += dda(50, 68, 60, bar_y)

    # Barbell rod
    points += dda(25, bar_y, 75, bar_y)

    # Weights
    points += dda(25, bar_y-8, 25, bar_y+8)
    points += dda(30, bar_y-8, 30, bar_y+8)
    points += dda(70, bar_y-8, 70, bar_y+8)
    points += dda(75, bar_y-8, 75, bar_y+8)

    line.set_data(
        [p[0] for p in points],
        [p[1] for p in points]
    )

    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=60,
    interval=50,
    repeat=True,
    blit=False
)

plt.show()
