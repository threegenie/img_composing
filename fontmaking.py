import numpy as np
import cv2

img1 = cv2.imread('initial.jpg') #합성할 초성 
img2 = cv2.imread('medial.jpg') #합성할 중성
img3 = cv2.imread('final.jpg') #합성할 중성
background = cv2.imread('background.jpg') #하얀색 배경화면

#초성,중성,종성 Resize
initial_img1 = cv2.resize(img1, dsize=(300,300), interpolation = cv2.INTER_AREA) #초성
medial_img2 = cv2.resize(img2, dsize=(200,300), interpolation = cv2.INTER_AREA) #중성
final_img3 = cv2.resize(img3, dsize=(300,200), interpolation = cv2.INTER_AREA) #종성


initial = initial_img1[0:300, 0:300] #합성할 초성 영역 roi 지정
medial = medial_img2[0:300, 0:200] #합성할 중성 영역 roi 지정
final = final_img3[0:200, 0:300] #합성할 종성 영역 roi 지정

background[0:300, 0:300] = initial #배경에 초성 넣기
background[0:300, 300:500] = medial #배경에 중성 넣기
background[300:500, 100:400] = final #배경에 종성 넣기

cv2.imshow('font', background) #완성된 이미지 보여주기
cv2.imshow('initial', initial_img1) #초성 이미지 보여주기
cv2.imshow('medial', medial_img2) #중성 이미지 보여주기
cv2.imshow('final', final_img3) #종성 이미지 보여주기

cv2.waitkey(0)
cv2.destroyAllWindows()
