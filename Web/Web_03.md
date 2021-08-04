# Web_03

## CSS Layout

- 웹페이지의 요소들을 어떻게 취합하고 어느 위치에 놓을지 제어
- css layout techniques
  - Display
  - Position
  - Float
  - Flexbox
  - Bootstrap Grid System

### Float

- 한 요소가 정상 흐름으로부터 빠져나와 텍스트 및 인라인 요소가 그 주위를 감싸 요소의 좌, 우측을 따라 배치되게 함

- 본래는 이미지를 한쪽으로 띄우고 텍스트가 둘러싸는 레이아웃

- 여기서 더 나아가 이미지가 아닌 요소들에도 적용 -> 웹사이트 전체 레이아웃

- Float 속성

  - none: 기본값
  - left: 왼쪽으로 띄움
  - right: 오른쪽으로 띄움

- Float clear

  - float에 의해 레이아웃이 망가지는 걸 막아줌

  - ```css
    .clearfix::after {
        content: "";
        display: block;
        clear: both;
    }
    ```

  -  `::after`  : 가상 요소를 만듦

    -  선택한 요소의 맨 마지막에 가상 요소를 생성
    - 보통 content 속성과 함께 요소에 장식용 콘텐츠 추가
    - 기본값은 inline

  -  `clear: both;`

    - 선언으로 float에 영향을 받지 않도록 함
    - clear 속성은 float 및 비 float 요소 모두에 적용됨

- 정리
  - flexbox 및 grid 레이아웃 나오기 전에 열 레이아웃을 만드는데 사용
  - flexbox 및 grid 레이아웃의 출현으로 원래의 float 이미지를 위한 역할로 돌아감
    - MDN에서는 legacy 레이아웃 기술로 분류
  - 웹에 여전히 사용하는 경우도 있음(naver nav 바)

### Flexbox

- Flexible Box module Flexbox 인터페이스 내의 아이템 간 "공간배분"과 강력한 "정렬" 기능을 제공하기 위한 1차원 레이아웃 모델
- 요소 간 공간 배분과 정렬 기능을 위한 1차원(단방향) 레이아웃
- 기억해야할 두 가지 : **요소**와 **축**
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
- 속성
  - 배치 방향 설정
    - flex-direction : 메인 축(main axis)의 방향 설정
  - 메인축 방향 정렬
    - justify-content
  - 교차축 방향 정렬
    - align-items, align-self, align-content
  - 기타
    - flex-wrap, flex-flow, flex-grow, order

- flex-direction

  - main-axis 방향만 바뀜
  - row(default) : 왼쪽에서 오른쪽
  - row-reverse : 오른쪽에서 왼쪽

  - column : 위에서 아래
  - column-reverse : 아래에서 위

- justify & align

  - justify : 메인축
  - align : 교차축

- content & items & self

  - content : 여러줄
  - items : 한 줄
  - self : flex item 개별 요소에 작성
  - 예시
    - justify-content : 메인축 기준 여러 줄 정렬
    - align-items : 교차축 기준 한 줄 정렬
    - align-self : 교차축 기준 선택한 요소 하나 정렬



- 정리
  - display: flex
    - 정렬하려는 부모 요소에 작성
    - inline-flex : flex 영역을 인라인 블록으로 사용
  - flex 선언 시 기본 값들
    - item 은 행으로 나열
    - item 메인축의 시작부터 정렬
    - item은 교차축 크기만큼 늘어남
    - flex-wrap 속성은 nowrap
  - flex-wrap
  - flex-flow : flex-direction + flex-wrap
  - order : 작을 수록 앞으로 이동
  - flew-grow: 메인축의 남은 공간을 항목들에 분배

### Bootstrap

>  The most popular HTML, CSS, and JS library in the world

- 트위터에서 시작된 오픈 소스 프론트엔드 라이브러리
- 웹 페이지에서 많이 쓰이는 요소 거의 전부 내장
- 별도 디자인을 위한 시간이 크게 줄어듬. 여러 브라우저를 지원하기 위한 크로스 브라우징에 불필요한 시간 x
- one source multi use
  - 반응형 웹 디자인
- NETFLIX, VOGUE 사이트가 Bootstrap으로 작성됨.

- CDN

  - Content Delivery(Distribution) Network
  - 컨텐츠를 효율적으로 전달하기 위해, 서버와 사용자 사이의 물리적 거리를 줄여 컨텐츠 로드 지연 최소화

- Class 선택

  - m-1, m-2, m-3, m-4, m-5 : margin 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem

  - mx-0 : x축 margin 0
  - py-0 : y축 padding 0

- Flexbox in Bootstrap
  - `.d-flex`



### Grid system

- Responsive Web Design
  - 다양한 화면 크기를 가진 디바이스들
  - 웹디자인에 대한 접근 방식
- Bootstrap Grid System은 flexbox로 제작됨
- container > rows > column으로 컨텐츠 배치, 정렬
- 12개 column, 6개 grid breakpoints
- row
  - column들의 wrapper
- gutters
  - grid system에서 공간을 확보하고 컨텐츠 정렬하는 column 사이 padding
- breakpoints
  - 다양한 디바이스에 적용하기 위해 특정 px조건에 대한 지점을 정해둠, 이게 breakpoints
  - viewport의 너비가 px 단위이므로 breakpoint에도 px 사용
  - 예시
    - `col-sm-1` : sm 사이즈에서는 이 col은 1칸 차지함
    - `col-md-3` : md 사이즈에서는 3칸 차지함
- col
  - row 당 12개 column
  - 너비는 부모 요소 기준으로 크기가 조정됨
  - 내용은 반드시 column 안에 있어야함
  - column만이 row의 바로 하위 자식
- offset
  - 지정한 만큼 col을 무시하고 다음 공간부터 적용
- nesting
  - row > col > row > col 중첩