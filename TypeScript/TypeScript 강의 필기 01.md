# TypeScript 강의 필기 01

## 01. 타입스크립트를 쓰는 이유

브라우저는 TypeScript를 이해하지 못함. JavaScript로 변환해서 로드해야 실행 가능.

그럼에도 TypeScript를 사용하는 이유는?

### JavaScript의 문제점

```javascript
// JavaScript

function add(num1, num2) {
    console.log(num1 + num2);
}

add();  // NaN
add(1);  // NaN
add(1, 2);  // 3
add(3, 4, 5);  // 7
add('hello', 'world')  // "helloworld"
```

함수가 실행되고 에러가 발생하지 않음.

함수를 만든 개발자가 원하는 사용 방식이 아님.

함수를 사용하는 개발자가 원하는 결과가 아님.

=> 실수가 분명함에도 에러가 발생하지 않아 버그를 발견하기 어려움

```javascript
// JavaScript

function showItems(arr){
    arr.forEach((item) => {
        console.log(item);
    })
}

showItems([1, 2, 3]);  // ok!
showItems(1, 2, 3);    // TypeError
```

JavaScript는 동적언어.

- 런타임에 타입 결정 / 오류 발견
- 개발자의 실수를 사용자가 고스란히 발견

Java, TypeScript는 정적언어.

- 컴파일 타임에 타입 결정 / 오류 발견
- 초기 개발 시간이 걸리더라도 안정적인 코드 작성 가능

```typescript
// TypeScript

// 함수 인자에 타입을 명시해야함.
function add(num1:number, num2:number) {
    console.log(num1 + num2);
}

// 함수에 정의된 인자 개수보다 많거나 적은 인자를 넘기면 에러
// 함수에 정의된 인자 타입과 다른 인자를 넘기면 에러
add(1, 2);  // 3
```



```typescript
// TypeScript

function showItems(arr:string[]){
    arr.forEach((item) => {
        console.log(item);
    })
}

showItems([1, 2, 3]);
```

다른 개발자가 작성한 함수를 사용할 때에도 어떤 인자를 넘겨야하는지 일일히 코드를 확인해볼 필요가 없음.

사전에 에러를 방지할 수 있음.

