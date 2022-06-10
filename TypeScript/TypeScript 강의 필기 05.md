# TypeScript 강의 필기 05

## 05. 리터럴, 유니온/교차 타입

Literal Types

TypeScript에는 문자열과 숫자, 두가지 리터럴 타입이 있음.

`const`를 사용하면 변수가 가질 수 있는 값을 1개로 제한 좁힘(Narrowing)

```typescript
const userName1 = 'Bob';  // 문자형 리터럴 타입
let userName2: string | number = 'Tom';
userName2 = 3;

// 리터럴 타입은 유니언 타입과 같이 사용 가능
type Job = 'police' | 'developer' | 'teacher'

interface User {
    name: string;
    job: Job;
}

const user:User = {
    name: 'Bob',
    job: 'developer'
}

interface HighSchoolStudent {
    name: number | string;
    grade: 1 | 2 | 3;
}
```



유니언 타입

```typescript
// Union Types

interface Car {
    name: 'car';
    color: string;
    start(): void;
}

interface Mobile {
    name: 'mobile';
    color: string;
    call(): void;
}

function getGift(gift: Car | Mobile) {
    console.log(gift.color);
    if(gift.name === 'car'){
        gift.start();
    } else {
        gift.call();
    }
}
```



교차 타입

```typescript
// Intersection Types

interface Car {
    name: string;
    start(): void;
}

interface Toy {
    name: string;
    color: string;
    price: number;
}

const toyCar: Toy & Car = {
    name: 'tayo',
    start() {},
    color: 'green',
    price: 1000,
}
```

