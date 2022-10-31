# Optional chaining `?.`

> [Optional chaining - MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Optional_chaining)



## Optional chaining

- `.` 체이닝 연산자와 유사하지만, 참조가 `null` 또는 `undefined`이면, 에러 발생 대신 `undefined`로 리턴.

  참조가 누락될 가능성이 있는 경우 사용하면 더 짧고 간단한 표현식이 가능.

### 사용

```javascript
obj.val?.prop
obj.val?.[expr]
obj.func?.(args)
```



### 예시

```javascript
const dinner = {
    desserts: ['tiramisu', 'carrot cake'],
    mainDishes: ['pizza', 'steak', 'pasta'],
    drinks: ['coke', 'beer']    
};


console.log(dinner.appetizer?.length);  // undefined
            
// 임시 변수 temp가 생성된다는 점을 제외하고 아래 코드와 동일
const temp = dinner.appetizer;
const appetizerCount = ((temp === null) || (temp === undefined)) ? undefined : temp.length;
```



### 왜 필요한가

- 참조나 기능이 Nullish할 수 있을 때 연결된 객체 값에 접근을 단순화
- 보장되지 않는 객체의 속성을 접근하고자 할 때 유용

	```jsx
	const nestedProp = obj.first && obj.first.second;
	```

- 위와 같이 `obj.first`가 `null`, `undefined`가 아니면 `obj.first.second`에 접근하도록 코드를 작성해 에러를 피할 수 있다. 하지만 `obj.first`가 0과 같이 Falsy한 값인 경우에도 second에 접근이 불가능하고 `obj.first`를 반환하게 된다. 따라서 체이닝이 길어지는 경우 안전하지 않다.
- 하지만 `?.` 을 이용하면 간단히 작성할 수 있다.

    ```jsx
    const nestedProp = obj.first?.second;
    ```

- 임시 변수 temp가 생성된다는 점을 제외하고 아래 코드와 동일

  ```jsx
  const temp = obj.first;
  const nestedProp = ((temp === null) || (temp === undefined)) ? undefined : temp.second;
  ```




### 주의

- Optional chaining을 선언되지 않은 루트 객체에 사용해선 안됨

    ```jsx
    undeclaredVar?.prop; // ReferenceError
    ```



### Optional chaining과 함수 호출

```javascript
const result = someInterface.customMethod?.();
```

- interface가 `null`이거나 `undefined`일 가능성이 있다면 `someInterface?.customMethod?.()` 으로 사용



### Optional chaining과 표현식

- bracket notation에 optional chaining을 사용 가능

    ```javascript
    const nestedProp = obj?.['prop' + 'Name'];
    ```

- 배열 접근 시 인덱스 유용
