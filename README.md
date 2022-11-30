# Capstone-Design
<br>

Real-time Customer count app using Mobilenet SSD & OpenCV
<br>

<img width="468" alt="image" src="https://user-images.githubusercontent.com/84511374/204717146-1ab0208c-9d16-4085-8494-996e33605705.png">

### Abstract
<br>
본 프로젝트는 mobilenet-ssd 네트워크와 opencv 딥러닝 모듈을 사용하여 카페에 존재하는 실시간 손님수를 알려주는 시스템이다.
<br>첫째, 카페의 출입문쪽에 카메라를 설치하여, 촬영되는 실시간 영상을 프레임 단위로 나누어 모델에 전송한다. 
<br>둘째, 모델에서는 전송 받은 프레임을 object detection, tracking하여 사람을 검출한다. 
<br>셋째, 들어오고 나가는 사람수를 계산하여 웹을 통해 사용자에게 제공한다. 후에 이를 발전시켜 지난 방문자 수를 제공하여 사용자가 방문하고자 하는 요일을 선택 할 수 있다. 또 다음날 방문자 수를 예측,제공하여 방문 여부를 결정 할 수 있다.

### Motivation
<br>
식당이나 카페를 이용하려고 방문하였는데 사람이 많으면 헛걸음을 하게 된다. 사람이 적은 곳을 선호하면 방문하고자 하는 장소에 전화를 하여 확인 해야하는 번거로움도 있다. 
<br>본 어플리케이션을 이용한다면 사용자는 간편하게 매장 내 인원수를 실시간으로 파악할 수 있고, 업주는 번거로운 과정 없이 사용자에게 정보를 제공할 수 있어 편리하다.

### Development Tools
<br>

- Python
- Flask
- OpenCV
- Visual studio Code

### Contributions
<br>
시간과 장소에 구애받지 않고 실시간으로 가게에 존재하는 손님 수를 알 수 있다.

손님수를 미리 확인한 후 다른 장소에 방문 할 수 있는 선택권이 생긴다.

현재 가게의 사람 수에 대한 문의 전화에서 벗어나 더 좋은 서비스를 제공할 수 있다.

### Implementaion
<br>

- Centroid  Algorithm
    유클리드 거리공식을 이용하여 점의 중심점을 추적하여 두 점간의 유사도를 
    측정하여 id를 부여하는 알고리즘이다. 이 기법으로 구할경우 많은 프레임 속 픽셀의 
    무게중심을 구하는 것이므로 그 오차를 줄여 빠르고 정확한 위치 검출에 유용하다.

- DNN(deep neural network module)
    Dnn 모듈을 사용하기 위하여 딥러닝 프레임워크인 caffe framework에 
    학습된 모델을 불러온다. blobFromImage함수를 이용해서 이미지에서 4차원 blob을 만들고 
    만든 blob을 setInput을 통해 입력받는다. 그후 forward를 이용하여 수행결과를 예측한다.

![image](https://user-images.githubusercontent.com/84511374/204724339-0310fbe7-17e0-4a3c-ac70-dfd180962892.png)

### OverView
<br>

<img width="180" alt="image" src="https://user-images.githubusercontent.com/84511374/204725647-0ccafd00-33da-4610-833c-f048f4d445f5.png" width="40%">
<img width="181" alt="image" src="https://user-images.githubusercontent.com/84511374/204725812-82bceb60-68ff-41a3-ad6d-29d6e21c01b2.png" width="40%">

- 사람이 들어오는 것을 감지
- 검정색 선을 기준으로 사람이 들어온 것이 확인되면 Enter값 0->1로 바뀜
- 사람이 나가는 것을 감지
- 검정색 선을 기준으로 사람이 나가는 것이 확인되면 Exit값 3->4로 바뀜
- result = Enter -Exit

### UI
<br>

<img width="689" alt="image" src="https://user-images.githubusercontent.com/84511374/204726304-476cc955-b8b0-40cf-9856-74a2f57deb1e.png">





