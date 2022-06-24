#  CSS-in-JS

## CSS-in-CSS

### CSS 모듈

- CSS 클래스를 만들면 자동으로 고유한 클래스네임을 만들어 scope를 제한하게 됨

  - 아래와 같이 .css file을 작성하면

    ```css
    .container {
        width: 320px;
        background: blue;
    }
    ```

  - HTML에 렌더링될 때 아래와 같이 고유한 클래스 네임이 만들어진다.

    ```css
    .container_4xks92k2kl {
        width: 320px;
        background: blue;
    }
    ```

- 중복 및 관리의 위험성이 적고, CSS 네이밍 규칙이 간소화된다는 장점

- 하지만 별도로 많은 CSS 파일을 만들어 관리해야한다는 단점

### CSS preprocessor

- CSS 전처리기, CSS를 정적으로 분석하여 별도의 CSS 파일로 추출
- 자신만의 특별한 syntax로 CSS를 생성하는 프로그램.
- Sass, Less, Stylus 등
- CSS 만을 사용했을 때의 문제점을 변수, 함수, 상속 등 일반적인 프로그래밍 개념을 사용해 보완
- 개발 시간, 비용 절약, 구조화된 코드 유지 및 관리 용이의 장점
- 컴파일하는데 시간이 소요된다는 단점

## CSS-in-JS

- 자바스크립트 코드에서 CSS를 작성하는 방식. 2014년 페이스북 개발자 Christopher Chedeau가 처음 소개.
- 기존 CSS를 작성하는 어려움을 해결할 수 있다고 강조
  - Global namespace : 글로벌 공간에서 선언된 이름의 명명 규칙 필요
  - Dependencies : CSS 간 의존 관리
  - Dead Code Elimination : 미사용 코드 검출
  - Minification : 클래스 이름 최소화
  - Sharing Constants : JS와 CSS의 상태 공유
  - Non-deterministic Resolution : CSS 로드 우선 순위 이슈
  - Isolation : CSS와 JS의 상속에 따른 격리 필요 이슈
- 컴포넌트 라이프 스타일에 맞게 스타일을 적용할 수 있기 때문에 동적 스타일 적용에 자유롭다.
- 해당 컴포넌트가 렌더링 될때만 스타일 태그를 생성하기 때문에 컴포넌트 기반 프레임워크에 용이하다.
- 원리
  - 클래스 이름을 따로 명명하지 않는다. 브라우저 렌더링 시 webkit 엔진이 CSS 파일과 classname 태그를 기반으로 렌더링 트리를 생성하기 때문에 모든 CSS-in-JS는 CSS preprocessor를 내장한다.
  - 런타임 시 각 컴포넌트를 hashing하여 동적인 클래스 네임을 생성하고 head 태그에 style태그를 추가한다.
  - styled-components는 stylis(CSS preprocessor) 이용

- 많은 라이브러리들
  - styled-components
  - jss
  - emotion 등

### CSS-in-JS 라이브러리 간의 특징 정리

CSS-in-JS 라이브러리 간에 가장 중요한 차별 요소는 "스타일을 얼마나 동적으로 작성할 수 있는가".

이를 기준으로 나누면 다음과 같다.

#### 1세대

- CSS preprocessor를 사용하여 css 모듈 형태로 사용
- CSS를 정적으로 분석하여 별도의 CSS 파일 추출.
- runtime에서의 동작이 없기 때문에 zero runtime css-in-js 특징

#### 2세대

- JS 변수를 활용하여 CSS를 작성할 수 있는 Radium 같은 라이브러리.
- 컴포넌트에서 스타일을 제어할 수 있으나, inline style을 사용하므로 pseudo selector 등 CSS의 모든 spec 사용 불가

#### 3세대

- 2세대의 css syntax 한계를 극복.
- JavaScript 템플릿으로 CSS를 작성하면 빌드 과정에서 `<style>` 태그를 생성하여 주입.
- 동적으로 변경되는 스타일을 정의하기 까다롭다는 단점

#### 4세대

- JavaScript 코드로 제어하는 동적 스타일링을 runtime 개념을 도입해 해결
- build time에서 모든 스타일을 생성하는 것이 아닌, runtime을 활용.



#### 다음 세대?

- 복잡한 스타일 계산에서 발생하는 Runtime overhead를 해결하기 위해 zero-runtime을 주장하는 라이브러리들이 등장.
- zero-runtime css-in-js
  - runtime에서 동작이 없는 css-in-js.
  - Linaria는 styled-components에서 영감을 받아 유사한 API를 가진 라이브러리로 zero-runtime으로 동작.
  - 1세대에서는 할 수 없던 prop, state에 따른 동적 스타일링 가능
    - 내부적으로 css variable을 사용하고 있기 때문. 스타일 시트를 새로 만들지 않고 css variable만 수정하여 달라지는 조건에 대해 스타일을 다르게 적용.

### Critical CSS

https://web.dev/i18n/ko/extract-critical-css/

- **Critical CSS** : 사용자에게 가능한 한 빨리 콘텐츠를 렌더링하기 위해 스크롤 없이 볼 수 있는 콘텐츠에 대한 CSS를 추출하는 기술
- 즉, 현재 화면에서 필요한 CSS만 효율적으로 먼저 로딩하는 기술.
- **스크롤없이 볼 수 있는 부분**은 스크롤하기 전 페이지 로드 시 뷰어가 보는 모든 콘텐츠. 다양한 장치와 화면 크기가 있기 때문에 보편적으로 정의된 픽셀 높이는 없다.



#### styled-components에서의 Critical CSS

- 페이지에서 사용하는 CSS만 head에 `<style>` 태그로 삽입된다.
- 현재 페이지에서 사용되고 있는 스타일만 별도의 스타일 시트로 생성한다.
- 최초 렌더링 이후 prop이나 state에 의해 변경되는 스타일은 `<style>` 태그에 동적으로 삽입



## 참고 문서

- [웹 컴포넌트 스타일링 관리 CSS-in-JS vs CSS-in-CSS](https://www.samsungsds.com/kr/insights/web_component.html)

- https://so-so.dev/web/css-in-js-whats-the-defference/

- https://web.dev/i18n/ko/extract-critical-css/

  