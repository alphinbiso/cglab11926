#DDA ALG EXP1
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    xincr = dx / steps
    yincr = dy / steps

    x_points = []
    y_points = []

    x = x1
    y = y1

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))

        x = x + xincr
        y = y + yincr

    plt.plot(x_points, y_points, color="black")

x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
dda(x1, y1, x2, y2)

plt.grid(True)
plt.axis("equal")
plt.show()


