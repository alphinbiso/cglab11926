import matplotlib.pyplot as plt
import numpy as np
plt.ion()
a=np.ones((50,50,3))

a[10,10:41]=0
a[40,10:41]=0
a[10:41,10]=0
a[10:41,40]=0

fig,ax=plt.subplots()
img=plt.imshow(a)
plt.axis("off")

def fill(x,y):
    if(0<=x<50 and 0<=y<50 and np.all(a[y,x]==1)):
        a[y,x]=[1,1,0]
        img.set_data(a)
        plt.pause(0.001)

        fill(x+1,y)
        fill(x,y+1)
        fill(x-1,y)
        fill(x,y-1)
fill(11,11)
plt.ioff()
plt.show()

