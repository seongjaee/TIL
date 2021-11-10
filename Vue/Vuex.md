# [Vuex](https://vuex.vuejs.org/kr/)가 뭔가요?

## Vuex

- Statement management pattern + Library
- 상태를 전역 저장소로 관리할 수 있게 하는 라이브러리
  - 상태가 예측 가능한 방식으로만 변경될수 있도록 보장하는 규칙 설정
  - 모든 컴포넌트에 대한 중앙 집중식 저장소 역할

### 상태관리 패턴

- 컴포넌트의 공유된 상태를 추출하고 이를 전역에서 관리
- 모든 컴포넌트는 트리에 상관없이 상태에 액세스하거나 동작을 트리거
- 상태 관리 및 특정 규칙 적용과 관련된 개념을 정의하고 분리함으로써 코드의 구조와 유지 관리 기능 향상

#### State

- 상태는 곧 데이터, 해당 애플리케이션의 핵심 요소
- 중앙에서 관리하는 모든 상태 정보

- 원본소스

#### view

- state의 선언적 매핑

#### action

- view에서 사용자의 입력에 반응하여 state변경

### 기존의 Pass props & Emit event

- 각 컴포넌트는 독립적으로 데이터 관리

- 데이터의 단방향 흐름

  - state : 원본소스
  - view : state의 선언적 매핑
  - action : view에서 사용자의 입력에 반응하여 state변경

- 장점

  - 데이터 흐름 직관적 파악

- 단점

  - 컴포넌트 중첩이 깊어지면 데이터 전달이 복잡해짐

  - 공통의 상태를 공유하는 여러 컴포넌트가 있는 경우 데이터 전달이 복잡

  

### Vue management pattern

- 중앙 저장소에 state를 모아놓고 관리
- 규모가 큰 프로젝트에서 효율적
- 각 컴포넌트는 중앙 집중 저장소의 state만 신경씀
  - 동일한 state를 공유하는 컴포넌트들도 동기화



##  Vuex Core Concepts

- State                ==( Render )==>      Components

- Components  ==( Dispatch )==>   Action

- Action              ==( Commit )==>    Mutations

- Mutations       ==( Mutate )==>      State

### Vuex 핵심 컨셉

1. State
2. Mutations
3. Actions
4. Getters

### 1. State

- 중앙에서 관리하는 모든 상태 정보, 데이터
  - Vuex는 단일 상태 트리 single state tree 사용
  - 단일 객체는 모든 앱 상태를 포함하는 원본 소스 역할
  - 각 앱마다 하나의 저장소만 갖게된다
- 여러 컴포넌트 내부의 특정 state를 중앙에서 관리
  - Vuex Store에서 각 컴포넌트가 사용하는 state 한 눈에 파악 가능
- state가 변화하면 해당 state를 공유하는 모든 컴포넌트의 DOM이 자동으로 렌더링
- 각 컴포넌트는 Vuex Store에서 state 정보를 가져옴

### 2. Mutations

- 변이. state를 변경하는 유일한 방법
- mutation의 handler함수는 반드시 동기적이어야함
  - 비동기적 로직은 state가 변화하는 시점이 의도와 달라질 수 있음. 콜백이 실제로 호출될 시기를 알 수 없음
- 첫번째 인자로 항상 state
- Actions에서 commit() 메서드에 의해 호출

### 3. Actions

- state를 변경하는 대신 mutations를 commit() 메서드로 호출해서 실행
- mutation과 달리 비동기 작업이 포함될 수 있음

- context 객체 인자를 받음
  - context 객체를 통해 store.js 파일 내 모든 요소 속성 접근, 메서드 호출
  - 하지만 state를 직접 변경하지는 않음
- 컴포넌트에서 dispatch() 메서드에 의해 호출
- Actions를 통해 state를 조작할 수 있지만 state는 오로지 Mutations를 통해서만 조작해야함.
  - **명확한 역할 분담! 을 통한 state의 올바른 관리 유지**

### 4. Getters

- state를 변경하지 않고 활용하여 계산을 수행(computed와 유사)
  - 실제 계산된 값을 사용하는 것처럼 state를 기준으로 계산

- state의 종속성에 따라 cache되고 종속성이 변경된 경우에만 다시 재계산
- getters가 state를 변경하지는 않음

## Vuex 사용

- vue CLI에서 `$ vue add vuex`

- store 폴더가 새로 생김
  - store/index.js 에 Vuex core concepts를 작성

- 주의
  - Vuex Store에 반드시 모든 상태를 넣어야하는 건 아님.
  - Components Can Still Have Local State
- 데이터 가져오기
  - `$store.state`

- dispatch
  - `$store.dispatch(<호출할 actions>, <payload>)`
- Mutation handler name
  - Mutation 핸드러 함수는 상수로 작성 권장
  - 다른 tool에서 디버깅 유용 어떤 것이 mutation인 지 파악 쉬워짐



## Vuex persistedstate

- 페이지가 리로드되어서 state가 유지되도록 도와주는 라이브러리

- state를 local storage에 저장