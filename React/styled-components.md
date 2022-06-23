# styled-components

https://styled-components.com/docs

## 동기

- React 컴포넌트 시스템을 스타일링하기 위한 CSS를 개선하기 위한 방법!
- single use case에 집중해, **개발자 경험**과 최종 **사용자를 위한 아웃풋**을 최적화했다.

- styled-components가 제공하는 것들
  - **Automatic critical CSS** : 어떤 컴포넌트가 페이지에 렌더링되는지 추적하고, 스타일을 완전히 자동으로 주입한다. 이는 코드 분할과 결합했을 때 **사용자가 최소한의 코드를 로드하게 됨**을 의미한다.
  - **No class name bugs**: 스타일에 대한 클래스명을 고유하게 생성한다. 복제, 중복, 오타를 걱정할 필요 없다.
  - **Easier deletion of CSS**: 기존의 경우, 클래스명이 코드 어디에 사용되는지 여부를 알기 어렵다. styled-components는 모든 스타일링이 특정 컴포넌트에 묶여있기 때문에 이를 명확히 한다. 컴포넌트가 사용되지 않고 삭제된다면, 컴포넌트의 스타일도 함께 삭제된다.
  - **Simple dynamic styling**: 컴포넌트의 스타일을 컴포넌트의 props나 글로벌 테마를 기반으로 조정하기 때문에 간단하고 직관적이다. 여러 클래스를 수동으로 관리할 필요없다. 
  - **Painless maintenance**: 컴포넌트에 영향을 미치는 스타일을 찾기 위해 여러 파일을 뒤질 필요 없다. 코드베이스가 얼마나 크든 유지 보수가 쉽다.
  - **Automatic vendor prefixing**
    - [Vendor prefix - MDN Web Docs Glossary](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix)
- CSS를 개별 컴포넌트와 결합하면서도 CSS의 모든 이점을 얻을 수 있다.

## 사용

- styled-components는 기본적으로 [Tagged template literal](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)을 이용한다.
- 컴포넌트와 스타일 간의 매핑을 제거한다. 즉, 스타일을 정의할 때 스타일이 입혀진 실제 React 컴포넌트를 생성하게 된다.

```react
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;
```

### props 기반 적용

- styled-components의 템플릿 리터럴에 함수를 넘겨서 컴포넌트의 props에 기반으로 스타일 적용이 가능하다.

```react
const Button = styled.button`
  background: ${props => props.primary ? "palevioletred" : "white"};
  color: ${props => props.primary ? "white" : "palevioletred"};

  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

...
<Button>Normal</Button>
<Button primary>Primary</Button>Button>
```



### 스타일 확장

- 어떤 컴포넌트의 스타일을 상속받아 새로운 컴포넌트를 만드는 손쉬운 방법: `styled()` 함수로 감싼다.

```react
const Button = styled.button`
  color: palevioletred;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

// Button을 기반으로 스타일을 상속받은 새로운 컴포넌트
const TomatoButton = styled(Button)`
  color: tomato;
  border-color: tomato;
`;
```

- 가끔 styled-component 렌더링 시에 태그를 변경하고 싶을 수 있다. 예를 들어, 네비게이션 바에 a태그와 button이 섞여 있지만, 모두 동일한 스타일을 가져야할 때. 이럴 때를 위한 탈출구가 있다.
- `as` polymorphic prop을 사용해, 동적으로 스타일을 받는 엘리먼트를 수정할 수 있다. 

```react
const Button = styled.button`
  color: palevioletred;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;


// 위의 Button에서 작성한 스타일을 a 태그로 사용
<Button as="a" href="#">Link with Button styles</Button>
```



### 어떤 컴포넌트든 스타일링

- 전달된 `className` props을 DOM 엘리먼트에 연결하는 한, `styled` 메서드는 커스텀 컴포넌트 또는 서드파티 컴포넌트 모두 완벽히 작동한다.

```react
// react-router-dom의 Link 컴포넌트 예시
const Link = ({ className, children }) => (
  <a className={className}>
    {children}
  </a>
);

