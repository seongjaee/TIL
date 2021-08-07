# CSS_Layout_03

## Bootstrap layout

### Bootstrap이란?

>  The most popular HTML, CSS, and JS library in the world
>
>  [https://getbootstrap.com/](https://getbootstrap.com/)

- 트위터에서 시작된 오픈 소스 프론트엔드 라이브러리
- 웹 페이지에서 많이 쓰이는 요소 거의 전부 내장
- Bootstrap을 이용하면 별도 디자인을 위한 시간이 크게 감소
- 여러 브라우저를 지원하기 위한 크로스 브라우징에 불필요한 시간을 단축시킴
- one source multi use
  - 반응형 웹 디자인
- NETFLIX, VOGUE 사이트가 Bootstrap으로 작성됨.
- - 

### Bootstrap 사용

- CDN
  - Content Delivery(Distribution) Network
  - 컨텐츠를 효율적으로 전달하기 위해, 서버와 사용자 사이의 물리적 거리를 줄여 컨텐츠 로드 지연 최소화
  - [https://getbootstrap.com/docs/5.1/getting-started/introduction/#quick-start](https://getbootstrap.com/docs/5.1/getting-started/introduction/#quick-start) 에서 주소를 복사해 사용가능
  - head 태그에 다른 스타일 시트보다 상단에 넣어야함

- Class 선택

  - m-1, m-2, m-3, m-4, m-5 : margin 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem
  - mx-0 : x축 margin 0
  - py-0 : y축 padding 0

  등 필요한 스타일을 검색해서 찾아 HTML class태그에 추가한다.



### Grid System

- Responsive Web Design, 반응형 웹 디자인 
  - 모바일 기기와 같은 다양한 화면 크기를 가진 디바이스들이 등장했다.
  - 제각기 다른 화면에 대한 웹 디자인을 어떻게 해결할 것인가? 이것에 대한 접근 방식

- Bootstrap Grid System은 flexbox로 제작됨

- container > rows > column으로 컨텐츠 배치, 정렬

- 하나의 row는 12개 column으로 나누어 지고, 각 column들은 6개 grid breakpoints가 있다.

- #### container

  - grid system의 기본 블록
  - pd, mg 에 대한 스타일 값만 갖고 있음
  - container의 최대 크기가 정해져 있음
  - container-fluid : 화면 전체를 container로 지정

- #### row

  - column들의 wrapper

- #### gutters

  - grid system에서 공간을 확보하고 컨텐츠 정렬하는 column 사이 padding

- #### breakpoints

  - 다양한 디바이스에 적용하기 위해 특정 px조건에 대한 지점을 정해둠, 이게 breakpoints
  - xs, sm, md, lg, xl, xxl 6개
  - viewport의 너비가 px 단위이므로 breakpoint에도 px 사용
  - 예시
    - `col-sm-1` : sm 사이즈에서는 이 col은 1칸 차지함
    - `col-md-3` : md 사이즈에서는 3칸 차지함
  - 보통 브라우저는 md, 태블릿이 sm, 모바일이 xs로 생각.

- #### col

  - row 당 12개 column
  - 너비는 부모 요소 기준으로 크기가 조정됨
  - 내용은 반드시 column 안에 있어야함
  - column만이 row의 바로 하위 자식

- #### offset

  - 지정한 만큼 col을 무시하고 다음 공간부터 적용
  - 앞을 비운다

- #### nesting

  - row > col > row > col 중첩 가능

- #### d-none, d-block

  - 브레이크 포인트마다 보이게할지 안보이게 할지 설정

- #### 주의

  - grid와 d-flex를 동시에 쓰려고 하면 충돌남
  - 정렬할 때 되도록 하나만 이용하자.