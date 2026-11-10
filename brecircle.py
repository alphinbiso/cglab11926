import matplotlib.pyplot as plt

xc=int(input("enter center x"))
yc=int(input("enter center y"))
r=int(input("enter radius"))

x=0
y=r
p=3-2*r

while x<=y:

    plt.plot(xc+x,yc+y,color="blue")
    plt.plot(xc-x,yc+y,color="blue")
    plt.plot(xc+x,yc-y,color="blue")
    plt.plot(xc-x,yc-y,color="blue")

    plt.plot(xc+y,yc+x,color="blue")
    plt.plot(xc-y,yc+x,color="blue")
    plt.plot(xc+y,yc-x,color="blue")
    plt.plot(xc-y,yc-x,color="blue")

    if p<0:
        p=p+4*x+6
    else:
        p=p+4*(x-y)+10
        y=y-1

    x=x+1

plt.axis("equal")
plt.grid(True)
plt.show()
