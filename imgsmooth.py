import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("transformation.jpeg",0)

gaussian=cv2.GaussianBlur(img,(3,3),0)
average=cv2.blur(img,(3,3))
box=cv2.boxFilter(img,-1,(3,3))
median=cv2.medianBlur(img,3)

kernel=np.ones((3,3),np.uint8)
minimum=cv2.erode(img,kernel)
maximum=cv2.dilate(img,kernel)

bilateral=cv2.bilateralFilter(img,9,75,75)

images=[img,gaussian,average,box,median,minimum,maximum,bilateral]
titles=["Original","Gaussian","Average","Box","Median","Min","Max","Bilateral"]

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],cmap="gray",vmin=0,vmax=255)
    plt.title(titles[i])
    plt.axis("off")

plt.show()