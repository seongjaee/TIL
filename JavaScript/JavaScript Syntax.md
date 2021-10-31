# JavaScript 문법

## 01. 변수

- `let` 키워드, 변수

  ```javascript
  let a    // 선언
  a = 10   // 할당
  a = 5    // 재할당
  ```

- `const` 키워드, 상수

  - 재할당 불가능

  ```javascript
  const phone = 'Galaxy S2'  // 상수 선언, 할당
  phone = 'ZFlip'  // 재할당 에러 발생
  ```

### 블록 스코프

- JavaScript는 블록 스코프를 갖는다.

- 블록 스코프에서 선언한 `let`, `const`는 전역 스코프에서 접근 불가능
- 블록 스코프에서 변수의 생명 주기가 끝남.

- ```javascript
  let a = 1
  const b = 100
  
  if (true) {
      let a = 2
      const b = 200
  }
  console.log(a)  // 1
  console.log(b)  // 100

- `var` 키워드는 함수 스코프에서만 스코프 분리

- **호이스팅 hoisting**

  - 코드 실행전에 `var` 키워드 변수는 미리 선언됨. 할당은 나중에.

  ```javascript
  console.log(hoisted)  // undefined, 에러는 나지 않음.
  var hoisted  = 'Hi'
  ```

  - `let`, `const` 은 호이스팅 없음

  ```javascript
  console.log(lunch)    // 에러
  const lunch = '돈까스'
  
  console.log(dinner)   // 에러
  let dinner = '스파게티'



## 02. 타입과 연산

- `number` 타입
  - 정수, 실수, Infinity(1/0 등), NaN(Not a Number)
  
- `Date` 객체

  - `Date([parameters])` 로 객체 생성, 인자를 비워두면 오늘 날짜 시간으로 반영.
  - `set` 으로 값 설정, `get` 으로 값 반환,
  - `parse()` 로 날짜를 나태나는 문자열을 Date 객체로 반환.

- `string` 타입
  - 템플릿 리터럴(Template Literal)
    - '' 대신`` ` 으로 문자열을 감싸고 `${}` 안에 변수
  - `includes()` : 문자열에 특정 문자열이 포함되어있는지 boolean값 반환

- `undefined` vs `null`
  - `undefined` : 값을 알 수 없음. 선언 되었으나 할당 되지 않음.
  - `null` : 의도적으로 비워둔 값.
  - `typeof null` : `object`
  - `typeof undefined` : `undefined`

- `boolean` 타입
  - `true`
  - `false`

- 연산자

  - `+`, `-`, `*`, `/`

  - 3항 연산자, `? :`

    - `condition ? expression if true : expression if false`

    - ```javascript
      const subscribed = true
      const status = subscribed ? '구독중' : '구독취소'
      ```

      

## 03. 조건문

- `if ... else if ... else`

```javascript
const time = 'morning'

if (time === 'morning') {
    console.log('Good morining')
} else if (time === 'afternoon') {
    console.log('Good afternoon')
} else {
    console.log('Good night!')
}
```

- `switch ... case`

```javascript
const numOne = 10
const numTwo = 100
const operator = '+'

