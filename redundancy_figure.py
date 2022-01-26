import matplotlib.pyplot as plt
import numpy as np
import skimage

np.random.seed(0)
image = skimage.data.astronaut()
plt.imshow(image)
plt.axis('off')
plt.savefig('Figures/intro_figures/astronaut.pdf', dpi=300, bbox_inches='tight')
mask = np.random.uniform(size=image.shape[:2]) > 0.5
masked_image = image * mask[..., None]
plt.imshow(masked_image)
plt.axis('off')
plt.savefig('Figures/intro_figures/astronaut_masked.pdf', dpi=300, bbox_inches='tight')