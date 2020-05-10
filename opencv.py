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
from datetime import datetime

def background_filter(weather_type):
    now = datetime.now()
    image = cv2.imread('static/Images/road1.jpg', cv2.IMREAD_COLOR)

    if((weather_type == "clouds") or ("rain" in weather_type) or (now.hour > 20 or now.hour < 5)):
        image = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
    elif(("snow" in weather_type) or ("hail" in weather_type)):
        image = cv2.applyColorMap(image, cv2.COLORMAP_WINTER)
    elif("fog" in weather_type):
        image = cv2.applyColorMap(image, cv2.COLORMAP_BONE)

    status = cv2.imwrite('static/Images/road2.jpg', image)


#background_filter("asdfasdfasdf")