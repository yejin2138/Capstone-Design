# Capstone-Design
Real-time Customer count app using Mobilenet SSD & OpenCV

<img width="468" alt="image" src="https://user-images.githubusercontent.com/84511374/204717146-1ab0208c-9d16-4085-8494-996e33605705.png">

## Abstract
<br>
본 프로젝트는 mobilenet-ssd 네트워크와 opencv 딥러닝 모듈을 사용하여 카페에 존재하는 실시간 손님수를 알려주는 시스템이다.
<br>첫째, 카페의 출입문쪽에 카메라를 설치하여, 촬영되는 실시간 영상을 프레임 단위로 나누어 모델에 전송한다. 
<br>둘째, 모델에서는 전송 받은 프레임을 object detection, tracking하여 사람을 검출한다. 
<br>셋째, 들어오고 나가는 사람수를 계산하여 웹을 통해 사용자에게 제공한다. 후에 이를 발전시켜 지난 방문자 수를 제공하여 사용자가 방문하고자 하는 요일을 선택 할 수 있다. 또 다음날 방문자 수를 예측,제공하여 방문 여부를 결정 할 수 있다.

## Motivation
<br>
식당이나 카페를 이용하려고 방문하였는데 사람이 많으면 헛걸음을 하게 된다. 사람이 적은 곳을 선호하면 방문하고자 하는 장소에 전화를 하여 확인 해야하는 번거로움도 있다. 
<br>본 어플리케이션을 이용한다면 사용자는 간편하게 매장 내 인원수를 실시간으로 파악할 수 있고, 업주는 번거로운 과정 없이 사용자에게 정보를 제공할 수 있어 편리하다.

##Development Tools
