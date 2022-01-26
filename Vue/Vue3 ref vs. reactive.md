# Vue3 ref vs. reactive

https://stackoverflow.com/questions/61452458/ref-vs-reactive-in-vue-3 정리

## 핵심

- `reactive()` 는 객체만 받음. String, Boolean, Number, null, undefined 등 JS primitive는 안됨.
- `ref()`는 내부적으로 `reactive`를 호출함.
- `reactive()`가 객체에 작동하므로 `reactive()`를 호출하는 `ref()`도 객체에 잘 작동함.
- 근데 `ref()`는 `.value` 속성이 있어서 재할당이 가능. `reactive()`는 이게 없어서 재할당 불가능

## `ref()`를 쓰면 좋을 때

- Primitive 인 경우,(String, Boolean, Number 등)
- 나중에 재할당할 필요가 있는 객체(예를 들어 array)
  - `ref([])`는 `ref(reactive([]))`랑 완전히 같음.

## `reactive()`를 쓰면 좋을 떄

- 나중에 재할당할 필요가 없는 객체일 때, 그리고 `ref()`의 오버헤드를 피하고 싶을 때.

## 요약

`ref()`는 모든 객체 타입에 작동하는데다 `.value`로 재할당까지 가능하다. `ref()` 로 시작하기는 좋으나, API에 익숙해질수록 오버헤드가 적은 `reactive()`가 더 좋을 수 있음.