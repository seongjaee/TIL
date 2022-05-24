# 클로저

https://developer.mozilla.org/ko/docs/Web/JavaScript/Closures

**클로저**는 함수와 함수가 선언된 어휘적 환경(Lexical Environment)의 조합이다.

클로저를 이해하기 위해서 먼저 자바스크립트의 Lexical scoping을 이해해야한다.

## Lexical scoping

예시 코드

```javascript
function init() {
    var name = "철수";  // init()으로 만들어지는 로컬 변수
    function greeting() { // 내부 함수이며, 클로저
        alert(`Hello ${name}!`); // 부모 함수인 init()안에 선언된 name을 이용
    }
    greeting();    
}
init();
```

`greeting()`에는 `name`이 없지만, `name`이 잘 출력된다.

이렇게 중첩된 함수는 외부 범위(scope)에서 선언한 변수에도 접근 가능하다.

이게 lexical scoping의 예시이다. 함수가 실행되는 순간 새로운 lexical 환경이 만들어지고, 이 환경에 함수가 넘겨받은 매개변수와 로컬 변수가 저장된다.

lexical이란 lexical scoping 과정에서 변수가 어디에서 사용 가능한지 알기 위해 그 변수가 소스코드 내 어디에서 선언되었는지 고려한다는 것을 의미한다.

위의 코드가 실행되면서,

- 전역 lexical환경에 `init` 함수가 선언되고, 초기화된다.

- `init()`가 실행된다.
- 함수가 실행되면서 `init` lexical 환경이 만들어지고, 그 안에 `name`, `greeting`이 저장된다. 
- `greeting()`이 실행되고, `greeting` lexical 환경이 만들어지고, `alert` 실행을 위해 `name`을 찾아나감.
- `greeting` lexical 환경에 `name`이 없으니 외부 `init` lexical 환경에서 `name`을 찾음.



## 클로저 Closure

예시 코드

```javascript
 function makeFunc() {
    var name = "철수";
    function greeting() {
        alert(`Hello ${name}!`);
    }
    return greeting;  // 위의 예시와 다르게 함수를 실행하지 않고 반환한다
 }

var myFunc = makeFunc();
//myFunc변수에 makeFunc 리턴함
//유효범위의 어휘적 환경을 유지
myFunc();
//리턴된 greeting 함수를 실행(name 변수에 접근)
```

이전 예시와 동일한 결과가 나온다!

`myFunc`에는 `makeFunc()`의 결과 값인 `greeting`이 저장된다.

흥미로운건 `greeting()`이 '실행되기 전' 에 저장된다.

`makeFunc()` 실행이 끝나면 `name` 변수에 접근하지 못할 것으로 예상되지만, 그렇지 않다.

JavaScript는 함수를 리턴하는 함수가 클로저를 형성하기 때문이다.

클로저는 함수와 함수가 선언된 어휘적 환경의 조합이다. 이 환경은 클로저가 생성된 시점의 유효 범위 내에 있는 모든 지역 변수로 구성된다.

`myFunc`은 `makeFunc`이 실행될 때 생성된 `greeting` 함수의 인스턴스에 대한 참조다.

 `greeting` 함수의 인스턴스는 변수 `name`이 있는 어휘적 환경에 대한 참조를 유지한다.

따라서 `myFunc`이 호출될 때 `name`은 사용할 수 있는 상태다.



다른 예시

```javascript
function makeAdder(x) {
    let y = 1;
    return function(z) {
        y = 100;
        return x + y + z;
    }
}

let add3 = makeAdder(3);
let add10 = makeAdder(10);

console.log(add3(2));  // 105 (x:3 + y:100 + z:2)
console.log(add10(2));  // 112 (x:10 + y:100 + z:2)
```

`makeAdder`는 함수를 만들어내는 공장이다.

즉, `makeAdder`는 특정 값을 인자로 갖는 함수들을 리턴한다.

`add3`은 매개변수 x에 3을 더하고, `add10`은 매개변수 x에 10을 더한다.

`add3`, `add10` 둘 다 클로저다. 둘은 같은 함수 본문을 공유하지만, 다른 lexical 환경을 저장한다.

`add3`의 lexical 환경에서 x는 3이지만, `add10`의 lexical 환경에서는 10이다.

또 둘 다 y는 초기값 1에서 100으로 변경된다.

즉 클로저가 리턴된 후에도 외부함수의 변수들에 접근 가능하다는 것이며, 클로저에 단순히 값 형태로 전달되는게 아니라는 뜻이다.

`add3`의 경우를 차근차근 살펴보면,

