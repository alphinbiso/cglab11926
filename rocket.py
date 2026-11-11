import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax=plt.subplots()

def body(bx,by ):
  ax.fill([4+bx,4+bx,6+bx,8+bx,8+bx], [2,8,11,8,2], color="gray")
  ax.fill([4+bx,2+bx,4+bx], [2,0,1], color="red")
  ax.fill([8+bx,10+bx,8+bx], [2,0,1], color="red")
  ax.fill([5+bx,7+bx,7+bx,5+bx], [6,6,7,7], color="blue")
  ax.fill([4+bx,6+bx,8+bx], [1,-2,1], color="orange")
def update(frame):
  ax.clear()
  body(frame*0.3,0)
  ax.set_xlim(0,12)
  ax.set_ylim(-3,30)
ani = animation.FuncAnimation(
  fig, update, frames=50, interval=100)

plt.show()
