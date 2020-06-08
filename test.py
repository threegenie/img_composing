import numpy as np
import cv2

#배경에 이미지 넣기를 위한 테스트 코드

img = cv2.imread('original.jpg')
background = cv2.imread('background.jpg')

img_resize = cv2.resize(img, dsize=(300,300), interpolation = cv2.INTER_AREA)

img_roi = img_resize[0:100,0:100]

background[0:100,0:100] = img_roi

cv2.imshow('original_font',background)
cv2.imshow('resize_original',img_resize)

cv2.waitkey(0)
cv2.destroyAllWindows()
