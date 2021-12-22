# React Tutorial

### [React](https://ko.reactjs.org/)

- 사용자 인터페이스를 만들기 위한 JavaScript 라이브러리
- 국내에서는 Angular나 Vue.js보다 많이 사용됨. 대부분의 개발 회사에서 FE개발에 React를 선택
- 선언형
  - 상호작용 UI 만들기 쉬워짐.
  - 애플리케이션의 각 state에 대한 간단한 뷰만 설계하면, 데이터가 변경됨에 따라 적절한 컴포넌트만 효율적으로 갱신, 렌더링
  - 선언형 뷰는 코드가 어떻게 동작할지 예상하기 쉽고 디버깅하기 쉬움.
- 컴포넌트 베이스
  - 캡슐화된 컴포넌트가 스스로 자신의 상태를 관리,
  - 컴포넌트 로직은 JS로 작성.
  - 다양한 형식의 데이터를 앱 안에서 전달.
  - DOM과 별개로 state를 관리
- 한 번 배워서 어디서나 사용
  - 기존 코드를 다시 작성하지 않고도 React의 새로운 기능을 이용해 개발 가능

#### JSX

- JS를 확장한 문법. React element 생성.
- React에서는 렌더링 로직이 UI로직
  - 이벤트 처리 방식, 시간에 따라 state가 변하는 방식, 데이터가 준비되는 방식
- React는 마크업과 로직을 각각의 파일에 넣어 기술을 인위적으로 분리하는 대신, 둘 다 포함하는 컴포넌트로 느슨하게 연결해 `separates concerns`한다.
  - [separates concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)
    - 관심사 분리. 관심사란 프로그램 코드에 영향을 미치는 정보의 집합.
    - 잘 정의된 인터페이스가 있는 코드 부분 안에 정보를 캡슐화시킴
    - 프로그램 설계, 배포, 이용, 코드 단순화 및 유지보수 등 일부 관점에서 높은 자유도가 생김.

##### JSX 사용

- JSX 중괄호 안에 JS 표현식을 넣는다.

- 가독성을 위해 JSX를 여러 줄로 나눌 땐 괄호로 묶자.

- JSX도 표현식이다. 컴파일이 끝나면 JSX 표현식이 보통의 JS 함수 호출이 되고 JS 객체로 평가됨.

- JSX 속성

  - `const element = <div tabIndex="0"></div> `  : 문자열 리터럴 삽입
  - `const element = <img src={user.avatarUrl}></img>;`  : 중괄호로 JS 표현식 삽입

- JSX 자식 정의 가능

  - ```react
    const element = (
      <div>
        <h1>Hello!</h1>
        <h2>Good to see you here.</h2>
      </div>
    );
    ```

- JSX는 Injection Attack을 방지

  - user input을 JSX에 넣는 것도 안전.
  - React DOM은 JSX의 값들을 렌더링하기 전에 escape 함. 명시적으로 적히지 않은건 주입할 수 없음
  - 렌더링 되기 전에 전부 문자열로 변환됨. XSS 공격을 막아줌

#### 엘리먼트 렌더링

- Element : React 앱의 가장 작은 단위
- React Element는 DOM Element와 달리 일반객체

- React 앱에는 일반적으로 하나의 루트 DOM 노드가 있음.
- React element를 루트 DOM 노드에 렌더링 하려면 `ReactDOM.render(element, document.getElementById('root'))`로 둘 다 전달
- React element는 불변객체 : Immutable object => 자식이나 속성을 변경할 수 없음. 즉 특정 시점의 UI를 보여줌. 지금까지 내용으로 생각해보면 UI를 업데이트하는 유일한 방법은 새로운 엘리먼트 생성 후 `ReactDOM.render()`로 전달.
  - 하지만 실제 대부분 React 앱은 `ReactDOM.render()`를 한 번만 호출

#### Components와 Props

- 컴포넌트는 JS 함수와 유사. props라는 임의의 입력을 받아 화면에 어떻게 표시할지 React element를 반환

- 함수 컴포넌트

  - ```React
    function Welcome(props) {
      return <h1>Hello, {props.name}</h1>;
    }
    ```

- 클래스 컴포넌트

  - ```react
    class Welcome extends React.Component {
      render() {
        return <h1>Hello, {this.props.name}</h1>;
      }
    }
    ```

- React 엘리먼트는 사용자 정의 컴포넌트로 나타낼 수 있음

  `const element = <Welcome name="Sara" />;`

