import numpy as np
import cv2

def first(img1, img2, background): #초성, 종성 ex) 가
    #초성,중성,종성 Resize
    initial_img1 = cv2.resize(img1, dsize=(250,300), interpolation = cv2.INTER_AREA) #초성
    final_img2 = cv2.resize(img2, dsize=(150,400), interpolation = cv2.INTER_AREA) #종성


    initial = initial_img1[0:300, 0:250] #합성할 초성 영역 roi 지정
    final = final_img2[0:400, 0:150] #합성할 종성 영역 roi 지정

    background[0:300, 50:300] = initial #배경에 초성 넣기
    background[0:400, 300:450] = final #배경에 종성 넣기

    background_gray = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY) #grayscale
    ret, dst = cv2.threshold(background_gray,170, 255, cv2.THRESH_BINARY_INV) #글자만 추출하기 위해 이진화

    dst = ~dst #색반전으로 글자가 검은색, 배경이 흰색으로 보이게 해줌

    dst = cv2.imshow('font_first',dst) #완성된 이미지 보여주기

    return dst

def second(img1, img2, img3, background): #초성, 중성, 종성 ex) 강
    #초성,중성,종성 Resize
    initial_img1 = cv2.resize(img1, dsize=(250,300), interpolation = cv2.INTER_AREA) #초성
    medial_img2 = cv2.resize(img2, dsize=(150,300), interpolation = cv2.INTER_AREA) #중성
    final_img3 = cv2.resize(img3, dsize=(350,200), interpolation = cv2.INTER_AREA) #종성


    initial = initial_img1[0:300, 0:250] #합성할 초성 영역 roi 지정
    medial = medial_img2[0:300, 0:150] #합성할 중성 영역 roi 지정
    final = final_img3[0:200, 0:350] #합성할 종성 영역 roi 지정

    background[0:300, 50:300] = initial #배경에 초성 넣기
    background[0:300, 300:450] = medial #배경에 중성 넣기
    background[300:500, 100:450] = final #배경에 종성 넣기

    background_gray = cv2.cvtColor(background,cv2.COLOR_RGB2GRAY) #grayscale
    ret, dst = cv2.threshold(background_gray,170, 255, cv2.THRESH_BINARY_INV) #글자만 추출하기 위해 이진화

    dst = ~dst #색반전으로 글자가 검은색, 배경이 흰색으로 보이게 해줌

    dst = cv2.imshow('font_second',dst) #완성된 이미지 보여주기

    return dst


def third(img1, img2, background): #초성, 종성 ex) 고
    #초성,중성,종성 Resize
    initial_img1 = cv2.resize(img1, dsize=(400,300), interpolation = cv2.INTER_AREA) #초성
    final_img2 = cv2.resize(img2, dsize=(350,200), interpolation = cv2.INTER_AREA) #종성


    initial = initial_img1[0:300, 0:400] #합성할 초성 영역 roi 지정
    final = final_img2[0:200, 0:350] #합성할 종성 영역 roi 지정

    background[0:300, 50:450] = initial #배경에 초성 넣기
    background[300:500,100:450] = final #배경에 종성 넣기

    background_gray = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY) #grayscale
    ret, dst = cv2.threshold(background_gray,170, 255, cv2.THRESH_BINARY_INV) #글자만 추출하기 위해 이진화

    dst = ~dst #색반전으로 글자가 검은색, 배경이 흰색으로 보이게 해줌

    dst = cv2.imshow('font_third',dst) #완성된 이미지 보여주기

    return dst

def fourth(img1, img2, img3, background): #초성, 중성, 종성 ex) 곡
    #초성,중성,종성 Resize
    initial_img1 = cv2.resize(img1, dsize=(400,200), interpolation = cv2.INTER_AREA) #초성
    medial_img2 = cv2.resize(img2, dsize=(400,100), interpolation = cv2.INTER_AREA) #중성
    final_img3 = cv2.resize(img3, dsize=(350,200), interpolation = cv2.INTER_AREA) #종성


    initial = initial_img1[0:200, 0:400] #합성할 초성 영역 roi 지정
    medial = medial_img2[0:100, 0:400] #합성할 중성 영역 roi 지정
    final = final_img3[0:200, 0:350] #합성할 종성 영역 roi 지정

    background[0:200, 50:450] = initial #배경에 초성 넣기
    background[200:300, 50:450] = medial #배경에 중성 넣기
    background[300:500, 100:450] = final #배경에 종성 넣기

    background_gray = cv2.cvtColor(background,cv2.COLOR_RGB2GRAY) #grayscale
    ret, dst = cv2.threshold(background_gray,170, 255, cv2.THRESH_BINARY_INV) #글자만 추출하기 위해 이진화

    dst = ~dst #색반전으로 글자가 검은색, 배경이 흰색으로 보이게 해줌

    dst = cv2.imshow('font_fourth',dst) #완성된 이미지 보여주기

    return dst



img1 = cv2.imread('1.jpg') #ㄱ
img2 = cv2.imread('2.jpg') #ㄴ
img3 = cv2.imread('3.jpg') #ㄹ
img4 = cv2.imread('4.jpg') #ㅏ
img5 = cv2.imread('5.jpg') #ㅗ
background = cv2.imread('background.jpg') #하얀색 배경화면

first(img3, img4, background) #라
second(img2, img4, img1, background) #낙
third(img1, img5, background) #고
fourth(img2, img5, img3, background) #놀

cv2.waitkey(0)
cv2.destroyAllWindows()
