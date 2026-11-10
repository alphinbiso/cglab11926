import cv2
import matplotlib.pyplot as plt

img=cv2.imread("transformation.jpeg",0)

# Contrast stretching
cs=cv2.normalize(img,None,0,255,cv2.NORM_MINMAX)

# Histogram equalization
he=cv2.equalizeHist(img)

images=[img,cs,he]
titles=["Original","Contrast Stretching","Histogram Equalization"]

plt.figure(figsize=(10,6))

# Display images
for i in range(3):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

# Display histograms
for i in range(3):
    plt.subplot(2,3,i+4)
    plt.hist(images[i].ravel(),256,[0,256])
    plt.title(titles[i]+" Histogram")

plt.tight_layout()
plt.show()