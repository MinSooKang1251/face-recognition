# github-facerecogniton
 
 
 
 # 파이썬 AI 얼굴 인식, 이모티콘 합성 기능
 
 <img width="439" alt="111" src="https://user-images.githubusercontent.com/78295968/124686441-1b91ac80-df0e-11eb-896c-51ccf5c27a98.png">

 
 - 주요 기능
 1. 얼굴 인식
 2. 결과 영상에 이모티콘 등 준비한 이미지 입히기
 
 ![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/78295968/124685882-1718c400-df0d-11eb-9efc-c75b34439608.gif)
내 영상을 사용하여 프로그램을 만들었다.


 
 ## 사용 라이브러리
 - open-cv 
 - numpy 
 - dlib
 
 ## oepn-cv
 이미지 처리를 위한 Open-cv
 
- Open Source Computer Vision 의 약자

- 실시간 이미지/영상 처리에 사용하는 오픈 소스 라이브러리 

- Python, C++, Java 와 같은 다양한 개발 환경을 지원

- Windows, Linux, Mac OS, iOS 및 Android같은 다양한 OS를 지원하는 크로스 플랫폼

OpenCV에서 이미지를 읽기 위해서는 imread() 함수를 사용하고, 이미지를 저장하기 위해서는 imwrite() 함수를 사용한다. 또한, 이미지를 화면에 표시하기 위해서는 imshow() 함수를 사용하는데, 이 함수를 사용하면 OpenCV가 새 윈도우 창을 만들고 해당 이미지를 보여준다. 아래 예제는 한 이미지 파일을 읽어 들여 이를 화면에 출력한 후, 다른 파일명으로 이미지를 저장하는 코드이다.



출처: https://devuna.tistory.com/40 [튜나 개발일기]
 
 ## mumpy
 행열 연산 라이브러리 numpy
 
 ## dlib
 이미지 처리 라이브러리 dlib (얼굴인식을 위한)
 
 - 설명
 인턴하고 있는 회사에서 파이썬과 파이썬 내부 라이브러리를 이용하여 인공지능 AI 얼굴인식 기능 개발을 부탁하셨다.
 파이썬을 회사에서 처음 접해보았고 step1으로 빠르게 문법 공부와 인공지능 CS에 대해 공부를 하였다.
 step2로는 step1을 기반으로 웹상에 오픈되어있는 AI 얼굴인식 기능 소스를 토대로 스스로 실습 해보았다.
 이 사이드프로젝트는 step1을 마친 후 들어간 step2이며 유튜브(빵형의 개발도상국)를 통해 공부 후 작성해보았다.
 아직 서투른 실력이기에 코드를 공부하고 구현하는 데에 있어서 엄청난 오류와 삽질이 있었다. 
 정확하게 내가 이해한 바가 맞는지 햇갈리는 단계를 거쳐 결과물이라 할 수 있는 수준의 값을 얻었다.
 
 ## reference
 https://github.com/kairess/face_detector <빵형 깃허브>
 
 https://www.youtube.com/watch?v=tpWVyJqehG4 <유튜브 빵형의 개발도상국>
 
