
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from matplotlib.patches import Circle

fig, ax = plt.subplots()

# Rotate and move a point
def move_point(x, y, cx, cy, angle):
    X = x * math.cos(angle) - y * math.sin(angle) + cx
    Y = x * math.sin(angle) + y * math.cos(angle) + cy
    return X, Y

def draw_car(cx, cy, angle):
    # Car body
    body = [(-1.5, 0), (1.5, 0), (1.3, 0.5),
            (0.9, 0.6), (-1, 0.6), (-1.4, 0.4)]

    points = [move_point(x, y, cx, cy, angle) for x, y in body]
    ax.fill(*zip(*points), color="red", zorder=5)

    # Car roof
    roof = [(-0.8, 0.6), (-0.4, 1.1),
            (0.6, 1.1), (1, 0.6)]

    points = [move_point(x, y, cx, cy, angle) for x, y in roof]
    ax.fill(*zip(*points), color="darkred", zorder=6)

    # Windows
    window = [(-0.35, 0.65), (-0.1, 1),
              (0.4, 1), (0.7, 0.65)]

    points = [move_point(x, y, cx, cy, angle) for x, y in window]
    ax.fill(*zip(*points), color="lightblue", zorder=7)

    # Wheels
    for wx in [-0.9, 0.9]:
        x, y = move_point(wx, 0, cx, cy, angle)
        wheel = Circle((x, y), 0.25, color="black", zorder=8)
        ax.add_patch(wheel)

        x, y = move_point(wx, 0, cx, cy, angle)
        ax.scatter(x, y, color="gray", s=20, zorder=9)

    # Headlight
    x, y = move_point(1.45, 0.3, cx, cy, angle)
    ax.scatter(x, y, color="yellow", s=25, zorder=9)

def update(frame):
    ax.clear()
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    # Curved road
    road_x = [i * 0.1 for i in range(150)]
    road_y = [3 + 2 * math.sin(0.4 * x) for x in road_x]

    ax.plot(road_x, road_y, color="gray", linewidth=25, zorder=1)
    ax.plot(road_x, road_y, color="white", linewidth=2, zorder=2)

    # Car position on the white line
    cx = frame * 0.15
    cy = 3 + 2 * math.sin(0.4 * cx)

    # Road direction / car rotation
    slope = 0.8 * math.cos(0.4 * cx)
    angle = math.atan(slope)

    draw_car(cx, cy, angle)

    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

ani = animation.FuncAnimation(
    fig, update, frames=80, interval=100
)

plt.show()

