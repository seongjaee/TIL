# React Hook

[Reactjs.org > 문서 > Hook](https://ko.reactjs.org/docs/hooks-intro.html)를 정리한 내용.

## 1. Hook

Hook은 React 16.8 버전에 새로 추가되었음

기존 Class에서만 지원되던 state 등의 기능을 함수 컴포넌트에서도 가능하게 해준다.

### **[동기](https://ko.reactjs.org/docs/hooks-intro.html#motivation)**

- 계층의 변화 없이 상태 관련 로직을 재사용할 수 있도록 도와준다.
- 생명주기 메서드를 기반으로 쪼개지 않고, 서로 비슷한 것을 하는 작은 함수의 묶음으로 컴포넌트를 나누는 방법을 사용할 수 있다.
- React 컴포넌트는 함수에 더 가까움. Class 없이 React 기능들을 사용하는 방법을 제시.



### Hook이란?

- 함수 컴포넌트에서 React state와 생명주기 기능을 연동(hook into)할 수 있게 해주는 함수. 
- class 없이 React를 사용할 수 있게 해준다. 
- 내장 hook 제공과 동시에 개발자가 직접 hook 만드는 것도 가능하다.



### Hook 사용 규칙

- 최상위에서만 Hook을 호출해야함. (반복문, 조건문, 중첩된 함수 내에서 실행 X)
- React 함수 컴포넌트 내에서만 Hook을 호출해야함



## 2. State Hook, useState

```react
const [state, setState] = useState(initialState)
```

현재의 state값과 state값을 업데이트하는 함수를 쌍으로 제공. 배열 구조 분해를 통해 할당할 수 있음.

초기값은 `this.state`와 달리 객체일 필요는 없음. 첫 번째 렌더링에만 딱 한 번 사용.

한 컴포넌트에 여러 `useState`를 사용할 수 도 있음.

```react
const [age, setAge] = useState(42);
const [fruit, setFruit] = useState('banana');
const [todos, setTodos] = useState([{ text: 'Learn Hooks' }]);
```





### **하나의 state를 써야할까? 여러 개의 state를 사용해야할까?**

반드시 여러 state 변수를 사용하지 않아도 된다. state 변수로 객체나 배열을 사용할 수도 있기 때문에 연관있는 데이터를 묶어서 사용할 수 있다. 그러나 이 경우 주의할 점이 있다.

클래스 컴포넌트의 `this.setState`과 달리, state를 갱신하는 것은 병합이 아닌 *대체*하는 것.

따라서 state가 객체, 배열 등으로 묶여있는 경우, 주의해야함.

예시 코드)

```react
const [state, setState] = useState({ left: 0, top: 0, width: 100, height: 100 });

// ...
useEffect(() => {
    // spread 연산을 통해 다른 값이 손실되지 않게 함.
    setState(state => ({...state, left: e.pageX, top: e.pageY}));
    // ...
})
// ...
```

React는 함께 변경되는 값에 따라 state를 여러 state 변수로 분할하는 것을 추천한다.

위의 state를 position과 size 객체로 분할한다.

예시 코드)

```react
const [position, setPosition] = useState({ left: 0, top: 0 });
const [size, setSize] = useState({ width: 100, height: 100 });

// ...
useEffect(() => {
    setState({ left: e.pageX, top: e.pageY });
    // ...
})
```

위와 같이 독립된 state 변수를 분리하면, 관련 로직을 커스텀 Hook으로 쉽게 추출 가능하다는 장점이 있다.



모든 state를 단일 `useState` 호출에 넣는 방식과 필드마다 `useState` 호출에 넣는 방식, 이 두 극단 사이의 균형을 찾고 **관련 state를 몇 개의 독립 state 변수로 그룹화할 때 가장 읽기 쉽다**. state 로직이 복잡해지면 Reducer로 관리하거나 커스텀 Hook을 사용하는 것이 좋다.



## 3. Effect Hook, useEffect

```react
useEffect(() => {
    // effect 함수
}, [의존성])
```

- Effect Hook을 사용하면 함수 컴포넌트에서 side effect를 수행할 수 있다.

- React에서 "**side effect**"란
  - 데이터를 가져오기
  - 구독 설정하기
  - DOM을 직접 조작하는 작업 등
  - 다른 컴포넌트에 영향을 주거나, 렌더링 과정에서 구현할 수 없는 작업.

