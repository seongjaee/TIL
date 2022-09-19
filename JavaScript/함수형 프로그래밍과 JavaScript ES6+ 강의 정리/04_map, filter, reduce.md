# 함수형 프로그래밍과 JavaScript ES6+ 강의 정리

## 4. map, filter, reduce

- map

  ```javascript
  const map = (f, iter) => {
      let res = [];
      for (const a of iter) {
          res.push(f(a))  // f에게 위임, 수집할 값을 추상화
      }
      return res;
  };
  
  map(p => p.name, products);
  ```

- 이터러블 프로토콜을 따른 map의 다형성

  ```javascript
    document.querySelectorAll('*').map(el => el.nodeName)  // TypeError, NodeList에는 map이 없음
    
    // 앞서 정의한 map 사용
    map(el => el.nodeName, document.querySelectorAll('*'))  // ['HTML', 'HEAD', ...]
    
    const it = document.querySelectorAll('*')[Symbol.iterator]();
    it.next();  // {value: html, done: false}
    it.next();  // {value: head, done: false}
  ```

    이터러블 프로토콜을 따르는 모든 객체에 `map` 적용 가능

    ```javascript
    function *gen() {
        yield 2;
        yield 3;
        yield 4;
    }
    console.log(map(a => a * a, gen()));  // [4, 9, 16]
    ```
	```javascript
	let m = new Map();
	m.set('a', 10);
	m.set('b', 20);
	
	// 값이 2배인 새로운 Map 객체
	new Map(map(([k, a]) => [k, a * 2] , m));

- filter

  특정 조건을 만족하는 값만 걸러냄

  ```javascript
  const filter = (f, iter) => {
      let res = [];
      for (const a of iter) {
          if (f(a)) res.push(a);
      }
      return res;
  }
  
  filter(p => p.price < 20000, products)
  ```

- reduce

  이터러블 값을 하나의 값으로 축약

  ```javascript
  const reduce = (f, acc, iter) => {
      // acc가 생략되어 인자가 2개일 때 처리
      if (!iter) {
          iter = acc[Symbol.iterator]();
          acc = iter.next().value;
      }
      for (const a of iter) {
          acc = f(acc, a);
      }
      return acc;
  }
  
  const add = (a, b) => a + b;
  reduce(add, [1, 2, 3, 4, 5]);  // 15
  ```

- map + filter + reduce

  ```javascript
  const products = [
      { name: '반팔티', price: 15000 },
      { name: '긴팔티', price: 20000 },
      { name: '케이스', price: 15000 },
      { name: '후드티', price: 30000 },
      { name: '바지', price: 25000 },
  ];
  
  // 가격이 20000원 미만인 상품들의 가격 합
  const add = (a, b) => a + b;
  reduce(
  	add, 
      map(p => p.price, 
          filter(p => p.price < 20000, products)))
  
  reduce(
  	add, 
      filter(n => n < 20000, 
          map(p => p.price, products)))
  ```

  중첩되어있는 경우 코드를 오른쪽에서부터 읽어나가면 좋다.

  

