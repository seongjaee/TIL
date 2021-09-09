# C# coding convention :memo:

> [C# Coding Conventions](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)

- 코딩 컨벤션은

  - 일관된 코드를 만들어, 레이아웃이 아니라 내용에 집중하도록 한다.

  - 경험을 통한 추측으로 코드를 빨리 읽을 수 있도록 한다.

  - 유지 보수 변경에 용이하게 한다.

    

## Naming convention :speech_balloon:

### Pascal case

- `class`, `record`, `struct` 에는 PascalCasing을 이용한다.

- `interface` 는 `I` 접두사를 붙인다.

- `public`을 붙인 애들도 Pascal로 쓴다.



### Camel case

- `private`, `internal` 필드는 camelCasing으로 작성하고 `_` 접두사를 붙인다.

- `private`, `internal` 인 `static` 필드는 `s_` 접두사, thread static은 `t_` 접두사.
- 메서드 매개변수도 camelCase.



## Layout convention :triangular_ruler:

- 한 줄에 한 구문(statement)

- 한 줄에 한 선언(declaration)

- 메서드와 속성 정의 사이는 적어도 한 줄 비우기.

- 괄호는 다음과 같이

  ```C#
  if ((val1 > val2) && (val1 > val3))
  {
      // Take appropriate action.
  }
  ```

  

## Commenting conventions :pen:

- 주석은 별도의 줄에 작성.
- 주석은 대문자로 시작.
- 마침표로 주석 끝내기

- `//` 뒤에 한 칸 띄우기



## Language guidelines

- 짧은 문자열을 붙이고 싶다면 문자열 보간 이용, `$'{} {}'`
- 반복문으로 문자열을 붙일 때는 `StringBuilder`객체로

- 할당 시에 타입이 명확하거나, 구체적인 유형까진 중요하지 않다면 `var` 타입으로 선언

   ```c#
   var var1 = "This is clearly a string.";
   var var2 = 27;
   ```

- 명확하지 않다면 `var` 쓰지 않기 

- for 루프 변수의 타입을 암시적 타입 `var` 사용

- foreach 루프에서는 명시적 타입 사용

- 배열 선언은 간단하게!

  ```c#
  string[] vowels1 = { "a", "e", "i", "o", "u" };
  ```

- `&` 나 `|` 보단 `&&`, `||` 사용하기. 불필요한 연산을 줄일 수 있다.

- 객체 인스턴스화 하는 방법

  ```c#
  var instance1 = new ExampleClass();
  ExampleClass instance2 = new();
  ExampleClass instance2 = new ExampleClass();
  ```

  ```C#
  // 1.
  var instance3 = new ExampleClass { Name = "Desktop", ID = 37414,
      Location = "Redmond", Age = 2.3 };
  
  // 2.
  var instance4 = new ExampleClass();
  instance4.Name = "Desktop";
  instance4.ID = 37414;
  instance4.Location = "Redmond";
  instance4.Age = 2.3;
  ```

  

