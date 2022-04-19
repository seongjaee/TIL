# React 공식 문서 자습서 대충 읽어보기

https://ko.reactjs.org/docs/hello-world.html

> 코드를 쓸 일 보다 읽을 일이 더 많다.

## **JSX**

- React에서는 본질적으로 렌더링 로직이 UI 로직과 연결된다는 사실을 받아들입니다.
  - UI로직
    - 이벤트가 처리되는 방식
    - 시간에 따라 state가 변하는 방식
    - 화면에 표시하기 위해 데이터가 준비되는 방식

- 마크업과 로직을 포함하는 "컴포넌트"라는 느슨한 연결 유닛으로 **관심사 분리**

## **엘리먼트 렌더링**

**엘리먼트**

- 엘리먼트는 React 앱의 가장 작은 단위
- 화면에 표시할 내용 기술
- 일반 객체

- React DOM이 DOM을 업데이트해 React 엘리먼트와 동일하도록 함.

- 엘리먼트와 컴포넌트는 다름. 엘리먼트는 컴포넌트의 "구성 요소"

- 불변 객체, 생성 이후에는 엘리먼트의 자식이나 속성 변경 불가. 즉 특정 시점의 UI를 보여줌.

**업데이트**

- React DOM은 엘리먼트와 그 자식 엘리먼트를 이전 엘리먼트와 비교, 필요한 경우에만 DOM을 업데이트

- 매번 UI를 다시 렌더링하도록 해도 실제 변경된 엘리먼트만 재렌더링됨.

## Components와 Props

- **컴포넌트**를 통해 UI를 재사용 가능한 개별적인 여러 조각으로 나누고, 각 조각을 개별적으로 살펴볼 수 있음.

- 컴포넌트는 JavaScript 함수와 유사. 
  - "props"라는 입력을 받아
  - 화면에 어떻게 표시할지 기술하는 React 엘리먼트 반환

### 컴포넌트 추출

컴포넌트를 여러 개의 작은 컴포넌트로 나누는 것을 두려워하지 마세요.

- 컴포넌트의 구성 요소들이 중첩 구조로 이루어져 있으면 변경이 어렵고, 재사용이 어려움.
- props의 이름은 사용될 context가 아닌 컴포넌트 자체의 관점에서 짓는 것을 권장.

- 재사용 가능한 컴포넌트들을 만들어 놓는 것은 큰 앱에서 작업할 때 효율적.
- UI 일부가 자체적으로 복잡한 경우에는 별도의 컴포넌트로 만드는 게 좋음

### props는 읽기 전용

- 컴포넌트의 자체 props를 수정할 수 없음. => 순수 함수!
  - 순수 함수: 입력값을 바꾸려 하지 않고 동일한 입력값에 대해 동일한 결과를 반환.
- React의 한 가지 엄격한 규칙
  - **모든 React 컴포넌트는 자신의 props를 다룰 때 반드시 순수 함수처럼 동작해야 합니다.**



엥 UI는 동적이고 시간에 따라 변하는데, 데이터를 바꿀 수 없나요?

=> 아뇨! "state"가 있습니다.



## State와 생명 주기

- State는 props와 유사하지만, **비공개**이며 컴포넌트에 의해 **완전히 제어**됩니다.

### **생명 주기**

- 애플리케이션에 많은 컴포넌트가 있는 경우, 컴포넌트 삭제될 때 해당 컴포넌트가 사용 중이던 리소스를 확보해야함.
- **마운팅** : 컴포넌트가 처음 DOM에 렌더링 될 때
- **언마운팅** : DOM이 삭제될 때

![image-20220419213314415](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20220419213314415.png)

State 주의 사항

- **직접 State를 수정해선 안됨**
  - 직접 state를 수정하면 컴포넌트가 재랜더링 되지 않음
- **State 업데이트는 비동기적일 수 도 있음**
  - React 성능을 위해 여러 state들의 변경을 한번에 모아서 한꺼번에 업데이트 할 수 있음
  - 즉, 다음 state를 계산할 때 현재 state에 의존해선 안됨.

