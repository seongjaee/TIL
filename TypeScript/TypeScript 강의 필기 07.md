# TypeScript 강의 필기 07

## 07. 제네릭 Generics

제네릭을 이용하면 크래스, 함수, 인터페이스를 다양한 타입으로 재사용 가능



```typescript
// Generic

function getSize(arr:number[]):number {
    return arr.length;
}

const arr1 = [1,2,3];
getSize(arr1);

const arr2 = ['a', 'b', 'c'];
getSize(arr2);  // error
```

배열의 길이를 반환하는 함수를 작성하고 싶지만, 숫자형 배열, 문자형 배열, 객체 배열 등등...

여러 입력 타입을 받을 수 있는 함수를 작성할 수는 없을까?



```typescript
// Generic

// 함수가 호출될 때 인자를 보고 타입이 결정됨.
function getSize<T>(arr: T[]):number {
    return arr.length;
}

const arr1 = [1,2,3];
getSize<number>(arr1);  // 타입을 명시해도 되고

const arr2 = ['a', 'b', 'c'];
getSize<string>(arr2);

const arr3 = [false, true, true];
getSize(arr3);  // 타입을 명시하지 않아도 됨.
```



```typescript
// interface에서 활용

interface Mobile<T> {
    name: string;
    price: number;
    option: T;
}

const m1:Mobile<object> = {
    name: 's21',
    price: 1000,
    option: {
        color: 'red',
        coupon: false,
    }
}

const m1:Mobile<{color:string, coupon:boolean}> = {
    name: 's21',
    price: 1000,
    option: {
        color: 'red',
        coupon: false,
    }
}

const m1:Mobile<string> = {
    name: 's20',
    price: 900,
    option: 'good'
}


```



```typescript
interface User {
    name: string;
    age: number;
}

interface Car {
    name: string;
    color: string;
}

interface Book {
    price: number;
}

const user:User = { name: 'a', age: 10 };
const car:Car = { name: 'bmw', color; 'red' };
const book:Book = { price: 3000 };

// T extends { name: string }  => T는 string 타입의 name 속성을 갖는 객체를 확장한 타입
function showName<T extends { name: string }>(data: T): string {
    return data.name;
}

showName(user);
showName(car);
showName(book);  // error
```

