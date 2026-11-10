import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def circle(cx, cy, r, color):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        points = [
            (x, y), (y, x), (-x, y), (-y, x),
            (-x, -y), (-y, -x), (x, -y), (y, -x)
        ]

        for px, py in points:
            ax.plot(cx + px, cy + py, ".", color=color, markersize=1)

        x += 1

        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

# Larger circles for smoother appearance
circle(125, 125, 100, "blue")
circle(125, 125, 50, "red")

ax.set_xlim(0, 250)
ax.set_ylim(0, 250)
ax.set_aspect("equal")
plt.show()