- **State 업데이트는 병합됨**

  - state가 여러 변수를 포함하는 경우, 하나의 변수를 수정해도 다른 변수에 영향 미치지 않음.

    

### 데이터는 아래로 흐른다

- 부모 컴포넌트가 자식 컴포넌트 모두 특정 컴포넌트가 stateful한가, stateless한가 상관할 필요 없음.

​	=> state는 로컬, 캡슐화됨. state를 소유, 설정한 컴포넌트 이외의 컴포넌트는 접근 불가

- 컴포넌트는 자신의 state를 자식 컴포넌트에 props로 전달 가능
  - 자식 컴포넌트는 이 props가 부모의 state에서 왔는지, props에서 왔는지, 직접 입력된 것인지 모름

- 트리구조가 props들의 폭포, 각 컴포넌트의 state는 임의의 점에서 만나지만 동시에 아래로 흐르는 수원(water source).

## 이벤트 처리

- React 엘리먼트에서 이벤트 처리와 DOM 엘리먼트 이벤트 처리 유사.

- React에서 기본 동작을 방지하기 위해서는 `preventDefault`를 명시적으로 호출해야함.

- 이벤트 핸들러에 인자 전달

  - ```react
    <button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
    <button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
    ```

  - 위에 둘 다 동작.

## 조건부 렌더링

- React에서는 원하는 동작을 캡슐화하는 컴포넌트를 만들 수 있음.

- ` if`나 `조건부 연산자`를 통해 조건 처리.

- JSX에서 `&&`을 이용해 쉽게 조건부 처리 가능.

  - ```react
    {unreadMessages.length > 0 &&
       <h2>
        You have {unreadMessages.length} unread messages.
       </h2>
    }
    ```

- If-Else 구문 인라인 : `condition ? true : false`

  - ```react
    <div>
      The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
    </div>
    ```

  - ```react
    <div>
      {isLoggedIn
        ? <LogoutButton onClick={this.handleLogoutClick} />
        : <LoginButton onClick={this.handleLoginClick} />
      }
    </div>
    ```

- 컴포넌트 렌더링 막으려면 `null` 반환

## 리스트와 Key

- 여러 개의 컴포넌트를 렌더링 하려면 `map()` 함수 이용.

- 반드시 항목에 key를 넣어야 함.
- 엘리먼트에 안정적인 고유성을 부여하기 위함.

## 폼

- HTML 폼 엘리먼트 자체가 내부 상태를 가지기 때문에, React의 다른 DOM 엘리먼트와 다르게 동작.
- JavaScript 함수로 폼의 제출을 처리하고 사용자가 폼에 입력한 데이터에 접근하도록 하는 것이 편리.
- 이를 위한 표준 방식 "제어 컴포넌트"

### 제어 컴포넌트

- HTML 폼 엘리먼트는 사용자의 입력을 기반으로 자신의 state를 관리
- React에서는 변경할 수 있는 state가 컴포넌트의 state 속성에 유지되며 관리.

- React state를 "신뢰 가능한 단일 출처"로 만들어 위의 두 요소를 결합.
  - 폼을 렌더링 하는 React 컴포넌트가 사용자 입력값을 제어.
  - **제어 컴포넌트** : 이렇게 React에 의해 값이 제어되는 입력 폼 엘리먼트



#### 다중 입력 제어

- 여러 `input` 엘리먼트를 제어할 때, 각 엘리먼트에 `name` 어트리뷰트를 추가하고 `event.target.name`을 통해 핸들러가 어떤 작업을 할 지 선택하게 함.

  

#### Formik

- 유효성 검사, 방문한 필드 추적 및 폼 제출 처리 등 도와줌
- 제어 컴포넌트 및 state 관리에 기초하기 때문에 쉽지는 않음.



## State 끌어올리기

