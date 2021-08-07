# Web_02

## CSS

Cascading Style Sheets

스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어

- CSS 구문
  - CSS구문은 선택자(selector)로 시작
  - 선택자로 스타일을 지정할 HTML 요소 선택
  - 중괄호 안에 속성(property), 값(value) 쌍으로 이루어진 선언(declaration)
    - 속성 : 어떤 스타일 기능을 변경할지
    - 값 : 어떻게 스타일 기능을 설정할지
- CSS 정의 방법
  - 인라인
    - HTML 태그 안에 직접 style 속성 활용
  - 내부 참조
    - head 태그 내에 `<style>` 에 지정
  - 외부 참조 (대부분 사용)
    - 외부 CSS 파일을 `<head>` 내 `<link>`를 통해 불러옴

### CSS Selectors

- 기본 선택자

  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자

- 결합자

  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자

- 의사 클래스/ 요소

  - 링크, 동적
  - 구조적

- 전체 선택자 : `*`

- 요소 선택자 : `h2` , `h2, h3`

  - HTML 태그 직접 선택

- 클래스 선택자 : `.(class)` 

  - 해당 클래스가 적용된 모든 항목

- id 선택자 : `#(id)` 

  - 해당 클래스가 적용된 모든 항목에 적용되지만,
  - 일반적으로 하나 문서에 1개만(Unique)

- 자식 결합자 : `(부모) > (자식)` 

  - 직계 자식만

- 자손 결합자 : `(부모) (자식)` 

  - 모든 하위 태그

- CSS 적용 우선 순위(cascading order)

  1. 중요도 - 주의, 사용 거의 안함
     - `!Important` 를 붙이면 순위가 가장 높음

  2. 우선 순위
     - 인라인 > id 선택자 > class 선택자 > 속성 선택자 > 요소 선택자 > 의사 요소

  3. 소스 순서

- CSS 상속
  - 부모 요소의 속성을 거의 모두 자식에게 상속
  - 상속되는 것
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것
    - Box model 관련 요소(width, height, margin, padding 등), position 관련 요소(position, top/bottom/right/left 등)

### CSS 단위

- 크기 단위

  - px(픽셀)
    - 고정적인 단위
    - 모니터마다 다름
  - %
    - 백분율
    - 가변적인 레이아웃

  - em
    - 상속의 영향
    - 부모를 기준으로 배수 단위
  - rem
    - 상속의 영향 x
    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위
  - viewport
    - 웹 페이지를 방문한 유저에게 보이는 영역
    - 주로 스마트폰이나 테블릿 디바이스 화면
    - viewport 기준으로 상대적 사이즈 결정
    - vw, vh, vmin, vmax

- 색상 단위

  1. 색상 키워드
     - 대소문자 구별 x
     - red, blue, black 특정 색 글자
  2.  RGB 색상
     - '#' + 16진수 표기법
     - rgb() 함수 표기법
  3. HSL 색상
     - hsl() 색상, 채도, 명도 표기

  - a는 alpha 투명도 추가

- CSS 문서 표현
  - 텍스트
    - 변형 서체
  - 컬러, 배경
  - 목록 꾸미기
  - 표 꾸미기

### CSS Selectors +

#### 결합자(Combinators)

- 자손 결합자
  - 하위 모든 요소 선택
- 자식 결합자
  - 바로 아래 요소 선택
- 일반 형제 결합자 `~`
  - 형제 요소(레벨이 같은) 중 뒤에 위치하는 요소를 모두 선택
- 인접 형제 결합자 `+`
  - 형제 요소(레벨이 같은) 중 바로 뒤에 위치하는 요소 선택



### CSS Box model

- HTML의 모든 요소는 box 형태

- Box model 구성

  - Margin
    - 테두리 바깥의 외부 여백
    - 배경색 지정 x
  - Border
    - 테두리 영역
  - Padding
    - 테두리 안쪽 내부 여백
    - content ~ border 사이
  - Content
    - 요소 실제 내용
  - margin/padding 지정에서 방향 생략 시 shorthand
    - 값 하나 : 상하좌우
    - 값 둘 : 상하/좌우
    - 값 셋 : 상/좌우/하
    - 값 넷 : 상/우/하/좌

  - border도 shorthand 있음

- box-sizing
  - content-box(default)
    - `width: 100px;`은 기본적으로 content의 너비를 말함
    - 이거 불편함
  - border-box
    - 보통 전체 선택자에`box-sizing: border-box;`로 설정
- 마진 상쇄
  - block A의 top과 block B의 bottom에 적용된 각각의 margin이 둘 중 큰 마진값으로 겹쳐짐
  - 보통 한 쪽으로만 margin을 줌
  - 호락호락하지 않군...

### CSS Display

어떻게 보여지는지(display)에 따라 문서의 배치가 달라짐

HTML 요소들을 어떻게 보여줄지 결정하는 속성

- `display: block` : 욕심쟁이
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체 가로 폭 전부 차지
  - 블록 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- `display: inline` : 소심쟁이
  - 줄 바꿈이 일어나지 않는 요소
  - 컨텐츠 너비만큼만 가로 폭 차지
  - width, height, margin-top, margin-bottom 지정 x
  - line-height로 상하 여백 지정

- [블록 레벨 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Block-level_elements)
  - `<div>` / `<ul>`, `<ol>` ,`<li>` / `<p>` / `<hr>` / `<form>`등
- [인라인 레벨 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements)
  - `<span>` / `<a>` / `<img>` / `<input>` ,`<label>` / `<b>` ,`<em>` ,`<i>`, `<strong>` 등
- 속성에 따른 수평 정렬
  - block : `margin-right: auto;` = inline: `text-align: left;`
- `display: inline-block`
  - block 과 inline 레벨 요소 모두 갖음
  - inline처럼 한 줄 표시 가능
  - block 처럼 width, height, margin 속성 지정 가능
- `display: none`
  - 해당 요소를 화면에 표시하지 않음. 공간조차 없어짐
  - `visibility: hidden` : 공간은 차지하나 화면에 보이지는 않음
- 다양한 display 속성- [MDN CSS display](https://developer.mozilla.org/ko/docs/Web/CSS/display)

### CSS Position

- 문서 상에 요소를 배치하는 방법을 지정
- `static` : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서(좌측 상단)
  - 부모 요소 내에 배치될 때는 부모 요소 위치 기준 배치
- 아래 세 개는 좌표 프로퍼티로 이동 가능
  - `relative` : 상대 위치
    - 자기 자신의 static 위치를 기준으로 이동
    - 요소가 차지하는 공간은 static일 때와 같음(과거 자기 위치)
    - 보이는 것만 이동, 차지하는 공간은 그대로
  - `absolute` : 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    - 'static이 아닌' 가장 가까운 부모 요소를 기준으로 이동
  - `fixed` : 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    - 부모요소와 관계없이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 위치

- `absolute` 특징
  - 원래 위치의 공간은 더이상 존재하지 않음
  - 다른 모든 것과 별개로 독자적인 곳
  - 페이지의 다른 요소 위치와 간섭하지 않는 격리된 사용자 인터페이스 기능 만드는데 활용
    - 팝업 정보 상자, 제어 메뉴, 롤오버 패널, 페이지 어디서나 끌어올수 있는 유저 인터페이스

### Emmet

- HTML & CSS 작성 시 빠른 마크업을 위한 오픈소스