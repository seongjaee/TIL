# Component Binding Helper

## [컴포넌트 바인딩 헬퍼](https://vuex.vuejs.org/kr/api/#%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%A9%E1%84%82%E1%85%A5%E1%86%AB%E1%84%90%E1%85%B3-%E1%84%87%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%83%E1%85%B5%E1%86%BC-%E1%84%92%E1%85%A6%E1%86%AF%E1%84%91%E1%85%A5)

- 매핑하고자 하는 이름이 index.js에 정의해 놓은 이름과 동일하면

## mapState

- Computed와 State를 매핑
- state를 객체 전개 연산자로 계산하여 추가
- mapState는 객체를 반환하는데, 그 객체를 ... 연산자를 이용해 풀어서 새로운 object에 매핑
- `import { mapState } from 'vuex'`

- ```javascript
  computed: {
    localComputed: {
        (...)
    },
     ...mapState([
      '<stateName>'
    ])  
  }
  ```

## mapGetters

- Computed와 Getters를 매핑

## mapActions

- payload는 pass prop으로 변경해서 전달

## mapMutations

