# **JavaScript 비동기 함수 관리 (Promise, await async)**

https://web.dev/promises/

https://poiemaweb.com/es6-promise

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise

## **프로미스(Promise)**

- 자바스크립트의 비동기 처리 패턴 중 하나
- 기존 콜백 패턴은 콜백 헬로 인해 가독성이 나쁘고, 비동기 처리 중 발생한 에러의 처리가 어렵고, 여러 개의 비동기 처리를 한번에 처리하기 어렵다는 단점
- 프로미스는 이를 보완하며 비동기 처리 시점을 명확하게 표현할 수 있다는 장점
- Promise 객체는 비동기 작업이 마주할 미래의 완료 또는 실패, 그리고 그 결과 값을 나타냄
- 비동기 연산이 종료된 이후에 결과 값과 실패 사유를 처리하기 위한 처리기를 연결
- 비동기 메서드에서 동기 메서드처럼 값을 반환할 수 있음
- 최종 결과를 반환하는 것은 아니고, 미래의 어떤 시점에 결과를 제공하겠다는 '약속'

### **프로미스의 생성**

- Promise 생성자 함수를 통해 인스턴스화
- 생성자 함수는 콜백 함수를 인자로 받고, 이 콜백 함수는 resolve와 reject 함수를 인자로 받음

```jsx
var promise = new Promise(function(resolve, reject) {
  // do a thing, possibly async, then…

  if (/* everything turned out fine */) {
    resolve("Stuff worked!");
  }
  else {
    reject(Error("It broke"));
  }
});
```

### 프로미스의 사용

```jsx
promise.then(function(result) {
  console.log(result); // "Stuff worked!"
}, function(err) {
  console.log(err); // Error: "It broke"
});
```

- ```
  then
  ```

   은 성공을 위한 콜백과 실패를 위한 콜백 두 가지를 인수로 사용.

  - 하지만 두 번째 콜백 함수는 첫 번째 콜백 함수에서 발생한 에러를 캐치하지 못하고, 가독성이 좋지 않음.
  - `catch`를 사용하는 것이 가독성이 좋고 명확해 권장됨
  - `catch()`는 `then(undefined, func)`과 같지만, then 내부의 콜백이 실패하는 경우도 캐치할 수 있다.

### **프로미스의 상태**

- 상태
  - pending: 비동기 처리 아직 수행하지 않은 상태
  - fulfilled : 비동기 처리 성공
  - rejected : 비동기 처리 실패
  - settled : 비동기 처리 완료(성공 또는 실패)
- 각 상태의 구현
  - pending : resolve 또는 reject 함수가 아직 호출되지 않은 상태
  - fulfilled : resolve 함수 호출된 상태
  - rejected : reject 함수 호출된 상태
  - settled : resolve 또는 reject 함수 호출된 상태
- Promise 생성자 함수가 인자로 전달받은 콜백 함수가 내부에서 비동기 처리 작업 수행
- 비동기 처리 성공 시 콜백함수의 인자로 전달받은 resolve 함수 호출 ⇒ 프로미스는 fulfilled 상태가 됨
- 비동기 처리 실패 시 reject 함수 호출 ⇒ 프로미스는 rejected 상태가 됨
- resolve, reject 메소드의 인자로 비동기 처리 결과를 전달. 처리 결과는 Promise 객체 후속 처리 메소드로 전달

### 프로미스의 후속 처리 메서드

- Promise로 구현된 비동기 함수는 Promise 객체 반환. Promise로 구현된 비동기 함수를 호출하는 측에서는 Promise 객체의 후속 처리 메서드를 통해 비동기 처리 결과 또는 에러 메시지를 전달받아 처리한다. Promise 객체의 상태에 따라 후속 처리 메서드를 체이닝 방식으로 호출
- then
  - 두 개의 콜백 함수를 인자로 전달 받음. 첫 번째 콜백 함수는 성공 시 호출, 두 번째 함수는 실패 시 호출
  - Promise 반환
- catch
  - 예외(비동기 처리, then 메소드에서 발생한 에러) 발생 시 호출됨
  - Promise 반환

### 프로미스의 에러 처리

- 후속 처리는 then, catch, finally를 사용해 수행
- catch 메서드를 모든 then 메서드 호출 이후 호출하면 비동기 처리에서 발생한 에러뿐만 아니라 then 메서드 내부에서 발생한 에러까지 모두 캐치 가능

### 프로미스 체이닝

- 프로미스 후속 처리 메서드를 체이닝하여 여러 개의 프로미스를 연결하여 사용
- then 메서드가 기본적으로 Promise를 반환하므로 여러 개의 프로미스를 연결할 수 있다.
- 비동기식 처리 모델
  - 병렬적으로 태스크 수행. 태스크가 종료되지 않은 상태더라도 대기하지 않고 다음 태스크 실행
  - 자바스크립트의 대부분의 DOM 이벤트 핸들러, Timer 함수, Ajax 요청이 비동기식 처리 모델로 동작