const StyledLink = styled(Link)`
  color: palevioletred;
  font-weight: bold;
`;

render(
  <div>
    <Link>Unstyled, boring Link</Link>
    <br />
    <StyledLink>Styled, exciting Link</StyledLink>
  </div>
);
```



### 전달받은 props

- 스타일링하려는 대상이 단순 엘리먼트라면( ex.`styled.div`)  알려진 HTML 속성을 DOM으로 넘긴다
- 스타일링하려는 대상이 커스텀 React 컴포넌트라면(ex. `styled(MyComponent)`), 모든 props를 넘긴다.

```react
const Input = styled.input`
  padding: 0.5em;
  margin: 0.5em;
  color: ${props => props.inputColor || "palevioletred"};
  background: papayawhip;
  border: none;
  border-radius: 3px;
`;

<div>
    <Input defaultValue="@probablyup" type="text" />
    <Input defaultValue="@geelen" type="text" inputColor="rebeccapurple" />
</div>
```

- `type`, `defaultValue` 은 DOM으로 넘겨지지만,  `inputColor` prop은 DOM으로 넘겨지지 않는다. styled-components가 non-standard 속성을 자동으로 필터링한다.





## styled-components 장단점 정리

### **장점**

- CSS 모델을 문서 레벨이 아닌 컴포넌트 레벨로 추상화하는 모듈성
- CSS-in-JS는 JavaScript 환경을 최대한 활용
- JavaScript와 CSS 사이의 상수와 함수를 공유
- 현재 사용중인 스타일만 DOM에 포함
- 짧은 길이의 고유한 클래스를 자동으로 생성하는 코드 경량화

### **단점**

- 러닝 커브
- 새로운 의존성 발생
- 별도 라이브러리 설치에 따른 번들 크기 증가
- CSS-in-CSS에 비해 느린 속도



## Inline-style vs styled-components

React에서 인라인 스타일을 사용하는 코드와 styled-compoents를 사용하는 코드는 얼핏 비슷해보인다.

어떤 차이가 있을까?

> 스포일러
>
> => inline styling은 pseudo 선택자, media query 등을 사용할 수 없다.



인라인 스타일을 사용하는 코드

```react
const style = {
    background: 'tomato',
    color: 'white'
}

<div style={style}>Hello World</div>
```



styled-components를 사용하는 코드

```react
const StyledDiv = styled.div`
	background: 'tomato',
    color: 'white'
`;

<StyledDiv>Hello World</StyledDiv>
```



### 차이점

#### 1. CSS 기능

- 우선 가장 큰 차이점은 inline style의 경우 CSS의 일부만을 지원한다. pseudo 선택자, media query, nesting 등을 사용할 수 없다.
- 반면, styled-components는 className를 이용해 CSS를 컴포넌트에 연결시킨다. 즉, 아래의 코드에서는 실제 CSS가 생성되기 때문에 pseudo 선택자, media query 등을 모두 사용할 수 있다.

#### 2. 확장성

- inline style을 사용하면 재사용성이 떨어지기 때문에 확장성이 떨어진다. 장기적으로 생각했을 때 탄력적인 애플리케이션을 만들기 어렵다.



## 참고 문서

- [Basics - styled-components](https://styled-components.com/docs/basics)
- [삼성 SDS - 인사이트 - 웹 컴포넌트 스타일링 관리 CSS-in-JS vs CSS-in-CSS](https://www.samsungsds.com/kr/insights/web_component.html)
- https://blog.logrocket.com/why-you-shouldnt-use-inline-styling-in-production-react-apps/
- https://mxstbr.blog/2016/11/inline-styles-vs-css-in-js/

- https://stackoverflow.com/questions/60596518/what-is-the-actual-difference-between-using-an-inline-style-and-using-a-css-in-j