- `makeAdder`가 선언되고 초기화된다.
- `add3` 변수가 선언된다.
- `makeAdder(3)`이 실행되면서 lexical 환경이 만들어진다. 넘겨받은 인자 x: 3, 변수 y: 1이 저장된다.
- `add3`에 익명함수 `function` 할당된다.
- `add3(2)`이 실행되면서 익명 함수 lexical 환경이 만들어진다. 넘겨받은 인자 z: 2가 저장된다.
- 익명 함수 lexical 환경에서 y값이 변경된다.
- 익명 함수 lexical 환경에서 x가 없으니 외부 `makeAdder` lexical 환경에서 x: 3을 찾는다.
- 따라서 x:3 + y:100 + z: 2 = 105



### 클로저 활용

클로저는 어떤 데이터와 그 데이터를 조작하는 함수를 연관시켜준다는 점에서 유용하다.

오직 하나의 메서드를 가지고 있는 객체를 일반적으로 사용하는 모든 곳에 클로저를 사용할 수 있다.

이런 상황은 웹에서 일반적이다. 몇 가지 동작을 정의하고 사용자에 의한 이벤트에 연결한다.

버튼을 누르면 글자의 색상과 텍스트를 토글시키는 코드를 만들어보자.

우선 클로저 없이 전역 변수를 이용해보자.

```html
<p id="colored">It's !</p>
<button id="toggle-button">Toggle</button>
```

```javascript
let currentColor = 'tomato';
const coloredP = document.getElementById("colored");

function toggleColor() {
  const nextColor = currentColor === 'tomato' ? 'forestgreen' : 'tomato';
  coloredP.innerText = `It's ${nextColor}!`;
  coloredP.style.color = nextColor;
  currentColor = nextColor;
}

document.getElementById("toggle-button").onclick = toggleColor;
```

전역 변수를 사용하면 `currentColor`의 의도치 않은 변경이 일어날 수도 있다.

클로저를 사용해서 전역 변수 없이 만들어보자.

```html
<p id="colored">It's !</p>
<button id="toggle-button">Toggle</button>
```

```javascript
const coloredP = document.getElementById("colored");

const toggleColor = (function () {
  let currentColor = "tomato";
  return () => {
    const nextColor = currentColor === "tomato" ? "forestgreen" : "tomato";
    coloredP.innerText = `It's ${nextColor}!`;
    coloredP.style.color = nextColor;
    currentColor = nextColor;
  };
})();

document.getElementById("toggle-button").onclick = toggleColor;
```





### 클로저를 이용해 private method 흉내내기

JavaScript는 프라이빗 메소드를 지원하지 않지만, 클로저를 이용해 흉내낼 수 있다.

제한적인 접근만 허용하고, 전역 네임 스페이스를 관리하는 강력한 방법을 제공하여 공용 인터페이스를 혼란스럽지 않게 할 수 있다.

아래와 같이 프라이빗 함수와 변구에 접근하는 퍼블릭 함수를 정의하기 위해 클로저를 사용하는 것을 모듈 패턴이라고 한다.

```javascript
function makeCounter() {
    let privateCounter = 0;
    function changeBy(val) {
        privateCounter += val;
    }
    
    return {
    	increment: () => { changeBy(1) },
        decrement: () => { changeBy(-1) },
        value: () => privateCounter
    }
}

let counter = makeCounter();

console.log(counter.value());  // 0
counter.increment();
counter.increment();
console.log(counter.value());  // 2
counter.decrement();
console.log(counter.value());  // 1
```

`counter.increment`, `counter.decrement`, `counter.value` 세 함수가 하나의 lexical 환경을 공유한다.

각각의 익명 함수는 정의되는 즉시 실행되면서 lexical 환경을 만든다. 그리고 이 lexical 환경은 두 개의 프라이빗 아이템을 포함하는데, `privateCounter` 변수와 `chnageBy` 함수다.

두 아이템 모두 익명 함수 외부에서는 접근할 수 없으며 익명 래퍼에서 반환된 세 개의 퍼블릭 함수를 통해서만 접근되어야한다. 세 개의 퍼블릭 함수는 같은 환경을 공유하는 클로저다.



하나의 공장 `makeCounter`로 여러 개의 카운터를 만들면 각각의 카운터는 독립성을 유지한다.

```javascript
function makeCounter() { ...생략...}

let counter1 = makeCounter();
let counter2 = makeCounter();
                        
console.log(counter1.value());  // 0
counter1.increment();
counter1.increment();
console.log(counter1.value());  // 2
                        
console.log(counter2.value());  // 0
```



### 고려사항

특정 작업에 클로저가 필요치 않은데 다른 함수 내에서 함수를 불필요하게 작성하는 것은 현명하지 않다. 처리 속도와 메모리 소비 측면에서 스크립트 성능에 부정적인 영향을 미친다.