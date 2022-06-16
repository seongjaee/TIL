# React Context API

> https://ko.reactjs.org/docs/context.html 를 정리한 내용입니다.

## React.createContext

```react
const MyContext = React.createContext(defaultValue);
```

Context 객체 생성.

React에서 렌더링이 일어날 때, Context 객체를 구독하는 하위 컴포넌트가 나오면 현재 context 값을 가장 가까운 상위 레벨의 Provider로부터 받아온다.

만약 상위 레벨에 매칭되는 Provider가 없다면 `defaultValue`를 사용한다. 따라서 기본값은 컴포넌트를 독립적으로 테스트할 때 유용하다. `defaultValue`에 `undefined`를 넣으면 기본값이 사용되지 않는다.



## Context.Provider

```react
<MyContext.Provider value={/* 어떤 값 */}>
```

`React.createContext()`로 context 객체를 만들었다면, 해당 context를 하위 컴포넌트들이 받을 수 있도록 설정해야한다. 이를 위해 사용하는 것이 `Context.Provider`이다.

React 컴포넌트인 Provider는 context를 구독하는 컴포넌트들에게 context의 변화를 알리는 역할을 한다.

`Context.Provider`로 하위 컴포넌트를 감싸주면, 모든 하위 컴포넌트들이 해당 context 데이터에 접근할 수 있게 된다. Provider 컴포넌트는 `value` prop을 받아서 하위 컴포넌트에 전달한다. Provider가 값을 전달할 수 있는 컴포넌트 수에는 제한이 없으며, Provider를 중첩해서 사용할 수도 있다. 중첩된 경우 하위 Provider의 값이 우선시된다.

Provider 하위에서 context를 구독하는 모든 컴포넌트들은 Provider의 `value` prop이 바뀔 때마다 재렌더링된다. 

이 때 상위 컴포넌트가 업데이트 대상이 아니더라도 하위 컴포넌트가 context를 사용한다면 하위 컴포넌트에서는 업데이트가 일어난다.

context 값의 변화를 판단하는 알고리즘은 JavaScript의 `Object.is` 알고리즘을 사용한다. 따라서 `value`로 객체를 전달하는 경우 **문제**가 발생할 수 있다.

### 주의사항

context를 사용하는 경우 재렌더링 여부를 참조(reference) 확인을 통해 결정하기 때문에, Provider의 부모가 렌더링될 때마다 불필요하게 하위 컴포넌트가 재렌더링이 되는 문제가 생길 수 있다.

```react
function App(props) {
    return (
      <MyContext.Provider value={{something: 'something'}}>
        <Toolbar />
      </MyContext.Provider>
    );
}
```

위의 코드는 `value`가 바뀔 때마다 매번 새로운 객체가 생성되므로 Provider가 렌더링 될 때마다 하위 컴포넌트 모두가 재렌더링된다.

이를 피하기 위해 value를 부모의 state로 끌어올릴 수 있다.

```react
function App(props) {
    const [value, setValue] = useState({ something: 'something'});
    
    return (
      <MyContext.Provider value={value}>
        <Toolbar />
      </MyContext.Provider>
    )
}
```



## Class.contextType

```react
class MyClass extends React.Component {
  componentDidMount() {
    let value = this.context;
    /* MyContext의 값을 이용한 코드 */
  }
  componentDidUpdate() {
    let value = this.context;
    /* ... */
  }
  componentWillUnmount() {
    let value = this.context;
    /* ... */
  }
  render() {
    let value = this.context;
    /* ... */
  }
}
MyClass.contextType = MyContext;
```

`MyClass.contextType = MyContext;`로 Context 객체를 원하는 클래스의 contextType 속성으로 지정할 수 있다. 클래스 컴포넌트 내에서 `this.context`를 이용해 해당 Context의 가장 가까운 Provider를 찾아 context 값을 사용할 수 있다.

이 API는 하나의 context만 구독할 수 있다. 여러 context를 구독하는 방법은 아래에 작성되어있다.



## Context.Consumer

```react
<MyContext.Consumer>
  {value => /* context 값을 이용한 렌더링 */}
</MyContext.Consumer>
```

Consumer 컴포넌트는 Context의 데이터를 구독하는 컴포넌트이다.

클래스 컴포넌트에서는 위의 Class.contextType을 이용했다면, 함수형 컴포넌트에서는 Consumer를 이용해 Context를 구독할 수 있다.

Context.Consumer의 자식은 함수(function as a child)여야한다. 함수를 Consumer로 감싸면 해당 함수는 context의 현재 값을 받아 React 노드를 반환한다. 이 함수가 받는 value 매개변수 값은 Provider value prop과 동일하다. 만약 상위 Provider가 없다면 `defaultValue`와 동일하다.



### function as child

```react
// children이라는 prop를 직접 선언하는 방식
<Profile children={name => <p>이름: {name}</p>} />

// Profile컴포넌트로 감싸서 children으로 만드는 방식
<Profile>{name => <p>이름: {name}</p>}</Profile>
```



## Context.displayName

Context 객체는 `displayName` 문자열 속성을 갖는다. React 개발자 도구에서 context가 어떻게 보여질 지를 결정한다.

```react
const MyContext = React.createContext(/* some value */);
MyContext.displayName = 'MyDisplayName';

<MyContext.Provider> // "MyDisplayName.Provider" in DevTools
<MyContext.Consumer> // "MyDisplayName.Consumer" in DevTools
```



## 여러 개의 Context 사용하기

여러 개의 Context를 사용하기 위해서 Provider를 중첩해서 사용할 수 있다.

```react
// 기본값이 light인  ThemeContext
const ThemeContext = React.createContext('light');

// 로그인한 유저 정보를 담는 UserContext
const UserContext = React.createContext({
  name: 'Guest',
});

class App extends React.Component {
  render() {
    const {signedInUser, theme} = this.props;

    // context 초기값을 제공하는 App 컴포넌트
    return (
      <ThemeContext.Provider value={theme}>
        <UserContext.Provider value={signedInUser}>
          <Layout />
        </UserContext.Provider>
      </ThemeContext.Provider>
    );
  }
}

function Layout() {
  return (
    <div>
      <Sidebar />
      <Content />
    </div>
  );
}

// 여러 context의 값을 받는 컴포넌트
function Content() {
  return (
    <ThemeContext.Consumer>
      {theme => (
        <UserContext.Consumer>
          {user => (
            <ProfilePage user={user} theme={theme} />
          )}
        </UserContext.Consumer>
      )}
    </ThemeContext.Consumer>
  );
}
```

하지만 둘 이상의 context 값이 함께 쓰이는 경우가 많다면, 그 값들을 한 번에 받는 render prop 컴포넌트를 만드는 것을 고려하자.



## useContext()

함수 컴포넌트에서 context를 사용하기 위해 Consumer로 감싸는 방법도 있지만, Hook을 이용하는 방법도 있다.

```react
function MyComponent(props) {
    const value = useContext(MyContext);
    
    return (
    	...
    )
}
```

useContext로 전달하는 인자는 context 객체 그 자체여야한다.

useContext를 호출한 컴포넌트는 context 값이 변경되면 항상 리렌더링되므로, 비용이 많이 든다면 메모이제이션을 사용해 최적화할 수 있다.