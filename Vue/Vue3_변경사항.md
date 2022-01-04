# Vue3

Vue3는 2020년 9월에 출시되었다. 이전까지는 Vue2 버전이 주로 사용되었으나, 최근 많은 라이브러리와 기술들이 Vue3 버전을 지원 중.

## Vue2와의 차이점

[Vue3 - migration from vue2] https://v3.ko.vuejs.org/guide/migration/introduction.html

- Composition API
- Teleport
- Fragments
- Emits 컴포넌트 옵션
- 커스텀 렌더러 생성을 위한 `@vue/runtime-core` 의 `createRenderer` API
- SFC Composition API의 더 쉬운 표현
- SFC State-driven CSS 변수
- SFC의 `<style scoped>` 전역 규칙으로 사용, 특정 slot 규칙으로 사용 가능

### 글로벌 API

Vue2에서 전역 컴포넌트, `Vue.component` API를 사용

```javascript
Vue.component('button-counter', {
  data: () => ({
    count: 0
  }),
  template: '<button @click="count++">Clicked {{ count }} times.</button>'
})
```

#### Vue3의 새로운 글로벌 API:`createApp`

```javascript
import { createApp } from 'vue'

const app = createApp({})
```

`createApp` 호출로 앱 인스턴스 반환.

```javascript
import { createApp } from 'vue'
import MyApp from './MyApp.vue'

const app = createApp(MyApp)
app.mount('#app')
```

### Composition API

컴포넌트가 커짐에 따라 컴포넌트의 **논리적 관심사** 목록이 커짐.

동일한 논리적 관심사 관련 코드를 읽기 위해 "점프"를 해야함.

Composition API는 동일한 논리적 관심사와 관련 있는 코드를 함께 배치해, 코드의 유지보수와 가독성을 높여줌.

#### `setup` 컴포넌트 옵션

`setup` 컴포넌트 옵션은 컴포넌트가 생성되기 전에, props가 한번 resolved될 때 실행. compostion API의 진입점 역할.

`setup` 옵션은 `props`와 `context`에 접근하는 function.

`setup`에서 반환하는 모든 것은 다른 컴포넌트에도 노출

### Fragments

Vue2에서 `<template>`에서는 단일 루트 요소가 강제.

Vue3에서는 다중 루트 노드 컴포넌트인 fragments 지원.

### 라이프사이클 훅

Composition API에서 on 접두어를 붙여 라이프사이클 훅에 접근 가능

### `v-model` 변경

- prop : `value` => `modelValue`
- event : `input` => `update:modelValue`
- 동일 컴포넌트의 다중 `v-model` 바인딩 가능
- 사용자 지정 `v-model` 수식어 생성 기능

### `key` 속성 변경

- 조건 분기문에서는 `key` 사용 x
- `<template v-for>` 에서 `key`는 이제 `<template>` 태그에 있어야함.

### `v-if`와 `v-for` 우선순위

- `v-if`가 더 우선순위 높음
- 동일 엘리먼트에 두 디렉티브 함께 사용하지 않는 것이 좋음..

### `v-bind` 변경

- 바인딩 순서가 렌더링 결과에 영향.
- `v-bind` 와 동일한 개별 속성이 모두 정의된 경우, 나중에 사용한게 덮어씀. 