- class의 생명주기 메서드인 `componentDidMount` 나 `componentDidUpdate`, `componentWillUnmount`와 같은 목적이지만, 하나로 통합된 것.
- 의존성 배열에 담긴 값들 중 단 하나라도 달라지면 effect를 재실행한다.
- 만약 의존성 배열이 빈 배열 `[]`이라면 마운트와 마운트 해제 시에 딱 한 번씩 실행된다.
- effect 함수의 return에 콜백 함수를 넣어, 언마운트시에 해당 콜백 함수를 호출하게 할 수 있다. 모든 effect는 정리를 위한 함수를 반환할 수 있다. effect는 렌더링마다 실행되므로, 렌더링마다 이전 렌더링에서 파생된 effect가 정리된 후에 다음 effect가 실행된다.



**useEffect가 하는 일**

React에게 컴포넌트가 렌더링 이후에 어떤 일을 수행해야하는 지를 알린다. React는 우리가 넘긴 함수(effects)를 기억했다가 *DOM 업데이트 후 호출* 한다.

매 렌더링 마다 effects를 실행한다.



**useEffect를 컴포넌트 안에서 부르는 이유**

컴포넌트 내부에 둠으로써 effect를 통해 state변수와 prop에 접근할 수 있게 된다.

Hook은 JavaScript의 클로저를 이용해 React에 한정된 API를 고안하기보다는 JavaScript가 이미 가지고 있는 방법을 이용해 문제를 해결한다.



**useEffect는 렌더링 이후에 매번 수행된다**

첫 번째 렌더링과 그 이후의 모든 업데이트에서 수행된다. React는 effect가 수행되는 시점에 이미 DOM이 업데이트 되었음을 보장한다.



**effect가 업데이트마다 실행되는 이유**

이런 디자인이 버그가 적은 컴포넌트를 만드는데 도움이 된다.

React 앱의 흔한 버그 중 하나가 `componentDidUpdate`를 제대로 다루지 않는 것이다. 친구가 온라인인지 아닌지 표시하는 컴포넌트의 예시에서, 컴포넌트가 마운트된 이후에 친구 상태를 구독하고, 컴포넌트가 언마운트될 때 구독을 해지한다고 해보자. 그럼 컴포넌트가 화면에 표시되는 동안 데이터가 변경되면 어떻게 될까. 친구가 오프라인이 되어도 컴포넌트는 계속 온라인 상태로 표시한다. 버그다. 따라서 `componentDidUpdate`로 업데이트마다 `이전 state` 의 친구들 구독을 해지하고, `새로운 state`의 친구들을 구독해야한다.

하지만 Hook을 사용하면, 애초에 업데이트마다 실행되므로 업데이트를 위한 특별한 코드가 필요 없다.



**종속성 배열에서 함수를 생략해도 되나요?**

일반적으로 아니다. effect 외부의 함수에서 어떤 props나 state가 사용되는지 기억하기 어렵다. 이것이 **effect에 필요한 함수를 effect 내부에 선언하려는 이유**다. 그래야 effect가 의존하고 있는 컴포넌트 스코프에서의 값들을 확인하기 쉽다.

만약 함수를 effect 내부로 이동할 수 없는 경우

- 함수를 컴포넌트 외부로 이동해본다.
- 함수가 순수한 계산이고 렌더링하는 동안 호출되도 된다면, effect 외부에서 호출하고 반환된 값에 따라 effect가 달라지도록 한다.
- effect 의존성 배열에 함수를 추가하되, 정의를 `useCallback` Hook에 감싸준다.



**effect 종속이 자주 변경되는 경우**

effect가 *너무 자주 변경되는 state*를 사용한다고 해서 **해당 state를 생략해선 안된다.** 일반적으로 버그가 발생한다.

```react
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1); // 이 effect는 'count' state에 따라 다릅니다
    }, 1000);
    return () => clearInterval(id);
  }, []); // 🔴 버그: `count`가 종속성으로 지정되지 않았습니다

  return <h1>{count}</h1>;
}
```



```react
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1);
    }, 1000);
    return () => clearInterval(id);
  }, [count]); // 버그 수정. but, 변경 시마다 interval이 재설정됨.

  return <h1>{count}</h1>;
}
```

종속성 배열에 `count`를 넣으면 버그가 수정되지만, 매번 interval이 재설정되어, `setTimeout`과 유사해진다. 즉 setInterval은 딱 한 번만 실행되고 지워진다.

이를 해결하기 위해 현재 state를 참조하지 않고 state를 변경하는 방법을 사용한다.

```react
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(c => c+1);
    }, 1000);
    return () => clearInterval(id);
  }, []); // effect가 컴포넌트 범위의 변수를 사용하지 않음.

  return <h1>{count}</h1>;
}
```



한 state가 다른 state를 의존하는 등의 더 복잡한 경우 useReducer Hook을 사용해 state 업데이트 로직을 effect 외부로 이동시킬 수 있다.

