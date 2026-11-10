# yet to look
import matplotlib.pyplot as plt

xmin,xmax=2,8
ymin,ymax=2,6

x1,y1=1,1
x2,y2=9,7

def code(x,y):
    c=0
    if x<xmin: c= c|1
    if x>xmax: c= c|2
    if y<ymin: c= c|4
    if y>ymax: c= c|8
    return c

c1=code(x1,y1)
c2=code(x2,y2)

while True:
    if c1==0 and c2==0:
        break

    if c1&c2:
        x1=x2
        break

    c=c1 if c1!=0 else c2

    if c&8:
        x=x1+(x2-x1)*(ymax-y1)/(y2-y1)
        y=ymax
    elif c&4:
        x=x1+(x2-x1)*(ymin-y1)/(y2-y1)
        y=ymin
    elif c&2:
        y=y1+(y2-y1)*(xmax-x1)/(x2-x1)
        x=xmax
    else:
        y=y1+(y2-y1)*(xmin-x1)/(x2-x1)
        x=xmin

    if c==c1:
        x1,y1=x,y
        c1=code(x1,y1)
    else:
        x2,y2=x,y
        c2=code(x2,y2)

plt.plot([xmin,xmax,xmax,xmin,xmin],
         [ymin,ymin,ymax,ymax,ymin],'k')

plt.plot([1,9],[1,7],'b--')

if c1==0 and c2==0:
    plt.plot([x1,x2],[y1,y2],'r',linewidth=3)

plt.grid()
plt.axis("equal")
plt.show()