- React가 사용자 정의 컴포넌트로 작성한 엘리먼트를 발견하면, JSX 속성과 자식을 해당 컴포넌트에 단일 객체로 전달. 이 객체가 **props**

- 렌더링 예시

  ```react
  function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
  }
  
  const element = <Welcome name="Sara" />;
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
  ```

  1. `<Welcome name="Sara" />` 엘리먼트로 `ReactDOM.render()`를 호출
  2. React는 `{name: 'Sara'}`를 props로 하여 `Welcome` 컴포넌트를 호출
  3. `Welcome` 컴포넌트는 결과적으로 `<h1>Hello, Sara</h1>` 엘리먼트를 반환
  4. React DOM은 `<h1>Hello, Sara</h1>` 엘리먼트와 일치하도록 DOM을 효율적으로 업데이트

- 컴포넌트는 자신의 출력에 다른 컴포넌트 참조 가능. React 앱에서는 버튼, 폼, 화면 등 모든 게 컴포넌트로 표현

- 컴포넌트 추출 : 구성요소들을 컴포넌트로 만들어 단순한 구조를 갖게 하자. 재사용성을 높이자.

- props는 읽기 전용. **모든 React 컴포넌트는 자신의 props를 다룰 때 반드시 순수 함수 처럼 동작해야함!**

  - 자신의 props의 값을 바꾸려고 하면 안됨

#### State and Lifecycle

- **State**는 props와 유사하지만, 비공개이며 컴포넌트에 의해 완전히 제어됨.

- 함수에서 클래스 컴포넌트로 변환 과정
  1. `React.Component`를 확장하는 클래스 생성
  2. `render()` 메서드 추가
  3. 함수 내용은 `render()` 메서드 안에 작성
  4. `render()` 안의 `props` 를 `this.props`로 변경

- **Lifcycle**

  - 마운팅 : 컴포넌트가 처음 DOM에 렌더링될 때
  - 언마운팅 : 컴포넌트에 의해 생성된 DOM이 삭제될 때
  - `componentDidMount()` : 컴포넌트가 DOM에 렌더링 된 후에 실행
  - `componentWillUnmount()` : 컴포넌트가 DOM에서 삭제될때 실행

- 시계 예시 코드

  ```react
  class Clock extends React.Component {
    constructor(props) {
      super(props);
      this.state = {date: new Date()};
    }
    
    componentDidMount() {
      this.timerID = setInterval(
        () => this.tick(),
        1000
      );
    }
    
    componenetWillUnmount() {
      clearInterval(this.timerID);
    }
    
    tick() {
      this.setState({
        date: new Date()
      });
    }
    
    render() {
      return (
        <div>
          <h1>Hello, world!</h1>
          <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
        </div>
      )
    }
  }
  
  ReactDOM.render(
    <Clock />,
    document.getElementById('root')
  );
  ```

  **동작 과정**

  1. `<Clock />`이 `ReactDOM.render()`에 들어가면, `Clock` 컴포넌트 찾아서 호출. `Clock`이 초기화되면서 `this.state`에 현재 시각을 지닌 객체가 생성됨.
  2. `Clock` 컴포넌트의 `render()` 메서드 호출. React가 `Clock` render output에 따라 DOM을 업데이트
  3. 이때, `componentDidMount()` lifecycle 메서드 호출, `Clock` 컴포넌트가 `tick()` 메서드를 1000ms 마다 호출해달라고 브라우저에게 요청.
  4. 브라우저가 매초 `tick()`메서드를 호출, `Clock`의 state를 변경하는 `setState()`함수를 호출해 UI가 업데이트 됨. React는 state의 변경을 감지하고, `render()` 메서드 다시 호출. `render()` 메서드 안의 `this.state.date`가 달라지고 render output에 업데이트된 시각이 포함됨. 이에 따라 React가 DOM을 업데이트
  5. 만약 `Clock` 컴포넌트가 DOM에서 삭제되면, React가 `componentWillUnmout()` lifecycle 메서드 호출, 타이머 멈춤.

