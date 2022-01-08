# Optional chaining `?.`

> [Optional chaining - MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

`.` 체이닝 연산자와 유사하지만, 참조가 `null` 또는 `undefined`이면, 에러 발생 대신 `undefined`로 리턴.

참조가 누락될 가능성이 있는 경우 사용하면 더 짧고 간단한 표현식이 가능.

**예시**

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

