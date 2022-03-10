# TypeScript 강의 필기 06

## 06. 클래스 Class



```typescript
class Car {
    color: string;
    constructor(color: string){
        this.color = color;
    }
    start() {
        console.log('start')
    }
}

const bmw = new Car('red');



class Car {
    // constructor(public color: string){
    constructor(readonly color: string){
        this.color = color;
    }
    start() {
        console.log('start')
    }
}

const bmw = new Car('red');
```



접근 제한자

```typescript
// Access modifier - public, private, protected
// 따로 명시하지 않으면 public : 자식 클래스, 인스턴스 모두 접근 가능
// private : 클래스 내부에서만 접근 가능, 자식 클래스 사용 불가능, #으로 약어 사용 가능
// protected : 자식 클래스에서 접근 가능, 인스턴스에서는 접근 불가능

class Car {
    readonly name: string = 'car';
    color: string;
    constructor(color: string, name) {
        this.color = color;
        this.name = name;
    }
    start() {
        console.log('start');
    }
}

class Bmw extends Car {
    constructor(color: string, name) {
        super(color, name);
    }
    showName() {
        console.log(super.name);
    }
}

const z4 = new Bmw('black', 'zzzz');
console.log(z4.name)
```



static

```typescript
// static 정적 멤버 변수

class Car {
    readonly name: string = 'car';
    color: string;
	static wheels = 4;
    constructor(color: string, name: string) {
        this.color = color;
        this.name = name;
    }
    start() {
        console.log('start');
        console.log(this.name);
        console.log(Car.wheels);  // static은 클래스이름.변수로 사용
    }
}

class Bmw extends Car {
    constructor(color: string, name: string) {
        super(color, name);
    }
    showName() {
        console.log(super.name);
    }
}

const z4 = new Bmw('black', 'zzzz');
console.log(z4.name)
console.log(Car.wheels);
```



추상 class

```typescript
// 추상 class
abstract class Car {
    color: string;
    constructor(color: string) {
        this.color = color;
    }
    start() {
        console.log('start');
    }
    abstract doSomething():void;  // 추상 클래스의 추상 메서드는 상속 클래스에서 반드시 구현
}

class Bmw extends Car {
    constructor(color: string) {
        super(color);
    }
    doSomething() {
        alert(3);
    }
}

const z4 = new Bmw('black');

const car = new Car('red');  // error. 추상 클래스는 인스턴스를 만들 수 없음
```

