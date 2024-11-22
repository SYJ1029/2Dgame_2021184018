# 2Dgame_2021184018
< Simple BaseBall >


프로젝트 제목 그대로 간단한 야구 게임을 만들 것입니다.

야구 게임은 기본적으로 야구의 규칙을 따르며, 총 3가지 과정을 가지고 있습니다.

1. 투수는 공을 던지고, 타자는 그 공을 치는 과정
2. 공을 친 이후에 수비과정을 추가로 구현해서, 한 '이닝'을 구현
3. 이닝을 3이닝까지 늘려서 짧은 분량의 야구게임을 완성

![baseball_idea](https://github.com/user-attachments/assets/9d333f5d-bafd-4203-8f67-0e87068e658f)

예전에 피쳐폰/스마트폰 용으로 출시했던 2012프로야구라는 게임입니다.
pc용 게임이 될 것이기에 그에 맞추어서 ui도 바뀔 예정이지만, 이런 상대적으로 간략화된 2d그래픽상으로 구성되는 간다한 야구 게임이 될 것입니다.


# 핵심 메커니즘

- 3차원 공간을 완전한 2차원상의 공간에서 표현하는 방법



# 예상 게임 진행 흐름

![gameflow](https://github.com/user-attachments/assets/3e161676-5f54-4954-af7f-bf5a8ee2b52f)


- 기본적으로 야구의 규칙을 따름
- 위 표는 한 공격권에서 얻은 점수, 총 점수의 합계를 나타낸 표
- 아래의 표는 한번의 공격상황에서 볼, 스트라이크, 아웃의 카운트를 표현


# 개발 내용
- Scene은 총 3개를 구상
1. 이미지들을 로딩하는 Scene
2. 투수가 공을 던지고, 타자가 공을 치는 걸 표현하는 Scene
3. 공을 친 이후를 표현하는 Scene

각 Scene을 구성하는 오브젝트는 다음과 같다.
1-1. 로딩화면을 구성할 배경사진
1-2. 로딩 바

< 2 - layer 1 >
> 배경 클래스
> 투수를 표현하는 Pitcher 클래스
  - 투수의 애니메이션을 정의하고, 공이 생성될 위치를 지정

< 2 - layer 2 >
> 공을 표현할 Ball1 클래스
  - 공의 애니메이션과 공의 움직임을 정의
> 타자를 표현할 Batter 클래스
  - 타자가 배트를 휘두르는 애니메이션을 정의
    -> Bat클래스를 생략함에따라 공과의 충돌체크를 같이 담당

< 3 - layer 1 >
> 경기장을 표현할 배경 클래스

< 3 - layer 2 >
> 세번째 Scene에서의 공을 표현할 Ball2 클래스
  - 수비상황에서 공의 움직을 표현하는 역할
> 수비수를 표현할 Defender 클래스
  - 수비수의 위치와 행동을 결정


- Player 클래스를 부모로 하고, 수비 위치(1루수, 2루수)로 나누어서 세부적인 자식 클래스를 생성
  
- gfw에서 배경을 다루는 스프라이트와 gfw, world 폴더 내 모듈은 전부 다 활용


  < 10/28일 까지 준비할 것 >
- 배경으로 사용할 이미지들을 준비해놓을 것
- git repository애 gfw를 등록할 것.
- 위의 계획에 따라 .gitignore를 업데이트




# 추후 개발 계획 - 2차 발표 이전까지

1주차: 계획했던 세 개의 Scene을 등록하고, 각 Scene끼리의 전환이 이루어지도록 하자

2주차: Scene 2에서 투수와 타자의 애니메이션을 구현, 9명의 타자가 순환하는 구조와 공수교대, 이닝을 구현해서 뼈대를 잡기

3주차: 투수가 공을 던지게 하자. 공을 생성하고 홈플레이트까지 뻗어나갈 수 있게 하며, 변화구도 던지게 해보자

4주차: 공과 타자의 충돌체크를 통해 공을 칠 수 있게 하자

5주차: 수비 구현1: 자신의 범위안으로 오는 공을 한번에 잡아서 out을 만들 수 있게 하기

6주차: 수비 구현2: 수비수들의 송구를 구현해 어느정도 수비를 할 줄 아는 수비수들을 최종적으로 구현하기

6.5주차: 선수 교체 기능과 같은 기타 기능들을 할 수 있다면 구현해서 간단한 야구게임을 완성하기




# 발표 영상 유튜브 링크
1차: https://youtu.be/YhcWDeT6S44

2차: 



# 진행 상황


** 3개의 Scene중에서 이미지를 로딩하는 Scene은 구현하지 않기로 했다.

|주차|commit|
|---|---|
|1주차|3|
|2주차|3|
|3주차|3|
|4주차|12|

![Commitcount](https://github.com/user-attachments/assets/e13364e9-6dc8-4dde-a296-a45593448617)

|주차|진행상황|
|---|----|
|1주차|33%| 
|2주차|10%| 
|3주차|80%| 
|4주차|80%| 

- 1주차 33%: 현재 타자가 공을 치는 Scene만이 구현되어있음
- 2주차 10%: 이미지 리소스를 찾지 못해 애니메이션을 포기했다
- 3주차 80%: 공은 성공적으로 던지지만 변화구를 구현하지 않았음
- 4주차 80%: 충돌체크는 잘 되고 있으나 명확히 시각화 되지 못함


# 구현한 요소
- Pitcher: 투수의 움직임을 구현할 클래스. 이미지 로딩 말고는 따로 담당하는 역할이 없다.
- Batter: 타자의 움직임과 공과의 충돌체크를 구현한 클래스.
- Ball: 공의 움직임과 공의 목표를 설정한 클래스
- 타자의 배트와 공과의 충돌체크


# 구현 예정인 요소
- Defender: 수비수의 이미지와 수비과정을 구현할 클래스
- Denfend.py: 타격 이후의 상황을 보여줄 Scene
- Ball 클래스가 Defend.py에서의 공의 움직임도 같이 담당할 수 있도록 추가
- 마우스 커서를 다른 이미지로 대체
- 스트라이크 존을 나타낼 이미지 렌더링