- `setState()` 에 대한 세 가지 주의 사항

  - **Do Not Modify State Directly**. state 직접 변경 금지

    - `this.state.comment = 'Hello';` 안됨!
    - `this.setState({comment: 'Hello'});` 이렇게 해야함

  - **State Updates May Be Asynchronous**. state 업데이트는 비동기적일 수 있음

    - React는 여러 `setState()`를 하나의 업데이트로 한번에 처리할 수 있음

    - `this.props`와 `this.state`가 비동기적으로 업데이트될 수 있기 때문에 다음 state를 계산하는데 이런 값에 의존하면 안됨

    - ```react
      // Wrong
      this.setState({
          counter: this.state.counter + this.props.increment,
      });
      ```

    - 고치는 법 : `setState()` 가 객체가 아닌 함수를 인자로 받도록 함. 함수는 이전 state와 업데이트된 props를 인자로 받게됨.

      ```react
      // Correct
      this.setState((state, props) => ({
        counter: state.counter + props.increment
      }));
      ```

  - **State Updates are Merged**. state 업데이트는 병합됨.

    - `setState()`를 호출하면, React는 제공받은 객체를 현재 state로 병합.

    - 예시, state가 다양한 독립적 변수를 포함하는 경우,

      ```react
       constructor(props) {
          super(props);
          this.state = {
            posts: [],
            comments: []
          };
        }
      ```

      `this.setState({posts: response.posts});`한다고 해서 `comments`가 사라지는건 아님.

- **데이터는 아래로 흐른다.**

  - 부모 컴포넌트나 자식 컴포넌트 모두 특정 컴포넌트가 statefull한지 stateless한지 알 수없음. 그리고 함수인지 클래스인지도 상관하지 않음.
  - 이게 state가 local 또는 캡슐화라고 불리는 이유. state는 소유한 컴포넌트를 제외하고는 접근할 수 없음.
  - 자신의 state를 자식 컴포넌트에 props으로 전달가능 -> 하향식(top-down), 단방향식(unidirectional) 데이터 흐름.
  - 모든 state는 항상 특정 컴포넌트의 소유이며, state에서 파생된 UI나 데이터는 자신의 아래 방향의 컴포넌트에만 영향을 미침.
  - 트리구조가 props들의 폭포, 각 컴포넌트의 state는 임의의 점에서 만나지만, 동시에 아래로 흐르는 부가적은 수원.

#### 이벤트 처리하기

- React 이벤트는 camelCase로 사용.
- JSX를 사용하여 함수로 이벤트 핸들러 전달

- `<button onClick={activateLasers}>Activate Lasers</button>` 이런식
- `preventDefault` 호출로 기본 동작 방지
- 콜백에서 `this`가 작동하려면 3가지 방법
  - 생성자 안에서 바인딩
  - 클래스 필드 문법
  - 콜백에 화살표 함수 사용
    - 콜백이 props로 전달되는 경우 성능 문제 발생

#### 조건부 렌더링

- `if` 나 `조건부 연산자`를 이용해서 렌더링
- 엘리먼트를 변수에 저장해 조건부로 다른 엘리먼트를 사용할 수 있음
- `<조건문> && element` 으로 조건문이 true면 뒤의 element 출력. 한 줄로 가능!
- `null` 반환으로 컴포넌트를 숨길 수 있음. `null` 반환 `render` 메서드는 라이프사이클에 영향 없음

#### 리스트와 Key

- `map`을 이용해 element 배열을 만들 수 있음

- 이 때 `map()` 안에서 리스트의 각 항목에 `key`를 할당해야함.

- key는 React가 항목 식별하는 데 사용, 안정적 고유성을 위해 배열 내부 엘리먼트에 key를 지정해야함.

- 대부분 데이터의 id값을 key로 사용

- key는 컴포넌트로 전달되지는 않음. key와 동일한 값이 필요하다면 다른 이름의 prop으로 전달해야함.

- JSX를 사용해 `map()`을 안에 넣을 수 있다.

  ```react
  function NumberList(props) {
    const numbers = props.numbers;
    return (
      <ul>
        {numbers.map((number) =>
          <ListItem key={number.toString()}
                    value={number} />
        )}
      </ul>
    );
  }
  ```

#### 폼

- 대부분의 경우, JS 함수로 폼의 제출을 처리하고, 폼에 입력한 데이터에 접근하도록 하는 게 편리
- 이를 위한 표준 방식은 "제어 컴포넌트" 기술 이용
- 제어 컴포넌트
  - React에 의해 값이 제어되는 입력 폼 엘리먼트

- 유효성 검사, 방문한 필드 추척, 폼 제출 처리 같은 완벽한 해결책은 일반적으로 Formik.

#### State 끌어올리기

- 동일한 데이터에 대한 변경사항을 여러 컴포넌트에 반영해야 할 때가 있음. 이럴 때 가장 가까운 공통 조상을 찾아 조상에게 state를 끌어올리는 게 좋음.
- 자식에게 state로 있던 걸 부모의 state로 만들고, 자식 컴포넌트는 부모에게 props를 받아 사용한다. 만약 자식 컴포넌트가 해당 데이터를 변경하고 싶은 경우, 부모에게 state를 변경하는 메서드를 props 받는다.

