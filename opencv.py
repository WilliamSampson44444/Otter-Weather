# from PIL import Image
# import numpy as np
# import cv2
# import datetime
# from datetime import time
# import time
# mytime = time.localtime()
# if mytime.tm_hour < 6 or mytime.tm_hour > 18:
# cv2.N = cv2.COLORMAP_OCEAN
# image = cv2.imread('road1.jpg', cv2.IMREAD_COLOR)
# image_color = cv2.applyColorMap(image, cv2.N)
# filename = 'road2.jpg'
# status = cv2.imwrite(filename, image_color)
# else:
#     im = Image.open('road.jpg')
#     im = im.save("road3.jpg")

import numpy as np
import cv2

cv2.N = cv2.COLORMAP_OCEAN
image = cv2.imread('road1.jpg', cv2.IMREAD_COLOR)
image_color = cv2.applyColorMap(image, cv2.N)
filename = 'road2.jpg'
status = cv2.imwrite(filename, image_color)