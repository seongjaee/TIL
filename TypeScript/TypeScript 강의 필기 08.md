# TypeScript 강의 필기 08

## 08. 유틸리티 타입 Utility Types

https://www.typescriptlang.org/docs/handbook/utility-types.html

`keyof`

```typescript
// keyof

interface User {
    id: number;
    name: string;
    age: number;
    gender: 'm' | 'f';
}

type UserKey = keyof User;  // 'id' | 'name' | 'age' | 'gender'

const uk:UserKey = 'name';
```



`Partial<T>`

```typescript
// Partial<T>
// 일부 속성만 사용

interface User {
    id: number;
    name: string;
    age: number;
    gender: 'm' | 'f';
}

let admin:Partial<User> = {
    id: 1,
    name: 'Bob'
}

/*
    즉,
    Partial<User> = {
    	id?: number;
        name?: string;
        age?: number;
        gender?: 'm' | 'f';
    }
*/
```



`Required<T>`

```typescript
// Required<T>
// 모든 속성을 필수로 바꿈

interface User {
    id: number;
    name: string;
    age?: number;
}

let admin: Required<User> = {  // error, age 정의해야함
    id: 1,
    name: 'Bob'
}
```



`Readonly<T>`

```typescript
// Readonly<T>
// 모든 속성을 readonly로 바꿈

interface User {
    id: number;
    name: string;
    age?: number;
}

let admin: Readonly<User> = {
    id: 1,
    name: 'Bob'
}

admin.id = 4;  // error
```



`Record<K, T>`

```typescript
// Record<K, T>

type Grade = '1' | '2' | '3' | '4';
type Score = 'A' | 'B' | 'C' | 'D';

const score: Record<Grade, Score> = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
}


interface User {
    id: number;
    name: string;
    age: number;
}

function isValid(user:User){
    const result: Record<keyof User, boolean> = {
        id : user.id > 0,
        name : user.name !== '',
        age: user.age > 0
    }
    return result;
}
```



`Pick<T,K>`

```typescript
// Pick<T,K>
// T에서 K만 뽑아서 사용

interface User {
    id: number;
    name: string;
    age: number;
    gender: 'M' | 'F';
}

const admin: Pick<User, 'id'|'name'> = {
    id: 0,
    name: 'Bob'
}
```



`Omit<T,K>`

```typescript
// Omit<T,K>
// Pick과 반대, 특정 속성을 제외하고 사용

interface User {
    id: number;
    name: string;
    age: number;
    gender: 'M' | 'F';
}

const admin: Omit<User, 'age'|'gender'> = {
    id: 0,
    name: 'Bob'
}
```



`Exclude<T1,T2>`

```typescript
// Exclude<T1,T2>
// T1에서 T2를 제외하고 사용

type T1 = string | number | boolean;
type T2 = Exclude<T1, number | string>;  // boolean
```



`NonNullable<Type>`

```typescript
// NonNullable<Type>
// null 과 undefined를 제외한 타입

type T1 = string | null | undefined | void;
type T2 = NonNullable<T1>;  // string | void
```