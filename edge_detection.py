import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

img = Image.open('el_gato.jpg')

gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])

edges = cv2.filter2D(gray, -1, kernel)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(img)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(edges, cmap='gray')
ax[1].set_title('Edge Detected Image')
ax[1].axis('off')

plt.tight_layout()
plt.show()