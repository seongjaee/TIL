# 함수형 프로그래밍과 JavaScript ES6+ 강의 정리

## 1. 함수형 자바스크립트 기본기

- 평가 : 코드가 계산되어 값을 만듦

- 일급 : 값으로 다룰 수 있음. 변수에 담을 수 있음. 함수의 인자로 사용 가능. 함수의 결과로 사용 가능

- 일급 함수 : 함수는 일급 객체. 조합성과 추상화의 도구

  - ```javascript
    const add10 = a => a + 10;
    
    const f1 = () => () => 1;
    console.log(f1());  // () => 1
    
    const f2 = f1();
    console.log(f2);  // () => 1
    console.log(f2());  // 1
    ```

- 고차 함수 : 함수를 값으로 다루는 함수

  - ```javascript
    // 함수를 인자로 받아서 실행
    const apply1 = f => f(1);
    const add2 = a => a + 2;
    apply1(add2);  // 3
    apply1(a => a - 1);  // 0
    
    const times = (f, n) => {
        let i = -1;
        while (++i < n) f(i);
    }
    times(a => console.log(a + 10), 3);
    // 10
    // 11
    // 12
    
    // 함수를 리턴하는 함수 (클로저를 만들어 리턴하는 함수)
    const addMaker = a => b => a + b;
    const add10 = addMaker(10);
    add10(5);  //  15
    ```

## 2. ES6에서의 순회와 이터러블:이터레이터 프로토콜

- 기존 리스트 순회

  ```javascript
  const list = [1, 2, 3];
  for (var i = 0; i < list.length; i++){
      console.log(list[i]);
  }
  ```

- 보다 **선언적**인 순회 가능

  ```javascript
  // for ... of
  for (const a of list) {
      console.log(a);
  }
  ```

- for...of의 순회 방식?

  - `Symbol.iterator`

    ```javascript
    const arr = [1, 2, 3];
    for (const a of arr) {
        console.log(a)
    }
    // 1 2 3
    console.log(arr[Symbol.iterator])  // f values() { [native code] }
    arr[Symbol.iterator] = null;
    for (const a of arr) {
        console.log(a)
    }
    // TypeError : arr is not iterable
    ```

- 이터러블 / 이터레이터 프로토콜

  - 이터러블 : 이터레이터를 리턴하는 `[Symbol.iterator]()`를 가진 값

  - 이터레이터 : `{ value, done }` 객체를 리턴하는 `next()`를 가진 값

  - 이터러블/이터레이터 프로토콜 : 이터러블을 `for...of`, 전개 연산자 등과 함께 동작하도록 규약

  - ```javascript
    const arr = [1, 2, 3];
    let iterator = arr[Symbol.iterator]();
    
    iterator.next() // {value: 1, done: false}
    iterator.next() // {value: 2, done: false}
    iterator.next() // {value: 3, done: false}
    iterator.next() // {value: undefined, done: true}
    ```

  - `for...of` 는 이터러블의 이터레이터의 next() 호출한 뒤 결과값의 value를 출력하고 있던 것

- 사용자 정의 이터러블

  ```javascript
  const iterable = {
      [Symbol.iterator]() {
          let i = 3;
          return {
              next() {
                  return i == 0 ? { done: true } : { value: i--, done: false }
              }
          }
      }
  }
  
  let iterator1 = iterable[Symbol.iterator]();
  console.log(iterator1.next());  // {value: 3, done: false}
  console.log(iterator1.next());  // {value: 2, done: false}
  console.log(iterator1.next());  // {value: 1, done: false}
  console.log(iterator1.next());  // {done: true}
  
  for (const a of iterable) {
      console.log(a);
  }
  // 3
  // 2
  // 1
  ```
  
  ```javascript
  // 잘 만들어진 이터러블은 순회를 기억함
  const arr = [1, 2, 3];
  const iter = arr[Symbol.iterator]();
  iter.next();  // {value: 1, done: false}
  
  for (const a of iter) {
      console.log(a);
  }
  // 2
  // 3
  
  console.log(iter[Symbol.iterator]() === iter)  // true
  ```

- Well-formed iterator

  - 위의 예시에서는 `iterable`이 얼마나 순회하였는지 기억하지 못함

  - 이를 해결하기 위해서는 이터러블의 `[Symbol.iterator]`를 실행했을 때 자기 자신을 반환해야함.

  - ```javascript
    // Well-formed iterator
    const iterable = {
        [Symbol.iterator]() {
            let i = 3;
            return {
                next() {
                    return i == 0 ? { done: true } : { value: i--, done: false }
                },
                [Symbol.iterator]() { return this; }
            }
        }
    }
    
    let iterator2 = iterable[Symbol.iterator]();
    console.log(iterator2.next());  // {value: 3, done: false}
    
    for (const a of iterator2) {
        console.log(a);
    }
    // 2
    // 1
    ```
    
  - 어디서든 `[Symbol.iterator]()`로 이터레이터를 만들었을 때 이전까지 진행되어있던 자신의 상태에서 순회를 진행하도록 할 수 있음

- 전개 연산자

  - 전개 연산자도 이터러블/이터레이터 프로토콜을 따름

    