useReducer의 dispatch함수 컴포넌트의 정체성은 항상 안정적이다.



최후의 수단으로 `useRef`를 이용해 가변 변수를 보유할 수 있다.

```react
function Example(props) {
  // 최신 props를 ref에 보관해주세요.
  const latestProps = useRef(props);
  useEffect(() => {
    latestProps.current = props;
  });

  useEffect(() => {
    function tick() {
      // 언제든지 최신 props 읽기
      console.log(latestProps.current);
    }

    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []); // 이 effect는 다시 실행되지 않습니다
}
```

다른 더 나은 대안이 없을 때만 사용하자. mutation에 의존하면 컴포넌트가 예측하기 어려워진다.



### **effect 이용 팁**

**관심사 분리를 위해 Multiple Effect를 사용한다.**

Hook 탄생 동기 중 하나는 생명주기 메서드가 관련 있는 로직이 여러 메서드에 분리된다는 점이었다.

useEffect을 여러 번 사용하는 방법으로 이 문제를 해결할 수 있다. Hook을 이용하면 **코드가 무엇을 하는지**에 따라 나누어 관심사 분리를 이룰 수 있다.

React는 컴포넌트에 사용된 모든 effect를 지정된 순서에 맞춰 적용된다.



## 4. Hook 규칙

**Hook 사용 두 가지 규칙**

- 최상위에서만 Hook을 호출해야함. (반복문, 조건문, 중첩된 함수 내에서 실행 X)
- React 함수 컴포넌트 내에서만 Hook을 호출해야함.



한 컴포넌트에서 state나 effect hook을 여러 개 사용할 수 있는데, React는 어떻게 특정 state가 어떤 useState 호출에 해당하는지 알 수 있을까?

**React가 Hook이 호출되는 순서에 의존**하기 때문이다. 모든 렌더링에서 Hook의 호출 순서가 같기 때문에 올바르게 동작할 수 있다.

따라서 만약 조건문 내에서 Hook을 호출해, 조건에 따라 Hook이 호출될지 않을지 결정된다면, 렌더링마다 Hook 호출 순서가 달라진다.

=> **컴포넌트 최상위에서 Hook이 호출되어야하는 이유**다.

조건에 따라 effect를 실행하고 싶다면 조건문을 Hook 내부에 넣어야한다.



## 5. Custom Hook

**React의 상태 관련 로직을 컴포넌트 간 공유하는 두 가지 방법**

- `render props`
- 고차 컴포넌트

Hook을 사용해 트리에 컴포넌트를 추가하지 않고 문제를 해결할 수 있다.



**Custom Hook 추출하기**

두 개의 JS 함수에서 같은 로직을 공유하고자 한다면 또 다른 함수로 분리한다. 컴포넌트와  Hook 또한 함수이기 때문에 마찬가지로 같은 방법을 사용할 수 있다.

**Custom Hook 은 이름이 use로 시작하는 JavaScript 함수다. Custom Hook은 다른 Hook을 호출할 수 있다.**

예시 코드)

```react
function useFriendStatus(friendID) {
  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }

    ChatAPI.subscribeToFriendStatus(friendID, handleStatusChange);
    return () => {
      ChatAPI.unsubscribeFromFriendStatus(friendID, handleStatusChange);
    };
  });

  return isOnline;
}
```

기존의 로직을 복사해 `useFriendStatus` 라는 함수 안에 넣었다.

다른 Hook들은 사용자 Hook 위로 놓여야하며, Custom Hook은 조건부 함수가 아니어야 한다.

이름은 반드시 `use`로 시작해야한다.



**Custom Hook 이용하기**

Custom Hook을 추출해 사용하더라도 작동 방식에 변화는 없다. 공통 코드를 뽑아내 새로운 함수로 만든 것 뿐이다. **Custom Hook은 React의 특별한 기능이 아니라, 기본적으로 Hook의 디자인을 따르는 관습이다.**



두 개의 컴포넌트가 같은 Custom Hook을 공유하더라도, 그 안의 state와 effect는 독립적이다.

각각의 Hook에 대한 호출은 서로 독립된 state를 받는다. 각 컴포넌트에서 Custom Hook을 직접 호출하기 때문에 React의 관점에서 컴포넌트는 useState나 useEffect를 호출한 것과 다름 없다.



Custom Hook은 로직 공유의 유연성을 제공한다. 다양한 쓰임새에 적용할 수 있고, 사용하기 쉬운 Hook을 만들 수도 있다.

Custom Hook이 복잡한 로직을 단순한 인터페이스 속에 숨길 수 있도록 하거나 복잡하게 뒤엉킨 컴포넌트를 풀어내도록 돕는 경우들을 찾아내는 것을 권장한다.