# React Hook API 참고서

https://ko.reactjs.org/docs/hooks-reference.html를 정리한 내용

## useState

```react
const [state, setState] = useState(initialState);
```

- 상태 값과 그 값을 갱신하는 함수 반환

- 최초 렌더링 시 state는 초기값.

- `setState`는 state 갱신 시 사용되며, `setState(newState)`와 같이 새 state값을 받아 컴포넌트 리렌더링을 큐에 등록. 다음 리렌더링 시 useState가 반환하는 첫 번째 값은 갱신된 최신 state

- React는 `setState` 함수 동일성이 안정적이고 리렌더링 시에도 변경되지 않을 것을 보장. 따라서 의존성 배열에 포함하지 않아도됨.

- 이전 state를 이용해 새로운 state를 계산하는 경우 함수를 전달할 수 있음.

  ```react
  setState(prev => prev + 1)
  ```

  함수가 현재 state와 동일한 값을 반환하면 재랜더링 건너뜀.

- 갱신 객체를 자동으로 합치지 않으므로, 

## useMemo

usememo로 전달된 함수는 렌더링이 일어나는 동안 실행된다.

따라서 렌더링이 일어나는 동안 실행되면 안되는 함수를 넣으면 안됨!

예를 들면 side effect 같은 것들

서버에서 데이터를 받아오거나, 수동으로 DOM을 조작하는 함수

useMemo에 의존성 배열이 없으면 의미가 없음.

## useCallback



## useRef

useRef()는 내부의 데이터가 변경되어도 별도로 알리지 않음. 즉 재랜더링이 일어나지 않음

## useReducer