- 동일한 데이터에 대한 변경사항을 여러 컴포넌트에 반영해야하는 경우가 발생. 이런 경우 가장 가까운 공통 조상으로 state를 끌어올리는 것이 좋음
- React 앱에서 변경이 일어나는 데이터에 대해서는 "진리의 원천(source of truth)"을 하나만 두어야 합니다.
- state를 끌어올리는 건 양방향 바인딩 접근 방식보다 많은 "보일러 플레이트" 코드를 유발하지만, 버그를 찾고 격리하기 더 쉽다는 장점.
- UI에서 잘못된 부분이 있다면 React Developer Tools에서 props 검사하고 state 갱신할 책임이 있는 컴포넌트를 찾을 때 까지 트리를 따라 탐색해보세요.

## 합성 vs 상속

- React에는 강력한 합성 모델이 있음. 상속 대신 합성을 사용하는 것이 좋ㅇ,ㅁ

### 컴포넌트에서 다른 컴포넌트 담기

- 어떤 자식 엘리먼트가 들어올 지 미리 예상할 수 없는 경우. 범용적인 박스 역할같은 컴포넌트.

- 이럴 때는 특수한 `children` props를 사용하여 자식 엘리먼트를 출력에 그래도 전달하는 것이 좋음.

  ```react
  function FancyBorder(props) {
    return (
      <div className={'FancyBorder FancyBorder-' + props.color}>
        {props.children}
      </div>
    );
  }
  ```

### 특수화

- 어떤 컴포넌트의 "특수한 경우"인 컴포넌트를 고려해야하는 경우.

- 더 "구제척인" 컴포넌트가 "일반적인" 컴포넌트를 렌더링하고 props를 통해 내용을 구성.

  ```react
  function Dialog(props) {
    return (
      <FancyBorder color="blue">
        <h1 className="Dialog-title">
          {props.title}
        </h1>
        <p className="Dialog-message">
          {props.message}
        </p>
      </FancyBorder>
    );
  }
  
  function WelcomeDialog() {
    return (
      <Dialog
        title="Welcome"
        message="Thank you for visiting our spacecraft!" />
    );
  }
  ```

  

## React로 생각하기

- React의 멋진 점 중 하나는 앱을 설계하는 방식.

### 1. UI를 컴포넌트 계층 구조로 나누기

- 모든 컴포넌트의 주변에 박스를 그리고 이름 붙이기.
- 어떤 것이 컴포넌트가 되어야할까?
  - 단일 책임 원칙 테크닉 : 하나의 컴포넌트는 한 가지 일을 하는게 이상적.

- 각 컴포넌트가 데이터 모델의 한 조각을 나타내도록 분리.
- 각 컴포넌트를 계층 구조로 나열.

### 2. React로 정적인 버전 만들기

- 렌더링은 되지만 아무 동작도 없는 버전 만들기.
  - 생각없이 타이핑만 많이 치면 됨.
- 재사용하는 컴포넌트를 만들고 props를 이용해 데이터 전달. 일단은 state를 쓰지 말자.
- 보통은 하향식이 쉽지만 프로젝트가 커지면 상향식으로 만들고 테스트 작성하면서 개발이 더 쉬움.

### 3. UI state에 대한 최소한의 표현 찾기

- UI 상호작용을 위해서 state가 필요.
- 변경 가능한 state의 최소 집합을 생각해보기.
- 중복 배제 원칙 : 앱이 필요로 하는 최소한의 state를 찾고 이를 통해 나머지를 그때그때 계산되도록 만들기.
- 어떤 게 state가 되어야하는가?
  1. 부모로부터 props를 통해 전달되나요? 그럼 아님.
  2. 시간이 지나도 변하지 않나요? 그럼 아님.
  3. 다른 state나 props를 통해 계산할 수 있나요? 그럼 아님.

### 4. State가 어디에 있어야할 지 찾기

- 누가 state를 변경하거나 소유할지 찾기.
- 공통 소유 컴포넌트 찾기
- 적절한 컴포넌트가 없다면 새로 공통 소유 컴포넌트를 만들기

### 5. 역방향 데이터 흐름 추가하기

- 계층 구조 하단의 컴포넌트에서 부모의 state를 업데이트 할 수 있도록 하기.