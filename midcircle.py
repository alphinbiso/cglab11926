import matplotlib.pyplot as plt

xc=int(input("enter center x"))
yc=int(input("enter center y"))
r=int(input("enter radius"))

x=0
y=r
p=1-r

while x<=y:

    plt.scatter(xc+x,yc+y,color="blue")
    plt.scatter(xc-x,yc+y,color="blue")
    plt.scatter(xc+x,yc-y,color="blue")
    plt.scatter(xc-x,yc-y,color="blue")

    plt.scatter(xc+y,yc+x,color="blue")
    plt.scatter(xc-y,yc+x,color="blue")
    plt.scatter(xc+y,yc-x,color="blue")
    plt.scatter(xc-y,yc-x,color="blue")

    if p<0:
        p=p+2*x+3
    else:
        p=p+2*(x-y)+5
        y=y-1

    x=x+1

plt.axis("equal")
plt.grid(True)
plt.show()
