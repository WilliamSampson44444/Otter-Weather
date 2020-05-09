import numpy as np
import cv2
import datetime

x = datetime.datetime.now()

if current_weather >= 5 and current_weather <= 17:
#daytime
    im.show('road.jpg')
elif current_weather >= 21 and current_weather <= 4:
#night
    cv2.N = cv2.COLORMAP_OCEAN
    image = cv2.imread('road.jpg', cv2.IMREAD_COLOR)
    image_color = cv2.applyColorMap(image, cv2.N)

    cv2.imshow("Weather", image_color)
    cv2.waitKey()
elif current_weather >= 17 and current_weather <= 20:
#sunset
    cv2.N = cv2.COLORMAP_HOT
    image = cv2.imread('road.jpg')
    image_color = cv2.applyColorMap(image, cv2.N)


    cv2.imshow("Weather", image_color)
    cv2.waitKey()