- 교훈
  - React 앱안에서 변경이 일어나는 데이터는 "진리의 원천(source of truth)"를 하나만 두어야 함.
  - 보통 state는 렌더링에 필요로 하는 컴포넌트에 먼저 추가. 그리고 다른 컴포넌트도 그 값이 필요해지면, 그 둘의 가장 가까운 공통 조상으로 끌어올림. 하향식 데이터 흐름에 기대자!
  - 보일러 플레이트 코드
    - 최소한의 변경으로 여러 곳에서 재사용되고, 반복적으로 비슷한 코드

#### 합성 vs 상속

- React는 강력한 합성 모델을 갖고 있으며, 상속 대신 합성을 사용하여 재사용하는 게 좋음

- 컴포넌트에 다른 컴포넌트 담기 : `children` prop을 사용해 자식 엘리먼트를 그래도 출력하기

  ```react
  function FancyBorder(props) {
    return (
      <div className={'FancyBorder FancyBorder-' + props.color}>
        {props.children}
      </div>
    );
  }
  
  function WelcomeDialog() {
    return (
      <FancyBorder color="blue">
        <h1 className="Dialog-title">
          Welcome
        </h1>
        <p className="Dialog-message">
          Thank you for visiting our spacecraft!
        </p>
      </FancyBorder>
    );
  }
  ```

- 컴포넌트에 여러 개의 자식이 들어올 것으로 예상된다면 `children` 대신 자신만의 고유한 방식을 적용할 수도.

- 어떤 컴포넌트의 "특수한 경우"인 컴포넌트를 고려해야하는 경우.
  - 구체적인 컴포넌트가 일반적인 컴포넌트를 렌더링하고 props를 통해 내용 구성

- 웬만하면 props와 합성으로 만들 수 있음. UI가 아닌 기능을 여러 컴포넌트에서 재사용하길 원하면 별도의 JS 모듈로 분리하는 게 좋음.

#### React로 사고하기

- React는 JS로 큰 규모의 빠른 웹 애플리케이션을 만드는 가장 좋은 방법.

- 목업으로 시작하기
- UI를 컴포넌트 계층 구조로 나누기
  - 무엇을 컴포넌트로 만들어야할까? -> 단일 책임 원칙. 하나의 컴포넌트가 한 가지의 일을 한다.
  - UI는 데이터모델이 같은 인포메이션 아키텍처를 가지는 경향이 있음. 각 컴포넌트가 데이터 모델의 한 조각이 되도록 분리
  - 컴포넌트를 확인했다면 이를 계층 구조로 나열하자
- React로 정적인 버전 만들기
  - 우선 데이터 모델을 가지고 렌더링은 되지만 동작이 없는 버전을 만든다.
  - 정적인 버전이므로 state없이 props만 가지고 만들 수 있다.
  - 간단한 예시는 하향식이 쉽지만 큰 규모의 프로젝트는 상향식으로 만들면서 테스트 작성하면서 개발이 더 쉽다.

- UI state에 대한 최소한의(하지만 완전한) 표현 찾아내기
  - UI를 상호작용하게 만들려면 데이터 모델을 변경할 수있는 방법이 필요. state를 통해 변경
  - 애플리케이션이 필요로 하는 가장 최소한의 state를 찾아 이를 통해 나머지 데이터를 그때그때 계산되도록 만들어야함.
  - 어떤 데이터가 state가 되어야하나?
    1. 부모로부터 props를 통해 전달된다면 state가 아님.
    2. 시간이 지나도 변하지 않으면 state가 아님
    3. 다른 state나 props를 가지고 계산 가능하다면 state가 아님.
- state가 어디에 있어야 할 지 찾기
  - 각각의 state를 기반으로 렌더링하는 모든 컴포넌트 찾기
  - 공통 조상 컴포넌트 찾기
  - 적절한 컴포넌트가 없다면 공통 조상 컴포넌트를 추가하기
- 역방향 데이터 흐름 추가하기
  - 부모 컴포넌트가 자식 컴포넌트에게 콜백을 넘겨서 자식 컴포넌트가 state를 변경하려고 할 때마다 호출하게 함.
  - 부모 컴포넌트에서 전달된 콜백은 `setState()`를 호출하고 앱이 업데이트 됨.
- 명심할 것.
  - **코드를 쓸 일보다 읽을 일이 더 많다.**