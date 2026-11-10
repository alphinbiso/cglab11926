import matplotlib.pyplot as plt
x1=int(input("enter x1"))
y1=int(input("enter y1"))
x2=int(input("enter x2"))
y2=int(input("enter y2"))
dx=x2-x1
dy=y2-y1
ddy=2*dy
dd=ddy-2*dx
p=ddy-dx
x=x1
y=y1
x_points=[]
y_points=[]

while x<=x2:
    x_points.append(x)
    y_points.append(y)
    if p<0:
        p=p+ddy
    else:
        p=p+ddy-dd
        y=y+1
    x=x+1
plt.scatter(x_points,y_points, color="blue")
plt.plot(x_points,y_points,color="red")
plt.axis("equal")
plt.grid(True)
plt.show()

