# React 비제어 컴포넌트

https://ko.reactjs.org/docs/uncontrolled-components.html를 정리한 글입니다.

- 비제어 컴포넌트는 DOM 자체에서 폼 데이터가 다루어진다.
- state 업데이트에 대한 이벤트 핸들러 대신 `ref`를 사용해 DOM에서 폼 값을 가져올 수 있다.

```react
function NameForm() {
  const input = useRef();
  const handleSubmit = (event) => {
    alert("A name was submitted: " + input.current.value);
    event.preventDefault();
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" ref={input} />
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
}
```

- 비제어 컴포넌트는 DOM에 신뢰 가능한 출처를 유지하므로, React와 non-React 코드 통합이 쉽다.
- 빠르고 간편하게 적은 코드를 작성할 수 있으나, 일반적으로는 제어 컴포넌트를 사용해야함.



---

## [제어 입력 vs 비제어 입력](https://goshacmd.com/controlled-vs-uncontrolled-inputs-react/)

- 폼을 만들 때 `state`와 `ref` 중 어느 것을 선택해야하는가? 

  폼은 결국 많은 웹 앱의 중심이다. 두 접근 방식의 차이와 언제 사용할지를 알아보자.

### 비제어

- **비제어 입력**은 전통적인 HTML 폼 입력과 같다. 사용자의 입력을 기억한다. 그리고 개발자는 그 값을 `ref`를 이용해 가져온다. 즉, 필요할 때(폼을 submit할 때 등) 필드의 값을 **pull**해야한다. 이게 폼 입력을 구현하는 가장 간단한 방법이다. 
- 하지만 그렇게 강력하지 않다.

### 제어

- **제어 입력**은 현재 값과 그 값을 변경할 콜백을 prop으로 받아들인다. 좀더 "리액트스러운 방법"이다.
- input 값이 어딘가에 state로 살아있어야한다. 일반적으로 입력을 렌더링하는 컴포넌트는 state를 저장해한다.
- 한글자 한글자를 타이핑할 때마다 콜백이 호출되고, 새로운 input 값을 state로 만든다.

- 이 흐름은 폼 컴포넌트에 값 변경을 **push**하는 것과 같다. 따라서 폼 컴포넌트는 명시적인 요청 없이, 항상 input의 현재 값을 가진다. 이 말은 데이터(state)와 UI(input)의 싱크가 항상 맞는다는 뜻이다.
- 또한 폼 컴포넌트가 input 변경을 즉시 반응함을 의미한다. 예를 들어,
  - 유효성 검사
  - 모든 필드에 유효한 데이터가 있는게 아니라면 버튼 disable로
  - 신용 카드 번호같은 특정 입력 형식 적용

- 이런 게 필요한 게 아니라면 비제어로 간단하게 사용해도 좋다.

### Element를 "제어"되게 만드는 것

- 폼 element는 value를 prop으로 받아들일때 "제어"된다.

### 결론

- 제어, 비제어 컴포넌트 모두 각자의 메리트가 있다.
- 자신의 특정 상황을 고려하고 접근 방식을 고르자.
- 폼이 UI 피드백 측면에서 정말 간단하다면 `ref`를 이용해 비제어해도 충분하다.

---



### 비제어 컴포넌트 기본값

- React 렌더링 생명주기에서 폼 엘리먼트의 `value` 속성은 DOM value를 대체한다. 비제어 컴포넌트를 사용하면 React 초깃값을 지정하지만, 그 이후의 업데이트는 제어하지 않는 것이 좋다.
- `defaultValue`를 사용하자. 컴포넌트 마운트 이후에 `defaultValue`를 변경해도 DOM의 값이 업데이트되지 않는다.



### 파일 입력 태그

- `<input type="file" />` 은 React에서 프로그래밍적으로 값을 설정할 수 없고 사용자만이 값을 설정할 수 있기 때무에 항상 비제어 컴포넌트.
- File API를 사용해 상호작용.

```react
function FileInput(props) {
  const fileInput = useRef();
  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Selected file : ${fileInput.current.files[0].name}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Upload file:
        <input type="file" ref={fileInput} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}
```

