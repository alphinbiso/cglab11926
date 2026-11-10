import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("img.jpeg",0)

sx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sy=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobelmag=cv2.magnitude(sx,sy)
sobel=np.clip(sobelmag,0,255).astype(np.uint8)

pkerx=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
pkery=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])

px=cv2.filter2D(img,cv2.CV_64F,pkerx)
py=cv2.filter2D(img,cv2.CV_64F,pkery)
prewittmag=cv2.magnitude(px,py)
prewitt=np.clip(prewittmag,0,255).astype(np.uint8)

robkerx=np.array([[1,0],[0,-1]])
robkery=np.array([[0,1],[-1,0]])

rx=cv2.filter2D(img,cv2.CV_64F,robkerx)
ry=cv2.filter2D(img,cv2.CV_64F,robkery)
robmag=cv2.magnitude(rx,ry)
roberts=np.clip(robmag,0,255).astype(np.uint8)

sharpsobel=cv2.add(img,sobel)
sharpprewit=cv2.add(img,prewitt)
sharproberts=cv2.add(img,roberts)

images=[img,sobel,sharpsobel,prewitt,sharpprewit,roberts,sharproberts]
titles=["original","sobel","sharpsobel","prewitt","sharpprewitt","roberts","sharproberts"]

for i in range(7):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],cmap="grey")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()