switch (operator) {
  case '+': {
    console.log(numOne + numTwo)
    break
  }
  case '-': {
    console.log(numOne - numTwo)
    break
  }
  case '*': {
    console.log(numOne * numTwo)
    break
  }
  case '/': {
    console.log(numOne / numTwo)
    break
  }
  default: {
    console.log('invalid operator')
  }
}
```



## 04. 반복문

- `while`

  ```javascript
  let i = 0
  while (i < 6) {
    console.log(i++)
  }
  ```

- `for`

  ```javascript
  for (let i=0; i<6; i+=2){
      console.log(i)
  }
  ```

- `for ... in`

  - `for ... in`은 list의 index(key)를 꺼낸다.
  - `string`으로 꺼낸다.

  ```javascript
  const chars = ['a', 'b', 'c']
  
  for (const idx in chars){
      console.log(chars[idx])
  }
  
  // output:
  // a
  // b
  // c
  ```

  ```javascript
  const myMovie = {
      title: '베놈 2: 렛 데어 비 카니지',
      releaseYear: 2021,
      actors: ['톰 하디', '우디 해럴슨'],
      genres: ['액션', 'SF', '스릴러'],
  }
  
  for (const key in myMovie) {
      console.log(myMovie[key])
  }
  
  // output:
  // 베놈 2: 렛 데어 비 카니지
  // 2021
  // ['톰 하디', '우디 해럴슨']
  // ['액션', 'SF', '스릴러']
  
  ```

  

- `for ... of`

  - `for ... of` 는 list의 value를 꺼낸다.

  ```javascript
  const chars = ['a', 'b', 'c']
  
  for (const char of chars){
      console.log(char)
  }
  
  // output:
  // a
  // b
  // c
  ```

  ```javascript
  const movies = [
    {title: '어바웃 타임'},
    {title: '굿 윌 헌팅'},
    {title: '인턴'},
  ]
  
  for (const movie of movies) {
    console.log(movie.title)
  }
  ```

  

## 05. 함수

- 함수 선언식

  ```javascript
  function isValid(password) {
      return password.length >= 8
  }
  ```

  - 함수 선언식은호이스팅이 일어남. 정의되기 전에 참조될 수 있음.

- 함수 표현식

  ```javascript
  const join = function (words, separator) {
  	let answer = words[0]
  	for (let i = 1; i < words.length; i++){
  		answer += separator + words[i]
  	}
  	return answer
  }
  
  join(['010', '1234', '5678'], '-') // 010-1234-5678
  ```

  - 표현식으로 작성하면 호이스팅 일어나지 않음. 스타일 가이드에도 표현식으로 작성하라고 되어있음.

- 함수 기본인자 설정

  ```javascript
  const makeOrder = function (menu='mocha', size='regular') {
  	return {menu: menu, size: size, }
  }
  ```

- 화살표 함수

  ```javascript
  const celsiusToFahrenheit = (celsius) => {
      const fahrenheit = celsius * 9/5 + 32 
      return fahrenheit
  }
  
  const celsiusToFahrenheit = celsius => celsius * 9/5 + 32 
  ```

  

## 06. 배열 메서드

- `push()` : 배열 뒤에 원소 추가

- `unshift()` : 배열 앞에 추가

- `indexOf()` : 배열에서 처음 발견한 요소의 인덱스 반환, 없으면 -1 반환
- `join()` : 배열을 separator를 기준으로 문자열로 합침
- `pop()` : 배열 맨 뒤에서 하나를 제거하고 제거한 요소를 반환

### 배열 helper메서드

- `array.map(function)` : 배열의 각 요소마다 function 적용한 배열 반환

- `array.filter(function)` : 배열에 각 요소마다 function 반환값이 True인 값만 남긴 밴열 반환

- `array.reduce(function (acc, elem), acc)` : acc부터 쌓아나감. function의 첫번째 인자는 쌓아가고 있는 acc, 두번째 인자는 array의 요소 elem

  - ```javascript
    const numbers = [1, 2, 3, 4]
    numbers.reduce(function (acc, number) {
        return acc + number
    }, 0)
    ```

- `array.find(function)` : 배열의 각 요소 중 function의 반환값이 True인 첫번째 요소를 반환
- `array.some(function)` : 배열의 각 요소 중 function의 반환값이 True인 요소가 하나라도 있는지 boolean값 반환, 하나의 요소라도 function의 반환값이 true면 true 반환
- `array.every(function)` : 배열의 모든 요소의 function 반환값이 True인지 boolean값 반환, 하나의 요소라도 function의 반환값이 false면 false 반환
- `array.forEach(function)` : 배열의 각 요소마다 function을 실행. 반환값 없음.



## 07. Object

- JS의 객체는 class instance로 만들어지지 않음. key, value로 이루어짐.

- 객체 속성에 `.key` 또는 `[key]`로 접근 가능

- Object 축약 문법

  - key와 value의 변수명과 값이 같을 때

  ```javascript
  const username = 'john'
  const contact = '010-1234-5678'
  
  const user = {
      username,
      contact
  }
  ```

- Destructuring

  - 객체를 key값으로 분해

  ```javascript
  const users = [
    {
      name: 'hailey',
      contact: '010-1234-5678',
    },
    {
      name: 'paul',
      contact: '010-5678-1234',
    },
  ]
  
  // users의 객체를 name, contact로 분해
  const userData = users.map(({ name, contact }, index) => {
    return { id: index, name: name, contact: contact }
  })
  
  // Moreover, 축약 문법까지 적용
  const userData = users.map(({ name, contact }, index) => {
    return { id: index, name, contact }
  })
  ```

  

