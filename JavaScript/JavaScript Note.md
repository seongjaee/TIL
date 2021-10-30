# JavaScript 노트

## sort()

- `.sort()` : [Array.prototype.sort() - MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

```javascript
const arr = [3, 4, 12, 5];
arr.sort();
console.log(arr);
// [12, 3, 4, 5]
```

- 문자열 기준으로 정렬한다...
- 숫자를 정렬하고 싶다면 compare 함수를 인자로 넣자.

```javascript
const arr = [3, 4, 12, 5];
arr.sort((x, y) => x - y);
console.log(arr);
// [3, 4, 5, 12]
```

- compare(x, y) 함수는 
  - x > y 일 때 1
  - x == y 일 때 0
  - x < y 일 때 -1 

## Array() 생성

- `[0, 1, 2, 3, 4]` 같은 배열을 만들고 싶을 때,

  - ```javascript
    const arr = [...Array(5).keys()];
    ```

  - `Array(5)` 처럼 숫자를 인자로 주면 그 숫자 크기의 빈 배열을 만든다.
  - `Array.keys()` 는 배열의 인덱스들을 키값으로 갖는 새로운 Array Iterator 객체를 만들어준다.
  - `...`  spread 연산자로 Iterator를 배열 안에 넣어서 배열로 만든다.

- `[0, 0, 0, 0, 0]` 같은 배열을 만들고 싶을 때,

  - ```javascript
    const arr = Array(5).fill(0);
    ```

  - `.fill(value, start, end)` 는 배열의 start부터 end까지 value로 채워준다.

  

