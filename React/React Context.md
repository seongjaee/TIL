# React Context

>  https://ko.reactjs.org/docs/context.html 를 정리한 내용입니다.

## 왜 Context를 사용해야할까

일반적인 React 애플리케이션에서 데이터는 부모에서 자식으로, 컴포넌트의 props를 통해 전달된다.

하지만 여러 컴포넌트에서 자주 사용되는 데이터의 경우 이 과정이 번거로울 수 있다.

context를 이용하면 트리 단계마다 명시적으로 props를 넘겨주지 않아도 컴포넌트 트리 전체에 데이터를 제공할 수 있다. 코드가 깔끔해지고 데이터를 한 곳에서 관리하기 때문에 디버깅이 쉬워진다는 장점이 있다.

## 언제 Context를 사용해야 할까?

전역적으로, 여러 컴포넌트들이 사용하는 데이터에 사용하면 좋다. 이러한 데이터로 "로그인 여부, 로그인 정보, UI 테마, 현재 선택된 언어" 등이 있다.

예시 코드)

```react
const ThemeContext = React.createContext('light');

class App extends React.Component {
  render() {
    return (
      <ThemeContext.Provider value="dark">
        <Toolbar />
      </ThemeContext.Provider>
    );
  }
}

function Toolbar() {
  return (
    <div>
      <ThemedButton />
    </div>
  );
}

class ThemedButton extends React.Component {
  static contextType = ThemeContext;
  render() {
    return <Button theme={this.context} />;
  }
}
```



## Context를 사용하기 전에 고려할 것

Context는 다양한 레벨에 위치한 많은 컴포넌트에 데이터를 전달하기 위해 사용한다. Context를 사용하면 컴포넌트를 재사용하기 어려워진다는 단점이 있다.

여러 레벨에 걸쳐 props 넘기는 데에 **context보다 컴포넌트 합성**이 더 간단할 수 있다.

```react
<Page user={user} avatarSize={avatarSize} />
// ... 그 아래에 ...
<PageLayout user={user} avatarSize={avatarSize} />
// ... 그 아래에 ...
<NavigationBar user={user} avatarSize={avatarSize} />
// ... 그 아래에 ...
<Link href={user.permalink}>
  <Avatar user={user} size={avatarSize} />
</Link>
```

user와 avatarSize 데이터를 실제 사용하는 곳은 `Avatar` 컴포넌트 뿐이지만, props를 통해 여러 레벨에 걸쳐 넘겨주어야 하는게 번거롭다.

대신 **`Avatar` 컴포넌트 자체를 넘겨주면**(컴포넌트 합성) context 사용 없이 이를 해결할 수 있다.

```react
function Page(props) {
  const user = props.user;
  const userLink = (
    <Link href={user.permalink}>
      <Avatar user={user} size={props.avatarSize} />
    </Link>
  );
  return <PageLayout userLink={userLink} />;
}

// 이제 이렇게 쓸 수 있습니다.
<Page user={user} avatarSize={avatarSize} />
// ... 그 아래에 ...
<PageLayout userLink={...} />
// ... 그 아래에 ...
<NavigationBar userLink={...} />
// ... 그 아래에 ...
{props.userLink}
```

이런 식으로 user와 avatarSize props를 중간 레벨 컴포넌트에게 보여주지 않을 수 있다.

이런 *제어의 역전(inversion of control)* 을 이용하면 넘겨줘야 할 props의 수는 줄고 최상위 컴포넌트의 제어력은 더 커지기 때문에 더 깔끔한 코드를 쓸 수 있다.

하지만 복잡한 로직을 상위로 옮기면 상위 컴포넌트들은 더 난해해지고, 하위 컴포넌트들은 너무 유연해진다.



하위 컴포넌트를 여러 개의 변수로 나누어 전달할 수 도 있다.

```react
function Page(props) {
  const user = props.user;
    
  const topBar = (
    <NavigationBar>
      <Link href={user.permalink}>
        <Avatar user={user} size={props.avatarSize} />
      </Link>
    </NavigationBar>
  );
  const content = <Feed user={user} />;
    
  return (
    <PageLayout
      topBar={topBar}
      content={content}
    />
  );
}
```

하위 컴포넌트를 topBar와 content로 분리해 전달했다.

이 패턴은 하위 컴포넌트의 의존성을 부모 컴포넌트와 분리해야 하는 대부분의 경우에 적합하다. 또 자식 컴포넌트가 렌더링 전에 부모 컴포넌트와 소통해야하는 경우에 `render props`를 사용해 처리할 수도 있다.

하지만 하나의 데이터에 여러 레벨의 많은 컴포넌트들이 접근해야할 때도 있다. 그럴 때에는 이런 방식이 아니라 context를 사용해야한다. context는 데이터가 변경될 때마다 모든 하위 컴포넌트들에게 broadcast해주기 때문이다. context를 사용해야하는 대표적인 예시로 "지역 정보, 테마, 데이터 캐시" 등이 있다.