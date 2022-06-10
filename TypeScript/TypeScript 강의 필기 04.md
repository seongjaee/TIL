# TypeScript 강의 필기 04

## 04. 함수

함수의 매개변수와 리턴값에 대한 타입 지정

```typescript
function add(num1:number, num2:number):number {
    return num1 + num2;
}

// 리턴값이 없는 경우 void
function add(num1:number, num2:number):void {
    console.log(num1 + num2);
}

```



선택적 매개변수 `?`

```typescript
// 선택적 매개변수, 인자를 넘기지 않아도 괜찮음
function hello(name?:string) {
    return `Hello, ${name || 'world'}`;
}

// 기본값을 줘도 됨
function hello(name = 'world') {
    return `Hello, ${name}`;
}
```

```typescript
// 선택적 매개변수는 맨 뒤에 와야함.
function hello(name:string, age?:number):string {
    if(age !== undefined){
        return `Hello, ${name}. You are ${age}`;
    } else {
        return `Hello, ${name}`;
    }
}

console.log(hello('Sam', 30));
console.log(hello('Sam'))

// 이렇게도 가능.
function hello(age:number | undefined, name:string):string {
    if(age !== undefined){
        return `Hello, ${name}. You are ${age}`;
    } else {
        return `Hello, ${name}`;
    }
}

console.log(hello(30, 'Sam'));
console.log(hello(undefined, 'Sam'))
```



나머지 매개변수 `...` 사용법

```typescript
// 나머지 매개변수를 사용하면 배열 타입으로
function add(...nums: number[]){
    return nums.reduce((result, num) => result + num, 0);
}

add(1, 2, 3);  // 6
add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10); // 55
```



this

```typescript
interface User {
    name: string;
}

const Sam: User = { name: 'Sam' };

// this의 타입을 정해주고 싶을 땐, 함수의 첫번째 매개변수에 this:type
function showName(this:User){
    console.log(this.name)
}

const a = showName.bind(Sam);
a();
```



오버로드

```typescript
interface User {
    name: string;
    age: number;
}

function join(name: string, age: number) User;
function join(name: string, age: string) string;

// 함수 내부 코드에서 분기 처리로 입력받는 매개변수의 타입에 따라 리턴값의 타입이 다름
// 위의 오버로드를 이용
function join(name: string, age: number | string): User | string{
    if (typeof age === 'number'){
        return {
            name,
            age,
        };
    } else {
        return '나이는 숫자로 입력해주세요'
    }
}

const sam: User = join('Sam', 30);
const jane: string = join('Jane', '30');
```

