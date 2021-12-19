from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('R-C.jpg'))
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y]=0
plt.figure('R-C')
plt.imshow(img)
plt.axis('off')
plt.show()