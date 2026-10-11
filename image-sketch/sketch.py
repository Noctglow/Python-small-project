from PIL import Image
import numpy as np

array_image = np.asarray(Image.open("input/fcity.jpg").convert('L')).astype('float')

depth = 5
grad = np.gradient(array_image)
grad_x , grad_y = grad[0], grad[1]
grad_x = grad_x * depth / 100
grad_y = grad_y * depth / 100

V = np.sqrt(grad_x**2 + grad_y**2 + 1.0**2)
unit_x = grad_x / V
unit_y = grad_y / V
unit_z = 1.0 / V

depression = np.pi/2.5
azimuth = np.pi/4
dx = np.cos(depression)*np.cos(azimuth)
dy = np.cos(depression)*np.sin(azimuth)
dz = np.sin(depression)

b = 255 * ( dx * unit_x + dy * unit_y + dz * unit_z )
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))
im.save("output/fcityHD.jpg")