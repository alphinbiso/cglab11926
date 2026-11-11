
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Midpoint Circle Algorithm
def midpoint_circle(cx, cy, r):
    x, y = 0, r
    p = 1 - r
    points = []

    while x <= y:
        pts = [
            (cx+x, cy+y), (cx-x, cy+y),
            (cx+x, cy-y), (cx-x, cy-y),
            (cx+y, cy+x), (cx-y, cy+x),
            (cx+y, cy-x), (cx-y, cy-x)
        ]
        points.extend(pts)

        if p < 0:
            p += 2*x + 3
        else:
            p += 2*(x-y) + 5
            y -= 1
        x += 1

    points = list(set(points))
    points.sort(key=lambda pt: math.atan2(pt[1]-cy, pt[0]-cx))

    return [p[0] for p in points], [p[1] for p in points]


# Figure setup
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 400)
ax.set_ylim(0, 300)
ax.set_aspect("equal")
ax.grid(True)
ax.set_title("Man Putting Basketball into Net")

# Draw man
ax.plot([70,70], [200,140], 'b', linewidth=4)
ax.plot([70,45], [140,100], 'b', linewidth=4)
ax.plot([70,95], [140,100], 'b', linewidth=4)

# Head using midpoint circle
hx, hy = midpoint_circle(70, 220, 18)
ax.plot(hx, hy, 'b', linewidth=2)

# Arms
ax.plot([70,90], [190,170], 'b', linewidth=4)
arm, = ax.plot([90,110], [170,155], 'b', linewidth=4)

# Basketball hoop
ax.plot([280,330], [195,195], 'r', linewidth=4)
ax.plot([285,295], [195,145], 'k')
ax.plot([325,315], [195,145], 'k')
ax.plot([295,315], [145,145], 'k')

# Net
for i in range(5):
    ax.plot([288+i*8, 298+i*4], [190,155], 'k', linewidth=1)

# Basketball
ball, = ax.plot([], [], color='orange', linewidth=3)
seam1, = ax.plot([], [], color='brown', linewidth=1.5)
seam2, = ax.plot([], [], color='brown', linewidth=1.5)

def update(frame):

    # Ball movement towards basket
    if frame <= 65:
        t = frame / 65
        bx = (1-t)**2 * 110 + 2*(1-t)*t*210 + t**2*305
        by = (1-t)**2 * 155 + 2*(1-t)*t*270 + t**2*195
    else:
        t = (frame-65)/25
        bx = 305
        by = 195 - 45*t

    # Draw ball using midpoint circle
    x, y = midpoint_circle(bx, by, 12)
    ball.set_data(x, y)

    # Basketball seams
    seam1.set_data([bx-8, bx+8], [by-8, by+8])
    seam2.set_data([bx-8, bx+8], [by+8, by-8])

    return ball, seam1, seam2

ani = FuncAnimation(
    fig, update,
    frames=91,
    interval=40,
    blit=False,
    repeat=True
)

plt.show()
