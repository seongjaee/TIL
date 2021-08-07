# CSS_Layout_02

## Flexbox

- Flexible Box module Flexbox 인터페이스 내의 아이템 간 "공간배분"과 강력한 "정렬" 기능을 제공하기 위한 1차원 레이아웃 모델
- 요소 간 공간 배분과 정렬 기능을 위한 1차원(단방향) 레이아웃

### 요소와 축

- 요소
  - Flex Container 부모 요소
  - Flex Item 자식 요소
- 축
  - main axis 메인 축
  - cross axis 교차 축
- Flex Container
  - Flexbox 레이아웃 형성하는 가장 기본적인 모델
  - Flex Item들이 놓이는 영역
  - 생성하려면 display 속성을 flex 혹은 inline-flex
- Flex Item
  - 컨테이너의 컨텐츠

### 속성

- 배치 방향 설정
  - flex-direction : 메인 축(main axis)의 방향 설정
- 메인축 방향 정렬
  - justify-content
- 교차축 방향 정렬
  - align-items, align-self, align-content
- 기타
  - flex-wrap, flex-flow, flex-grow, order

#### flex-direction

- main-axis 방향만 바뀜
- row(default) : 왼쪽에서 오른쪽
- row-reverse : 오른쪽에서 왼쪽

- column : 위에서 아래
- column-reverse : 아래에서 위

#### justify & align

- justify : 메인축 관련
- align : 교차축 관련

#### content & items & self

- content : 여러줄
- items : 한 줄
- self : flex item 개별 요소에 작성
- 예시
  - justify-content : 메인축 기준 여러 줄 정렬
  - align-items : 교차축 기준 한 줄 정렬
  - align-self : 교차축 기준 선택한 요소 하나 정렬

#### 정리

- display: flex
  - 정렬하려는 부모 요소에 작성
  - inline-flex : flex 영역을 인라인 블록으로 사용
- flex 선언 시 기본 값들
  - item 은 행으로 나열
  - item 메인축의 시작부터 정렬
  - item은 교차축 크기만큼 늘어남
  - flex-wrap 속성은 nowrap
- flex-wrap : flex item 들이 강제로 한 줄 배치되게 할지, 아니면 가능한 영역내에서 여러 행으로 배치되게 할지 결정
- flex-flow : flex-direction + flex-wrap을 한번에 지정
- order : item들에게 설정. 작을 수록 앞으로 이동
- flew-grow: 메인축의 남은 공간을 항목들에 분배

### 