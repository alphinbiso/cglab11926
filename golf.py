
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()

# Midpoint Circle Algorithm
def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    points = []

    while x <= y:
        pts = [
            (xc+x, yc+y), (xc-x, yc+y),
            (xc+x, yc-y), (xc-x, yc-y),
            (xc+y, yc+x), (xc-y, yc+x),
            (xc+y, yc-x), (xc-y, yc-x)
        ]

        points += pts

        if p < 0:
            p += 2*x + 3
        else:
            p += 2*(x-y) + 5
            y -= 1

        x += 1

    return points


def update(frame):
    ax.clear()

    # Ground
    ax.plot([0, 100], [10, 10], color="green")

    # Man's head using midpoint circle
    head = midpoint_circle(30, 70, 5)
    ax.scatter([p[0] for p in head],
               [p[1] for p in head], color="black", s=8)

    # Body
    ax.plot([30, 30], [65, 45], color="black")

    # Legs
    ax.plot([30, 20], [45, 10], color="black")
    ax.plot([30, 40], [45, 10], color="black")

    # Arms
    ax.plot([30, 40], [60, 50], color="black")
    ax.plot([30, 45], [60, 45], color="black")

    # Golf club swing
    angle = math.radians(130 - frame*4)

    hand_x = 45
    hand_y = 45
    length = 28

    club_x = hand_x + length * math.cos(angle)
    club_y = hand_y + length * math.sin(angle)

    ax.plot([hand_x, club_x],
            [hand_y, club_y], color="brown", linewidth=3)

    # Golf ball movement after hitting
    if frame < 30:
        ball_x = 65
    else:
        ball_x = 65 + (frame-30)*1.5

    ball = midpoint_circle(ball_x, 12, 2)

    ax.scatter([p[0] for p in ball],
               [p[1] for p in ball], color="white",
               edgecolors="black", s=12)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect("equal")
    ax.axis("off")


ani = animation.FuncAnimation(
    fig,
    update,
    frames=60,
    interval=50,
    repeat=True,
    blit=False
)

plt.show()
