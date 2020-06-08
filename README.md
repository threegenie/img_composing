# Test for composing images to make Korean fonts

- OpenCV Python
- 배경(background) 이미지에 합성하고 싶은 사진을 붙여넣는 방식
- 사진을 resize해서 roi 지정이 편리하도록 함
- 현재는 합성된 파일에 흰색 배경이 보이므로, 추후에 자모음 파일의 contour를 저장해서 붙여넣는 방식으로 수정할 예정

test.py 파일은 합성이 어떻게 되는지 알아보기 위한 테스트 파일

fontmaking.py 파일이 메인 파일

(06.09) fontmaking_binary.py 추가 : 사진 합성 후 글씨의 선만 남겨 폰트의 형태를 갖춤

참고 자료
- https://076923.github.io/posts/Python-opencv-8/ (resize)
- https://m.blog.naver.com/samsjang/220502203203 (roi 영역 지정 및 사진 영역 합성)
- https://keyog.tistory.com/18 (이진화)
