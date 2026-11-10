# yet to look
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig,ax=plt.subplots()

ball=plt.Circle((1,1),0.3,color="red")
ax.add_patch(ball)

ax.set_xlim(0,10)
ax.set_ylim(0,10)

x=1
y=5
vx=0.1
vy=0
g=0.01

def update(frame):
    global x,y,vx,vy

    x=x+vx
    vy=vy-g
    y=y+vy

    if y<=0.3:
        y=0.3
        vy=-vy

    if x>=9.7 or x<=0.3:
        vx=-vx

    ball.center=(x,y)
    return ball,

ani=animation.FuncAnimation(fig,update,interval=20)

plt.show()