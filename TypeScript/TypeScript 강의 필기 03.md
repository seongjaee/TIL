# TypeScript 강의 필기 03

## 03. 인터페이스(Interface)

객체는 `object` 타입으로 선언 가능

```typescript
let user:object;
user = {
    name: 'xx',
    age: 30,
}
console.log(user.name);  // 'object' 형식에 'name' 속성이 없습니다.
```



객체의 인터페이스

```typescript
type Score = 'A' | 'B' | 'C' | 'F';  // 새로운 타입 생성, 'A', 'B', 'C', 'F' 네 개의 값 중 하나만 가능

interface User {
    name : string;
    age : number;
    gender? : string;  // ? : 있어도 되고 없어도 되는 속성
    readonly birthYear : number;  // readonly : 읽기 전용 속성
    [grade:number] : Score;  // 키:밸류 속성 여러 개 입력 가능
}

let user : User = {
    // 인터페이스의 모든 속성을 입력해야함.
    name : 'xx',
    age : 30,
    birthYear : 2000,
    1 : 'A',
    2 : 'B'
}

user.age = 10;
console.log(user.name);  // 'xx'
```



함수의 인터페이스

```typescript
interface Add {
    (num1:number, num2:number):number;  // (입력값) : 출력값
}

const add : Add = function(x, y){  // 인터페이스에서 타입 명시하면 여기선 안써도 됨.
    return x + y;
}

console.log(add(10, 20));  // 30


interface IsAdult {
    (age:num):boolean;
}

const isAdult : IsAdult = age => age > 19;

isAdult(33);  // true
```



클래스의 인터페이스

```typescript
// implements

interface Car {
  color: string;
  wheels: number;
  start(): void;
}

class Bmw implements Car {
  // 인터페이스의 모든 속성을 입력해야함.
  color;
  wheels = 4;
  constructor(c:string){
      this.color = c;
  }
  start(){
      console.log('go...');
  }
}

const b = new Bmw('red');
console.log(b);  // Bmw: {"wheels": 4, "color": "red"}
b.start();  // "go..."
```



인터페이스의 확장

```typescript
// extends

interface Car {
    color: string;
    wheels: number;
    start(): void;
}

interface Benz extends Car {
    // 추가적인 속성 선언 가능
    door: number;
    stop(): void;
}

const benz : Benz = {
    door: 5,
    stop(){
        console.log('stop')
    }
    color: 'black',
    wheels: 4,
    
}
```



확장은 여러 개도 가능

```typescript
interface Car {
    color: string;
    wheels: number;
    start(): void;
}

interface Toy {
    name: string;
}

interface ToyCar extends Car, Toy {
    price: number,
}
```





### 질문

```typescript
interface User {
  name: string;
  id: number;
}

class UserAccount {
  name: string;
  id: number;

  constructor(name: string, id: number) {
    this.name = name;
    this.id = id;
  }
}

const user: User = new UserAccount("Murphy", 1);

const user2 : UserAccount = {
  name: 'Murphy',
  id: 1,
}

console.log(user);   // UserAccount: {"name": "Murphy", "id": 1} 
console.log(user2);  // {"name": "Murphy", "id": 1} 
```

위의 코드에서 `user` 와 `user2`의 차이점

