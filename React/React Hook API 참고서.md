# React Hook API 참고서

https://ko.reactjs.org/docs/hooks-reference.html를 정리한 내용입니다.

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

- `Object.is` 비교 알고리즘을 통해 동일한 값인지 확인.

- 렌더링 시 고비용 계산한다면 `useMemo`로 최적화 가능.



## useEffect

```react
useEffect(didUpdate)
```

- 명령형 또는 effect를 발생하는 함수를 인자로 받음
- side effects들은 함수 컴포넌트 본문이 아니라 `useEffect`에 사용해야함.
- `useEffect`에 전달된 함수는 렌더링 완료 후에 수행됨.
- React의 순수한 함수적인 세계에서 명령적인 세계로의 탈출구
- clean-up 함수를 반환할 수 있음. 다음 effect가 수행되기전에 이전 effect는 정리됨.
- 지연되면 안되는 effect가 있을 수 있음. 예를 들면 사용자에게 노출되는 DOM 변경은 다음 화면을 다 그리기 전에 동기화 되어야함. 이런 종류의 effect를 위해 `useLayoutEffect`를 제공함.



## useMemo

```react
const memoizedValue = useMemo(
	() => {
        return computeExpensiveValue(a, b);
    },
    [a, b]
);
```

- 메모이제이션된 값(Memoized value)를 리턴하는 Hook
- "생성" 함수와 의존성 배열을 인자로 전달해서 사용.
- 연산량이 많은 함수의 호출 결과를 저장해두었다가 같은 입력값으로 함수를 호출하면 기존의 저장되어 있던 결과를 반환 => 렌더링 시의 고비용 계산을 방지해 자원을 아낌

- usememo로 전달된 함수는 렌더링이 일어나는 동안 실행된다.
  따라서 렌더링이 일어나는 동안 실행되면 안되는 함수를 넣으면 안됨!
  - 예를 들면 side effect 같은 것들
  - 서버에서 데이터를 받아오거나, 수동으로 DOM을 조작하는 함수

- useMemo에 의존성 배열이 없으면 의미가 없음. 매 렌더링마다 함수가 실행되기 때문.
- 성능 최적화를 위해 사용할 수 있지만, 의미론적 보장이 되는 것은 아님.

## useCallback

```react
const memoizedCallback = useCallback(
  () => {
    doSomething(a, b);
  },
  [a, b],
);
```

- 메모이제이션된 콜백(Memoized callback)을 리턴하는 Hook

- 콜백과 의존성 배열을 인자로 전달해서 사용.

- 렌더링이 일어날 때마다 콜백을 재정의하는 것이 아니라 콜백의 의존성이 변경되었을 때만 새로 콜백을 정의해서 리턴.

- `useCallback` 은 동일한 참조에 의존하는 자식 컴포넌트에 콜백을 전달하면, 불필요한 렌더링을 방지할 수 있기 때문에 유용하다.

  ```react
  function ParentComponent(props) {
      const [count, setCount] = useState(0);
      
      const handleClick = useCallback((event) => {
          // 클릭 이벤트
      }, []);
      
      return {
          <>
            <button
              onClick={() => {
                  setCount(count + 1);
              }}
            >
          		{count}
            </button>
          
            <ChildComponent handleClick={handleClick} />
          </>
      }
  }
  ```

  `useCallback`을 사용하지 않고 부모 컴포넌트에서 정의한 함수를 자식 컴포넌트에 props로 내려주면, 부모 컴포넌트 렌더링마다 함수가 재정의되므로

  의존성 배열에 빈 배열이 들어갔기 때문에 컴포넌트 마운트 시점에만 함수가 정의됨.  자식 컴포넌트가 불필요하게 재렌더링되지 않음.

- `useCallback(fn, deps)` 와 `useMemo(() => fn, deps)`는 동일한 역할을 함.

- 

## useRef

```react
const refContainer = useRef(initialValue);
```

- Reference를 사용하기 위한 Hook

- **Reference** : 특정 컴포넌트에 접근할 수 있는 객체

  - `.current` 속성 : 현재 참조하고 있는 Element

- `initialValue`로 초기화된 ref 객체를 반환. 반환된 객체는 컴포넌트가 언마운트되기 전까지 유지.

- `useRef`는  `.current` 속성에 변경 가능한 값을 담고있는 상자로 생각할 수 있음.

- 일반적으로 자식에게 명령적으로 접근할 경우 사용

  ```react
  function TextInputWithFocusButton() {
    const inputEl = useRef(null);
    const onButtonClick = () => {
      // `current` 마운트된 text input element를 가리킴
      inputEl.current.focus();
    };
    return (
      <>
        <input ref={inputEl} type="text" />
        <button onClick={onButtonClick}>Focus the input</button>
      </>
    );
  }
  ```

  위의 코드는 button을 클릭하면 input 태그에 focus하는 코드.

- `<div ref={myRef}>` 와 같이 사용하면 React는 노드가 변경될 때마다 `myRef.current` 속성에 변경된 DOM 노드를 설정.
- `ref` 속성보다 `useRef()` 가 클래스에서 인스턴스 필드를 사용하는 것과 유사하게 다양한 변수를 저장할 수 있다는 장점.
- 이는 `useRef()`가 순수 JS 객체를 생성하기 때문.
  - 그렇다면 `useRef()`를 사용하는 것과 `{current: ...}`과 같이 `current` 속성을 포함한 JS 객체를 생성하는 것 두 방식의 차이는 무엇일까
  - 차이점은 `useRef`는 매 렌더링마다 동일한 ref 객체를 제공한다는 것.

- `useRef()`는 **내부의 데이터가 변경되어도 별도로 알리지 않음.** 즉, `.current`속성이 변경되어도 재렌더링이 일어나지 않음. 따라서 DOM 노드에 ref를 연결하거나 분리될 때 어떤 코드를 실행하려면 Callback ref를 사용해야함.

### Callback ref

- callback ref는 DOM 노드의 위치나 크기를 측정하는 기본적인 방법 중 하나.

- React는 ref가 다른 노드에 연결될 때마다 해당 콜백을 호출.

- ```react
  function MeasureExample() {
    const [height, setHeight] = useState(0);
  
    const measuredRef = useCallback(node => {
      if (node !== null) {
        setHeight(node.getBoundingClientRect().height);
      }
    }, []);
  
    return (
      <>
        <h1 ref={measuredRef}>Hello, world</h1>
        <h2>The above header is {Math.round(height)}px tall</h2>
      </>
    );
  }
  ```

  -  `useRef`는 현재 `ref` 값의 변경 사항을 알려주지 않음. 이에 반해, 콜백 ref를 사용하면 자식 컴포넌트가 변경되었을때 부모 컴포넌트에서 이에 대한 알림을 받고 업데이트 가능.

  

## useReducer

```react
const [state, dispatch] = useReducer(reducer, initialArg, init);
```

- `useState`의 대체 함수.
- `(state, action) => newState`의 형태로 reducer를 받고 `dispatch` 메서드와 짝의 형태로 현재 state 반환.
- 복잡한 정적 로직 또는 다음 state가 이전 state에 의존적인 경우 선호됨.
- 콜백 대신 dispatch를 전달할 수 있기 때문에 자세한 업데이트를 트리거하는 컴포넌트의 성능을 최적화할 수 있게 함.







