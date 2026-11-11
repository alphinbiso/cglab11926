import matplotlib.pyplot as plt
from matplotlib.patches import*
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 5)
ax.set_ylim(0, 10)
ax.set_aspect("equal")

# Pole
ax.fill([2.5,2.5],[0,3],color="black",linewidth=5)

# Traffic light box
box = Rectangle((1.5, 3),2,6, color="black")
ax.add_patch(box)

# Lights
red = Circle((2.5, 7.5), 0.7, color="gray")
yellow = Circle((2.5, 6), 0.7, color="gray")
green = Circle((2.5, 4.5), 0.7, color="gray")

ax.add_patch(red)
ax.add_patch(yellow)
ax.add_patch(green)

def update(frame):

    red.set_color("red" if frame <= 30 else "gray")
    yellow.set_color("yellow" if 30 < frame <= 60 else "gray")
    green.set_color("lime" if 60 <frame <=90 else "gray")

    return red, yellow, green

ani = FuncAnimation(fig, update, frames=90,
                    interval=10)

plt.show()