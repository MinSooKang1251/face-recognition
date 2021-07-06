import cv2, dlib, sys
import numpy as np
#스케일러를 통해 비디오 크기를 줄여준다.
scaler = 0.4

detector = dlib.get_frontal_face_detector()
#d아래의 shape머시기는 머신러닝으로 학습된 파일임. 구글링해서 다운 받았음.
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#캡 함수로 비디오 링크를 넣는다.
cap = cv2.VideoCapture('girl.mp4')

#load overlay image
overlay = cv2.imread('peach.png', cv2.IMREAD_UNCHANGED)

# overlay function 이미지를 입히는 이 함수는 어려움. 소스코드 구글링해서 따옴
def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
  bg_img = background_img.copy()
  # convert 3 channels to 4 channels
  if bg_img.shape[2] == 3:
    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2BGRA)

  if overlay_size is not None:
    img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

  b, g, r, a = cv2.split(img_to_overlay_t)

  mask = cv2.medianBlur(a, 5)

  h, w, _ = img_to_overlay_t.shape
  roi = bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)]

  img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
  img2_fg = cv2.bitwise_and(img_to_overlay_t, img_to_overlay_t, mask=mask)

  bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)] = cv2.add(img1_bg, img2_fg)

  # convert 4 channels to 4 channels
  bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGRA2BGR)

  return bg_img

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    ori = img.copy()

    #detect faces
    faces = detector(img)
    face = faces[0]

    #얼굴 특이점을 추출하기 위해 프레딕터 사용
    dlib_shape = predictor(img, face)
    #연산을 쉽게하기위해 numpy사용 그리고 shape_2d함수에 넣는다.
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])

    #compute center of face
    #numpy의 min, max함수를 이용하여 좌상단 우하단의 점을 구해준다
    top_left = np.min(shape_2d, axis=0)
    bottom_right = np.max(shape_2d, axis=0)
    
    #크기가 작으면 뒤에 * 1.8 등 숫자를 곱해서 키울 수있다. 소수점 있는 것을 곱하기 때문에 max앞에 int 사용
    face_size = int(max(bottom_right - top_left) * 1.3)  

    #얼굴의 중심을 구할 것이다. 모든 특징점의 평균을 구해 중심을 구한다.
    #평균이 소수점일 수 있어서 int로 설정한다.
    center_x, center_y = np.mean(shape_2d, axis=0).astype(np.int)

    result = overlay_transparent(ori, overlay, center_x -10, center_y  -25, overlay_size=(face_size, face_size))

    #visualize
    img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()), color=(255, 255, 255),
    thickness=2, lineType=cv2.LINE_AA)
    
    #for문을 돌면서 68개의 점이 그려진다
    for s in shape_2d:
        cv2.circle(img, center=tuple(s), radius=1, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
    
    
    #구한 좌상단, 우하단의 점을 이미지로 구한다. 서클 함수를 이용한다. 특징점을 구분하기 위해 파란색으로 한다.
    cv2.circle(img, center=tuple(top_left), radius=1, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple(bottom_right), radius=1, color=(255,0,0), thickness=2, lineType=cv2.LINE_AA)

    cv2.circle(img, center=tuple((center_x, center_y)), radius=1, color=(0,0,255), thickness=2, lineType=cv2.LINE_AA)
    
    #Imshow함수로 화면 출력. 앞에는 출력 타이틀 이름 뒤에는 imread의 리턴 값
    cv2.imshow('img', img)
    #위에 overlay함수를 리절트에 저장했고 그 저장한 리절트를 보여준다.
    cv2.imshow('result', result)
    cv2.waitKey(1)