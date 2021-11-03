# Syntax of Vue.js

## Vue instance

- 모든 Vue 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작
  - `const app = new Vue({ })`

- Vue 인스턴스 생성 시 option 객체를 전달해야함
- Options들을 사용하여 원하는 동작을 구현
- Vue Instance === Vue Component



## Options/DOM - `'el'`

- Vue 인스턴스에 연결(마운트) 할 기존 DOM 엘리먼트 필요
- CSS 선택자 문자열 또는 HTML Element로 작성
- new를 이용한 인스턴스 생성 때만 사용

- ```javascript
  const app = new Vue({
  	el: '#app',
  })
  ```

## Options/DOM - `'data'`

- Vue 인스턴스의 데이터 객체
- Vue 인스턴스의상태 데이터 정의
- Vue template에서 interpolation을 통해 접근 가능
- v-bind, v-on등 directive에서도 사용 가능
- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능

- 화살표 함수를 `data`에서 사용하면 안됨.
  - this가 Vue 인스턴스를 가리키지 않음

## Options/DOM - `'methods'`

- Vue 인스턴스에 추가할 메서드
- Vue template에서 interpolation을 통해 접근 가능

- v-bind, v-on등 directive에서도 사용 가능

- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능

- 화살표 함수를 메서드를서 사용하면 안됨.
  - this가 Vue 인스턴스를 가리키지 않음.



## Template Syntax

- 렌더링 된 DOM을 기본 Vue 인스턴스 데이터에 선언적으로 바인딩 할 수 있는 HTML 기반 템플릿 구문 사용

1. Interpolation
   - `{{  }}`
2. Directive
   - `v-`

### Interpolation

1. Text
   - `{{ msg }}`
2. Raw HTML
   - `v-html="rawHtml"`

3. Attributes
   - `v-bind:id="dynamicId"`
4. JS 표현식
   - `{{ number + 1 }}`
   - `{{ msg.split('') }}`



### Directive

- v- 접두사가 있는 특수속성
- `v-text`, `v-html`, `v-show`, `v-if` 등등
- 속성 값은 단일 JS 표현식(`v-for` 제외)
- 표현식의 값이 변경될 떄 반응적으로 DOM에 적용하는 역할
- 전달인자
  - `:`을 통해 전달인자 받음
- 수식어
  - `.`으로 표시되는 특수 접미사
  - directive를 특별한 방법으로 바인딩해야함.



- `v-text`
  - 엘리먼트의 textContent를 업데이트
  - 내부적으로 interpolation 문법이 `v-text`로 컴파일 됨.
- `v-html`
  - innerHTML을 업데이트
    - XSS 공격에 취약
  - 임의의 사용자로부터 받은 내용 절대 사용 금지.

- `v-show`
  - 조건부 렌더링 중 하나
  - 엘리먼트는 항상 렌더링 되고 DOM에 남아있음
  - display CSS 속성을 토글

- `v-if`, `v-else-if`,`v-else`

  - 조건부 렌더링 중 하나
  - 조건에 따라 블록을 렌더링

  - directive 표현식이 true일 때만 렌더링
  - 엘리먼트 및 포함된 directive는 토글하는 동안 삭제하고 다시 작성



- `v-show` vs `v-if`
  - v-show (Expensive initial load, cheap toggle)
    - CSS display 속성을 hidden으로 만들어 토글
    - 초기 렌더링 비용은 높으나 이후 토글 비용이 적음
  - v-if (Cheap initial load, expensive toggle)
    - false인 경우 렌더링 되지 않음
    - 초기 렌더링 비용은 낮으나 토글 비용이 큼

- `v-for`
  - 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록 여러번 렌더링
  - item in items 구문
  - item 위치 변수를 각 요소에서 상ㅇ 가능
    - 객체 경우 key
  - v-for 사용시 반드시 key속성을 각 요소에 작성
  - v-if와 함께 사용하면 v-for가 우선순위가 높음
    - 하지만 if와 for를 동시에 쓰면 안됨
- `v-bind`
  - HTML 요소 속성에 Vue 상태 데이터를 값으로 할당
  - Object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당
  - 약어로 `:`

- `v-model`

  - HTML form 요소와 data를 양방향 바인딩

  - 수식어

    - `.lazy` : input 대신 change 이벤트 이후에 동기화

    - `.number` : 자동으로 숫자로 형변환
    - `.trim` : 자동으로 trim(양쪽 공백 제거)

## Options/DOM - `'computed'`

- 데이터를 기반으로 하는 계산된 속성
- 함수 형태로 정의, 하지만 함수가 아닌 함수의 반환 값이 바인딩
- 종속된 데이터에 따라 저장
- **종속된 데이터가 변경될때만 함수를 실행**
  - 데이터에 의존하지 않는 computed 속성의 경우  업데이트되지 않음
- 반드시 반환값이 있어야함

- computed vs methods
  - 두 가지 접근 방식은 서로 동일
  - computed 속성은 종속 대상을 따라 저장된다는 차이점
  - 종속된 대상이 변경되지 않는 한 함수를 다시 호출해도 계산하지 않고 이미 계산된 결과를 반환
  - 이에 비해 methods를 호출하면 렌더링을 다시 할 때마다 항상  함수를 실행

## Options/DOM - `'watch'`

- 데이터에 변화가 일어났을 때 실행되는 함수
- 함수명은 감시할 데이터의 이름으로 작성
- computed vs watch
  - computed
    - 특정 값이 변동하면 해당 값을 다시 계산해서 보여준다.
    - 특정 데이터를 직접 사용, 가공하여 다른 값으로 만들 때 사용
    - 속성은 계산해야하는 목표 데이터를 정의하는 방식, 선언형 프로그래밍 방식
  - watch
    - 특정 값이 변동하면 다른 작업을 한다.
    - 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야할 때 사용
    - 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행
    - 명령형 프로그래밍 방식

## Options/DOM - `'filter'`

- 텍스트 형식화를 적용할 수 있는 필터
- interpoltaion 또는 v-bind 이용 시 사용 가능
- 표현식 `|` 필터 형식으로 사용
- 필터의 인자는  `|` 앞에 나올 변수
- chaining 가능 

