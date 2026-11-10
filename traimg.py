#tet to look
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
img=cv2.imread("transformation.jpeg",0)

# Transformations
identity=img
negative=255-img

log=np.uint8(255/np.log(256)*np.log(1+img))

invlog=np.uint8(255*(np.exp(img/255)-1)/(np.e-1))

power=np.uint8(255*(img/255)**2)

root=np.uint8(255*(img/255)**0.5)

# Display
images=[img,identity,negative,log,invlog,power,root]
titles=["Original","Identity","Negative","Log",
        "Inverse Log","Power","Root"]

for i in range(7):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.show()