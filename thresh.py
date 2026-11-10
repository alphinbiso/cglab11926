import cv2
import matplotlib.pyplot as plt

img=cv2.imread("transformation.jpeg",0)

T=88

while True:
    # Divide pixels into two groups
    g1=img[img>T]
    g2=img[img<=T]

    # Calculate group averages
    m1=g1.mean()
    m2=g2.mean()

    # Calculate new threshold
    newT=(m1+m2)/2

    if abs(T-newT)<1:
        break

    T=newT

# Apply threshold
_,result=cv2.threshold(img,T,255,cv2.THRESH_BINARY)

plt.subplot(1,2,1)
plt.imshow(img,cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(result,cmap="gray")
plt.title("Iterative Thresholding")
plt.axis("off")

plt.show()

