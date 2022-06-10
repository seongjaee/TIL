# TypeScript 강의 필기 02

## 02. 기본 타입

- `string`

- `number`

- `boolean`

- `number[]`

  - `Array<number>`

- `string[]`

  - `Array<string>`

- 튜플(Tuple) : `[string, number]`

- `void` : 아무것도 반환하지 않는 함수의 타입

- `never` : 영원히 끝나지 않거나, 에러를 반환하는 함수 타입

- `enum` : 비슷한 것끼리 묶어둠, 값을 명시하지 않으면 자동으로 1씩 증가하며 할당,

  특정 값만 입력하도록 강제하고 싶을 때, 그런 값들이 공통점이 있을 때 사용

  ```typescript
  enum OS {
      Windows,
      IOS,
      Android,
  }
  
  ```

  - `OS[0]` => `"Windows"`,
  - `OS[Windows]` => `0`
  - 양방향 할당

  ```typescript
  enum OS {
      Windows = 'win',
      IOS = 'ios',
      Android = 'and',
  }
  
  let myOS:OS;
  myOS = OS.Window
  ```

- `null`
- `undefined`