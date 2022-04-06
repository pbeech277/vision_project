import imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import edge_detect
from utils import to_ndarray

pic = imageio.imread('image-1.bmp')


print('Type of the image : ' , type(pic))

print('Shape of the image : {}'.format(pic.shape))
print('Image Hight {}'.format(pic.shape[0]))
print('Image Width {}'.format(pic.shape[1]))
print('Dimension of Image {}'.format(pic.ndim))

# img = Image.open('image-1.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-1.png')

# img = Image.open('image-2.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-2.png')

# img = Image.open('image-3.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-3.png')

# img = Image.open('image-4.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-4.png')

# img = Image.open('image-5.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-5.png')

# img = Image.open('image-6.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-6.png')

# img = Image.open('image-7.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-7.png')

# img = Image.open('image-8.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-8.png')

# img = Image.open('image-9.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-9.png')

# img = Image.open('image-10.bmp')
# rgb_img = img.convert('RGB')
# rgb_img.save('image-10.png')
img = np.asarray('image-1.png')

pic_edge = edge_detect.ced(img, 1.4, 0, 255)
pic_plot = edge_detect.plot(img)



plt.figure( figsize = (10,10))
plt.imshow(pic_plot)
plt.show()