- 비동기 코드
  - 다른 동기 코드와 달리 어떤 일이 발생했을 때, 한번 실행할 코드
  - 그렇다고 해서 다른 스레드에서 실행되는 것은 아님. 자바스크립트는 싱글 스레드 언어

### 프로미스의 정적 메서드

- `Promise.resolve()` : 인자로 전달된 값을 resolve하는 Promise 생성
- `Promise.reject()` : 인자로 전달된 값을 reject하는 Promise 생성
- `Promise.all()` : Promise의 배열을 받아 모두 성공적으로 완료될 때 처리하는 Promise 생성. 전달한 Promise와 동일한 순서로 결과 배열 반환

### 프로미스와 시퀀스

- 여러 개의 요청을 반복하고 순서대로 가져오는 방법

  - 작동하지 않는 방법

  ```jsx
  urls.forEach(function(url) {
    // Fetch chapter
    getJSON(url).then(function(chapter) {
      // and add it to the page
      addHtmlToPage(chapter.html);
    });
  })
  ```

  - forEach는 비동기를 인식하지 않으므로 다운로드되는 순서대로 챕터를 가져옴

- `Promise.resolve()` 이용

  ```jsx
  // Loop through our chapter urls
  urls.reduce(function(sequence, url) {
    // Add these actions to the end of the sequence
    return sequence.then(function() {
      return getJSON(chapterUrl);
    }).then(function(chapter) {
      addHtmlToPage(chapter.html);
    });
  }, Promise.resolve())
  ```

  - `array.reduce` 를 이용해 한번에 하나씩의 비동기 요청을 진행한다.
  - 하지만 완전히 비동기적이지 않다. 한번에 비동기 요청을 하는 게 브라우저는 더 효율적

- `Promise.all()` 이용

  ```jsx
  // Take an array of promises and wait on them all
    Promise.all(
      // Map our array of chapter urls to
      // an array of chapter json promises
      urls.map(getJSON)
    );
  ```

  - 하나씩 로드하는 것보다 빠를 수 있고 코드도 적다. 또 비동기 처리 완료 순서가 다를 수 있으나, 반환받는 순서는 동일하다.
  - 하지만 앞서 완료한 결과들이 오래 걸리는 결과들을 모두 기다려야 하는 단점이 있다.
  - 즉, 배열의 앞 순서가 먼저 완료되면 그대로 출력하고, 앞 순서가 완료되지 않으면 뒷 순서는 기다리게 하면 성능을 향상할 수 있다.

- 성능 향상 버전

  ```jsx
  urls.map(getJSON)
      .reduce(function(sequence, chapterPromise) {
        // Use reduce to chain the promises together,
        // adding content to the page for each chapter
        return sequence.then(function() {
          // Wait for everything in the sequence so far,
          // then wait for this chapter to arrive.
          return chapterPromise;
        }).then(function(chapter) {
          addHtmlToPage(chapter.html);
        });
      }, Promise.resolve());
  ```

## async/await

- 프로미스를 편하게 사용하기 위한 시맨틱 슈거

### async

- function 앞에 위치
- `async` 를 붙인 함수는 항상 프로미스를 반환. 프로미스가 아닌 값을 반환하더라도 resolved promise로 값을 감싸서 resolved promise가 반환되도록 해줌

### await

- `async` 키워드가 붙은 함수 안에서만 동작
- 프로미스가 처리될 때까지 기다림
- 프로미스가 처리되길 기다리는 동안 엔진이 다른일을 함
- 즉, `promise.then` 보다 세련된 문법. 가독성이 좋고 쓰기 좋음

### 에러 핸들링

- `await` 프로미스가 거부되면 `throw` 문처럼 에러가 던져짐
- `try...catch` 문으로 에러 핸들링 가능

### async / await 사용

```jsx
async function getJSON() {
	try{
		let response = await fetch(url);
		let json = await response.json();

		let user = json.user;
		console.log(user);
	} catch (error) {
		alert(error);
	}
}
```

### Top-level await

- 기존에는 최상위 스코프에서 `await` 를 사용할 수 없었음

- 익명 async 함수로 코드를 감싸서 사용해야했음

  ```jsx
  (async () => {
  	let res = await fetch(url);
  	let json = await res.json();
    ...
  }())
  ```

- ES2022에 최상위 `await` 가 추가됨.

- 이를 이용해 서로 다른 모듈 간 비동기 처리가 간단해질 수 있음

  ```jsx
  // A.mjs
  let todoList;
  
  const res = await fetch(url);
  todoList = await res.json();
  
  export { todoList };
  
  // B.mjs
  import { todoList } from './A.mjs';
  
  console.log(todoList);
  ```

- 이 밖에도

  - Dynamic dependency pathing
  - Resource initialization
  - Dependency fallbacks
  - WebAssembly Modules

  등에 사용될 수 있음