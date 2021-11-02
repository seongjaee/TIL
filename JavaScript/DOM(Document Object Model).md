# DOM(Document Object Model)

- 브라우저에서 할 수 있는 일
  - DOM 조작
    - 문서 조작
  - BOM 조작
    - navigator, screen, location, frames, history, XHR
  - JavaScript Core(ECMAScript)
    - Data Structure(Object, Array), Conditional Expression, Iteration

## DOM이란?

- 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급, 논리적 트리 모델
- 단순 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - window : DOM을 표현하는 창, 최상위 객체, 작성 시 생략가능
  - document : 페이지 컨텐츠 시작 포인트, 다른 요소들 포함
  - navigator, location, history, screen



### DOM 해석

- 파싱(Parsing)
  - 브라우저가 문자열을 해석해서 DOM Tree로 만드는 과정

- 스타일링(Styling)
- 레아이웃(Layout)

## BOM 이란?

- Browser Object Model
- 자바스크립트가 브라우저와 소통하기 위한 모델

- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어하는 수단
- window 객체는 모든 브라우저로부터 지원받음



## DOM 조작

- Document를 조작
- 조작 순서
  1. 선택 Select
  2. 변경 Manipulation

### DOM 관련 객체의 상속구조

- EventTarget
  - Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- Node
  - 여러 DOM 타입들이 상속하는 인터페이스
- Element
  - Document 안의 모든 객체가 상속하는 가장 범용적인 기반 클래스
- Document
  - 브라우저가 불러온 페이지
  - DOM 트리 진입점 역할
- HTMLElement
  - 모든 종류의 HTML 요소
  - 부모 element 속성 상속



### DOM 선택

- `Document.querySelector(selector)`
  - 선택자와 일치하는 element 하나 선택
  - 제공한 CSS selector를 만족하는 첫번째 element 객체 반환 없으면 null
- `Document.queuySelectorAll(selector)`
  - 제공한 선택자와 일치하는 여러 element 선택
  - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 지정된 셀렉터에 일치하는 NodeList 반환

- `getElementById(id)`
- `getElementByTagName(name)`
- `getElementByClassName(names)`

- `querySelector`, `querySelectorAll` 은 id, class, tag name 등 모두 사용가능함. 더 구체적이고 유연하게 선택가능

- 선택 메서드별 반환 타입
  - 단일 element
    - getElementById
    - querySelector()
  - HTMLCollection
    - getElementByTagName
    - getElementByClassName
  - NodeList
    - querySelectorAll

- HTMLCollection & NodeList
  - 둘 다 배열 같이 각 항목에 접근하기 위한 index 제공
  - HTMLCollection
    - name, id, index 속성으로 항목에 접근 가능
  - NodeList
    - index로만 항목에 접근 가능
    - 단, 배열에서 사용하는 forEach 함수 및 다양한 메서드 사용 가능
  - 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, `querySelectorAll()`에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영 X



### DOM 변경

- `Document.createElement()`

  - 작성한 태그 명의 HTML 요소 생성해 반환

- `Element.append()`

  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString 삽입
  - 여러 개의 객체를 추가할 수 있음
  - 반환 값 없음

- `Node.appendChild()`

  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 삽입 (Node 객체만) 

  - 한번에 오직 하나의 Node만 추가 가능
  - 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조하면 새로운 위치로 이동

- `Node.innerText`
  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현
  - 줄 바꿈 인식하고 숨겨진 내용 무시 등 최종적으로 스타일링 적용된 모습을 표현
- `Element.innerHTML`
  - 요소 내 포함된 HTML 마크업을 함께 반환
  - XSS 공격에 취약하므로 사용 시 주의
    - XSS (Cross-site Scripting)
    - 자바스크립트 코드를 삽입해 클라이언트가 실행하게 함.

### DOM 삭제

- `ChildNode.remove()`
  - Node가 속한 트리에서 해당 Node를 제거
- `Node.removeChild()`
  - DOM에서 자식 Node 제거 후 제거된 Node 반환
  - Node는 인자로 들어가는 자식 Node의 부모 Node

### DOM 속성

- `Element.setAttribute(name, value)`

  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 갱신, 존재하지 않으면 새 속성 추가

- `Element.getAttribute(attributeName)`

  - 해당 요소의 지정된 값을 반환, 없으면 null 반환

  - 인자는 값을 얻고자 하는 속성의 이름




### custom attribute

- HTML에서 `data-` 로 시작하는 속성을 커스텀할 수 있다.
- 불러올 땐 `.dataset`으로 불러온다.

