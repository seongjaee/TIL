### 참고

- [React Query Docs](https://react-query-v3.tanstack.com/overview)
- https://github.com/ssi02014/react-query-tutorial

# React Query

> it makes **fetching, caching, synchronizing and updating server state** in your React applications a breeze.

## Why React Query

- 기존 상태 관리 라이브러리는 비동기 또는 서버 상태 관리에 좋지 못함.
  - 서버 상태란?
    - DB에 저장되어있는 데이터 등 클라이언트와 서버가 비동기적으로 공유하는 상태
- 서버 상태는
  - 컨트롤하거나 소유할 수 없는 위치에서 원격으로 유지됨
  - 조회나 업데이트를 위한 비동기 API가 필요함
  - 나도 모르게, 다른 사람에 의해 변경될 수 있음
  - 데이터 최신 여부 보장이 어려움
- 애플리케이션에서 서버 상태를 관리하기 위해 다음과 같은 어려움이 있음
  - 캐싱…(프로그래밍에서 가장 어려움)
  - 동일 데이터에 대한 여러 요청을 단일 요청으로 중복 제거
  - 백그라운드에서 “구식” 데이터 업데이트
  - 데이터가 “구식”이 되면 알아채기
  - 최대한 빠르게 데이터 업데이트 반영
  - 페이지네이션, lazy loading 데이터 등 성능 최적화
  - 서버 상태 메모리, 가비지 콜렉션 관리
  - 쿼리 결과 메모이징
- React Query의 장점
  - 애플리케이션의 복잡, 어려운 많은 코드 제거, React Query 로직을 가진 유용한 코드들로 교체 ( 보일러플레이트 코드 제거 )
  - 애플리케이션 유지보수성을 높이고 기능 추가가 쉬워짐
  - 애플리케이션의 속도, 응답성을 높여 사용자들에게 직접적인 영향을 줌
  - 대역폭 절감, 메모리 성능 향상

## What is React Query

- React 애플리케이션에서 `서버 상태 조회` , `캐싱` , `동기화 및 업데이트` 를 쉽게 다룰 수 있게 도와주고, 클라이언트 상태와 서버 상태를 구분하기 위해 만들어진 라이브러리

### React Query 기능 및 장점

- 자동
  - 데이터를 가져올 위치와 데이터가 얼마나 필요한지만 지정하면 됨. 별다른 config없이 즉시 캐싱, 백그라운드 업데이트.
- 간단
  - Redux 같이 무겁고 커다란 코드가 필요치 않다. Promise만 다룰 수 있으면 쉽게 다룰 수 있다.
- 도구들
  - 전용 Devtool 지원

### useQuery

- Query
  - unique
  - 데이터의 비동기 소스와 선언적인 의존성
  - unique key(queryKey)와 function(queryFn), (options) 으로  구성

**useQuery의 매개변수**

- unique key(queryKey)
  - 내부적으로 재조회, 캐싱, 쿼리 공유에 사용됨
  - 배열로 지정
- Query Function
  - Promise 베이스 메서드로 서버에 data fetch하는데 사용
  - Promise를 반환해야함.
  - 서버 데이터를 업데이트(create/update/delete)하는 경우 useQuery가 아니라 Mutation을 사용할 것을 권고
- options
  - 다양한 옵션이 있음. 공식 문서를 참고하자.

**useQuery의 반환값**

- status

  - Query는 4가지 상태가 존재.(v4부터는 Idle 제거되어 3가지)
  - `loading` : query에 데이터가 없으며 조회중
  - `error` : query 중 에러를 만남
  - `success` : query는 성공적이었고 데이터 접근 가능

- `data`
  - Query Function이 반환한 Promise가 resolved된 데이터

- `isLoading`
  - 데이터가 없으며 로딩중을 나타내는 Boolean 값
  - 만약 캐싱된 데이터가 있으면 항상 false

- `isFetching`
  - 쿼리가 실행 중인지를 나타내는 Boolean값.
  - 캐싱된 데이터가 있더라도 쿼리 중이라면 true

- `error`
  - Query에서 발생한 에러 객체

- `isError`
  - 에러가 발생하면 true

### useMutation mutate

- Query와 달리 데이터 create/update/delete 또는 서버 사이드 이펙트 수행에 사용

- useMutation의 반환 값인 mutation 객체의 mutate 메서드를 통해 요청 함수 호출

  ```jsx
  const mutation = useMutation(newTodo => {
    return axios.post('/todos', newTodo)
  })
  
  // ...
  
  <button
   onClick={() => {
     mutation.mutate({ id: new Date(), title: 'Do Laundry' })
   }}
  >
   Create Todo
  </button>
  ```

### 쿼리 무효화 (Query Invalidation)

- 사용자가 무엇인가 완료했을 때(데이터 수정), 이전의 쿼리 데이터가 이제 “구식”(out of date, stale)임을 알 수 있다. 이 경우, Query가 자동으로 재조회하길 기다리지 않고, 강제로 Query를 최신화해야한다. 이렇게 이전의 Query를 무효화하고 최신화할 때, `invalidateQueries()` 를 사용한다.
- 즉 query가 오래되었다는 걸 판단하고 다시 `refetch` 할 때 쿼리 무효화를 진행한다.
