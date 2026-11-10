import matplotlib.pyplot as plt
import numpy as np

# Original triangle
x=[1,2,1.5,1]
y=[1,1,2,1]

# Translation
tx=2
ty=1
xt=[]
yt=[]

for i in range(len(x)):
    xt.append(x[i]+tx)
    yt.append(y[i]+ty)

# Rotation
theta=90
xr=[]
yr=[]

for i in range(len(x)):
    xr.append(x[i]*np.cos(np.radians(theta))-y[i]*np.sin(np.radians(theta)))
    yr.append(x[i]*np.sin(np.radians(theta))+y[i]*np.cos(np.radians(theta)))

# Scaling
sx=2
sy=2
xs=[]
ys=[]

for i in range(len(x)):
    xs.append(x[i]*sx)
    ys.append(y[i]*sy)

# Reflection about X-axis
xf=[]
yf=[]

for i in range(len(x)):
    xf.append(x[i])
    yf.append(-y[i])

# Display all transformations
plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("Original")
plt.grid()

plt.subplot(2,3,2)
plt.plot(xt,yt)
plt.title("Translation")
plt.grid()

plt.subplot(2,3,3)
plt.plot(xr,yr)
plt.title("Rotation")
plt.grid()

plt.subplot(2,3,4)
plt.plot(xs,ys)
plt.title("Scaling")
plt.grid()

plt.subplot(2,3,5)
plt.plot(xf,yf)
plt.title("Reflection")
plt.grid()

plt.show()