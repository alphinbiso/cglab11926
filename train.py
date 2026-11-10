
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from matplotlib.patches import Circle

fig, ax = plt.subplots()

def move_point(x, y, cx, cy, angle):
    X = x * math.cos(angle) - y * math.sin(angle) + cx
    Y = x * math.sin(angle) + y * math.cos(angle) + cy
    return X, Y

def draw_shape(points, cx, cy, angle, color):
    points = [move_point(x, y, cx, cy, angle) for x, y in points]
    ax.fill(*zip(*points), color=color, zorder=5)

def draw_coach(cx, cy, angle, color):
    # Coach body
    draw_shape(
        [(-0.9, 0.3), (0.9, 0.3), (0.9, 1.5), (-0.9, 1.5)],
        cx, cy, angle, color
    )

    # Windows
    for wx in [-0.5, 0.2]:
        draw_shape(
            [(wx, 0.9), (wx+0.4, 0.9),
             (wx+0.4, 1.3), (wx, 1.3)],
            cx, cy, angle, "lightblue"
        )

    # Wheels
    for wx in [-0.6, 0.6]:
        x, y = move_point(wx, 0.25, cx, cy, angle)
        ax.add_patch(Circle((x, y), 0.22, color="black", zorder=6))

def draw_train(cx, cy, angle):
    # Engine
    draw_shape(
        [(-1, 0.3), (1.5, 0.3), (1.5, 1.8), (-1, 1.8)],
        cx, cy, angle, "brown"
    )

    # Engine front
    draw_shape(
        [(1.5, 0.3), (2, 0.3), (2, 1.2), (1.5, 1.8)],
        cx, cy, angle, "orange"
    )

    # Engine window
    draw_shape(
        [(0.5, 1.1), (1.2, 1.1), (1.2, 1.6), (0.5, 1.6)],
        cx, cy, angle, "lightblue"
    )

    # Engine wheels
    for wx in [-0.6, 0.8]:
        x, y = move_point(wx, 0.25, cx, cy, angle)
        ax.add_patch(Circle((x, y), 0.25, color="black", zorder=6))

def update(frame):
    ax.clear()
    ax.set_facecolor("white")

    # Curved railway
    track_x = [i * 0.1 for i in range(150)]
    track_y = [3 + 2 * math.sin(0.4 * x) for x in track_x]

    ax.plot(track_x, track_y, color="brown", linewidth=10, zorder=1)

    # Rails
    for offset in [-0.25, 0.25]:
        rx, ry = [], []

        for x, y in zip(track_x, track_y):
            angle = math.atan(0.8 * math.cos(0.4 * x))
            rx.append(x - offset * math.sin(angle))
            ry.append(y + offset * math.cos(angle))

        ax.plot(rx, ry, color="black", linewidth=2, zorder=2)

    # Sleepers
    for x in track_x[::8]:
        y = 3 + 2 * math.sin(0.4 * x)
        angle = math.atan(0.8 * math.cos(0.4 * x))

        p1 = move_point(0, -0.6, x, y, angle)
        p2 = move_point(0, 0.6, x, y, angle)

        ax.plot([p1[0], p2[0]], [p1[1], p2[1]],
                color="brown", linewidth=3, zorder=2)

    # Engine follows track
    x = frame * 0.15
    y = 3 + 2 * math.sin(0.4 * x)
    angle = math.atan(0.8 * math.cos(0.4 * x))

    draw_train(x, y, angle)

    # Coaches follow track at separate positions
    for i in range(3):
        cx = x - (i + 1) * 2.2
        cy = 3 + 2 * math.sin(0.4 * cx)
        coach_angle = math.atan(0.8 * math.cos(0.4 * cx))

        draw_coach(cx, cy, coach_angle, "brown")

    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

ani = animation.FuncAnimation(
    fig, update, frames=80, interval=100
)

plt.show()

